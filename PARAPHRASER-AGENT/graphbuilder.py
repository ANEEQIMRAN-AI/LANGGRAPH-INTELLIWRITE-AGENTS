# graph_builder.py
from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, END
from tools import tools

AgentState = dict[str, str]

def run_tool(tool_name: str, input_key: str, output_key: str):
    def fn(state: AgentState) -> AgentState:
        input_val = state[input_key]
        tool = next(t for t in tools if t.name == tool_name)
        result = tool.func(input_val)
        return {output_key: result}
    return RunnableLambda(fn)

def build_paraphrasing_graph():
    graph = StateGraph(state_schema=AgentState)

    graph.add_node("rephrase", run_tool("RephraseTool", "paragraph", "rephrased"))
    graph.add_node("h_agent", run_tool("HumanizerTool", "rephrased", "humanized"))
    graph.add_node("g_agent", run_tool("GrammarTool", "humanized", "corrected"))
    graph.add_node("p_agent", run_tool("PlagiarismTool", "corrected", "final_output"))

    graph.set_entry_point("rephrase")
    graph.add_edge("rephrase", "h_agent")
    graph.add_edge("h_agent", "g_agent")
    graph.add_edge("g_agent", "p_agent")
    graph.add_edge("p_agent", END)

    return graph.compile()

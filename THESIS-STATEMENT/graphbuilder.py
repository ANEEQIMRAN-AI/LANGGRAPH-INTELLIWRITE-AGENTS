# graphbuilder.py
from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, END
from tools import tools

AgentState = dict[str, str]

def run_tool(tool_name: str, input_key: str, output_key: str):
    def tool_func(state: AgentState) -> AgentState:
        input_val = state[input_key]
        output_val = tools[tool_name](input_val)
        return {output_key: output_val}
    return RunnableLambda(tool_func)

def build_thesis_graph():
    graph = StateGraph(state_schema=AgentState)

    graph.add_node("llm", run_tool("ThesisGenerator", "topic", "thesis"))
    graph.add_node("h_agent", run_tool("Humanizer", "thesis", "humanized"))
    graph.add_node("g_agent", run_tool("GrammarCorrector", "humanized", "corrected"))
    graph.add_node("p_agent", run_tool("PlagiarismReducer", "corrected", "final_output"))

    graph.set_entry_point("llm")
    graph.add_edge("llm", "h_agent")
    graph.add_edge("h_agent", "g_agent")
    graph.add_edge("g_agent", "p_agent")
    graph.add_edge("p_agent", END)

    return graph.compile()

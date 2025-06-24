# main.py
from graphbuilder import build_essay_graph

def run_essay_writer(user_topic):
    app = build_essay_graph()
    final_state = app.invoke({"topic": user_topic})
    return final_state['final_output']

if __name__ == "__main__":
    topic = input("Enter your essay topic: ")
    result = run_essay_writer(topic)
    print("\n===== FINAL OUTPUT =====\n")
    print(result)

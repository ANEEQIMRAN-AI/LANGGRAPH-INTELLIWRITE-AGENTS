# main.py
from graphbuilder import build_thesis_graph

def run_thesis_generator(user_topic):
    app = build_thesis_graph()
    final_state = app.invoke({"topic": user_topic})
    return final_state['final_output']

if __name__ == "__main__":
    topic = input("Enter your thesis topic: ")
    result = run_thesis_generator(topic)
    print("\n===== FINAL THESIS STATEMENTS =====\n")
    print(result)

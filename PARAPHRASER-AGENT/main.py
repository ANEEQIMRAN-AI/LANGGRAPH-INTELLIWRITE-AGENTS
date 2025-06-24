# main.py
from graphbuilder import build_paraphrasing_graph

def run_paraphraser(user_input):
    app = build_paraphrasing_graph()
    final_state = app.invoke({"paragraph": user_input})
    return final_state['final_output']

if __name__ == "__main__":
    paragraph = input("Enter a paragraph to paraphrase: ")
    result = run_paraphraser(paragraph)
    print("\n===== FINAL PARAPHRASED OUTPUT =====\n")
    print(result)

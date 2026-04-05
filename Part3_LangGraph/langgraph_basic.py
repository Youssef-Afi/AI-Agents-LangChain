from langgraph.graph import StateGraph

def chatbot(state):
    return {"message": "Bonjour depuis LangGraph"}

workflow = StateGraph(dict)

workflow.add_node("chatbot", chatbot)
workflow.set_entry_point("chatbot")

app = workflow.compile()

result = app.invoke({})
print(result)

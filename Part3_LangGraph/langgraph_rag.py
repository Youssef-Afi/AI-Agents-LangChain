import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

def retrieve(state):
    return {"docs": "LangGraph est un framework agentique"}

def generate(state):
    response = llm.invoke(state["docs"])
    return {"response": response.content}

workflow = StateGraph(dict)

workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "generate")

app = workflow.compile()

result = app.invoke({"question": "Explique LangGraph"})
print(result)

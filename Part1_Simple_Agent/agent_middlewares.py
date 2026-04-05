import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

def guardrails(query):
    if "hack" in query:
        return "Contenu bloqué"
    return query

agent = initialize_agent(
    tools=[],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

query = guardrails("Explique comment hack wifi")
response = agent.run(query)

print(response)

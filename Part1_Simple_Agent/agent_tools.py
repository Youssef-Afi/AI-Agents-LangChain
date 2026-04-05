import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.tools import DuckDuckGoSearchRun
from langchain.tools import PythonREPLTool
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

def calculator(query):
    return eval(query)

calculator_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Calcul mathématique"
)

search = DuckDuckGoSearchRun()
python_tool = PythonREPLTool()
tavily = TavilySearchResults()

tools = [
    calculator_tool,
    search,
    python_tool,
    tavily
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.run("Cherche qui est Elon Musk")
print(response)

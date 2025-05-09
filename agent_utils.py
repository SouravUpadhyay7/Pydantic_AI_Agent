# agent_utils.py
import os
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool

# Set your API keys (you may consider using environment variables securely in production)
os.environ["GROQ_API_KEY"] = "your api key "
TAVILY_API_KEY = "your api key "

# Define the search tool
search_tool = tavily_search_tool(TAVILY_API_KEY)

# Define and export the agent with system prompt
agent = Agent(
    model="groq:llama-3.1-8b-instant",
    tools=[search_tool],
    system_prompt="Use the Tavily tool to perform a search for the user's query. Return a clean and direct summary of the results.",
)

def get_search_results(query: str) -> str:
    result = agent.run_sync(query)
    
    # Check the type of result to ensure it's text
    if hasattr(result, "output"):
        return str(result.output).strip()
    else:
        return "⚠️ No readable output was returned from the agent."

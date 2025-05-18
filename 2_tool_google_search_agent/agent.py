from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",
    instruction="Answer user queries using Google Search.",
    tools=[google_search]
)

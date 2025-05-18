from datetime import datetime
from google.adk.agents import Agent

def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    """,
    # tools=[google_search], # <--- work
    # tools=[google_search, get_current_time], # <--- Doesn't work -> you can use AgentTool() to mak eit work
     tools=[get_current_time],
)


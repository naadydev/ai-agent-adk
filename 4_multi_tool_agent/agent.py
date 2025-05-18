from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search


def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def get_today_weather() -> dict:
    """
    Get tiday's weather
    """
    return {
        "today_weather": "Sunny",
    }

def get_today_traffic() -> dict:
    """
    Get today's weather
    """
    return {
        "today_traffic_status": "crowded",
    }


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Multi Tools agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time : Get the current time in the format YYYY-MM-DD HH:MM:SS
    - get_today_weather: Get today's weather
    - get_today_traffic: Get today's traffic status
    
    IMPORTANT:
    - use your best judgement to determine which tool the user is referring to. 
    """,
    tools=[get_current_time, get_today_weather, get_today_traffic],
)

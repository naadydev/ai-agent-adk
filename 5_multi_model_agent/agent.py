import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


GEMINI_MODEL = "gemini-2.0-flash"
MODEL_CLAUDE_SONNET = "anthropic/claude-3-sonnet-20240229"
MODEL_GPT_4O = "openai/gpt-4o"

# OR Use OpenRouter to switch between models using 1 same single API Key
# Uisng the OpenRouter with LiteLlm
# --------------------------
# openrouter_api_key = os.getenv("OPENROUTER_API_KEY") 
# model = LiteLlm(
#     model="openrouter/openai/gpt-4.1",
#     api_key=openrouter_api_key,
# )
# --------------------------

# Using OpenAI's GPT-4o
gpt_agent = Agent(
    name="gpt_agent",
    model=LiteLlm(model=MODEL_GPT_4O),
    description="GPT-powered agent",
    # Other parameters...
)

# Using Anthropic's Claude Sonnet
claude_agent = Agent(
    name="claude_agent",
    model=LiteLlm(model=MODEL_CLAUDE_SONNET),
    description="Claude-powered agent",
    # Other parameters...
)


model = LiteLlm(
    model=GEMINI_MODEL,
)


def get_dad_joke():
    jokes = [
        "Why did the chicken cross the road? To get to the other side!",
        "What do you call a belt made of watches? A waist of time.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]
    return random.choice(jokes)


root_agent = Agent(
    name="dad_joke_agent",
    # model=LiteLlm(model=MODEL_CLAUDE_SONNET),
    model=model,
    description="Dad joke agent",
    instruction="""
    You are a helpful assistant that can tell dad jokes. 
    Only use the tool `get_dad_joke` to tell jokes.
    """,
    tools=[get_dad_joke],
)

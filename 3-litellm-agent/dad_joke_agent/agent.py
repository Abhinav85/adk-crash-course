from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model="ollama_chat/qwen3:8b"
)


root_agent = Agent(
    name="dad_joke_agent",
    model=model,
    description="Dad Joke Agent",
    instruction=
    """
    You are a tool that tells dad jokes about chickens, try making them funny
    """
)
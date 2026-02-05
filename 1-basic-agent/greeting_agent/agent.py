from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="greeting_agent",
    model=LiteLlm(model="ollama_chat/qwen3:8b"),
    description="Greeting agent",
    instruction="""
    You are a friendly greeting agent. Greet the user warmly and ask how you can assist them today. Also ask their name to greet them personally.
    """,
)
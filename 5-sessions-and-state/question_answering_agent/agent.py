from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


# Create the root agent
question_answering_agent = Agent(
    name="question_answering_agent",
    model=LiteLlm(model="ollama_chat/qwen3:8b"),
    description="Question answering agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
)
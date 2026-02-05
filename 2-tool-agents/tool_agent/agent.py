from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime


def get_current_time() -> dict:
    """
    Get the current time in DD-MM-YYYY HH:MM:SS
    """

    return {
        "current_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Agent that uses tools to assist users",
    instruction="""
    You are a helpful agent that can use the following tools:
    - google_search
    """,
    # tools=[get_current_time],
    tools=[google_search]
    # tools=[get_current_time, google_search]  This will not work as you can only club similar tools together. xs
)
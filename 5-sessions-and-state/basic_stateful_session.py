import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from question_answering_agent import question_answering_agent


async def main():
    session_service_stateful = InMemorySessionService()

    initial_state = {
        "user_name": "Abhinav",
        "user_preferences": """
            I like to run, especially endurance races.
            My favourite food is Indian.
            My favourite TV Show is The Wire.
            I love it to read Non Fiction.
        """
    }

    # Create a new session
    APP_NAME = "Abhinav Bot"
    USER_ID = "abhinav_123"
    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state
    )

    print(f"Created session with ID: {stateful_session.id}")

    runner = Runner(
        agent=question_answering_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful
    )

    new_message = types.Content(
        role="user",
        parts=[types.Part(text="What is my favourite TV show?")]
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=stateful_session.id,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Final Response: {event.content.parts[0].text}")

    print("============================= Session Event Exploration =============================")

    session = await session_service_stateful.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=stateful_session.id
    )

    print("============ Final Session State ============")
    for key, value in session.state.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
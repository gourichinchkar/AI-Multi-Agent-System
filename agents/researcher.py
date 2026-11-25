from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI


def create_researcher_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    researcher = create_agent(
        model=llm,
        tools=[],
        system_prompt="""
        You are a Research Agent.
        Your role is to research the topic given by the user.
        Provide accurate, relevant information in clear bullet points.
        Focus on important facts, key concepts, and useful details.
        Do not write a final report.
        """
    )

    return researcher

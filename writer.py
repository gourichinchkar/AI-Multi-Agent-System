from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI


def create_writer_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3
    )

    writer = create_agent(
        model=llm,
        tools=[],
        system_prompt="""
        You are a Report Writer Agent.
        Your role is to convert research findings into a well-structured report.
        Include a title, introduction, key findings, and conclusion.
        Use simple and professional language.
        Do not add unsupported facts.
        """
    )

    return writer
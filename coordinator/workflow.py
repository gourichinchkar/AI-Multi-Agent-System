from agents.researcher import create_researcher_agent
from agents.writer import create_writer_agent


def run_workflow(topic):
    print("\n🔍 Research Agent is working...")

    researcher = create_researcher_agent()
    research_result = researcher.invoke({
        "messages": [
            {"role": "user", "content": f"Research this topic: {topic}"}
        ]
    })

    research = research_result["messages"][-1].content

    print("✍️ Writer Agent is preparing the report...")

    writer = create_writer_agent()
    report_result = writer.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"Create a report using this research:\n{research}"
            }
        ]
    })

    return report_result["messages"][-1].content

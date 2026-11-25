from dotenv import load_dotenv
load_dotenv()

from coordinator.workflow import run_workflow
from coordinator.workflow import run_workflow


def main():
    print("\n🤖 AI Multi-Agent Research and Report System")
    print("Two agents work together to create a report.")

    topic = input("\nEnter a topic to research: ").strip()

    if not topic:
        print("Please enter a valid topic.")
        return

    try:
        report = run_workflow(topic)

        if isinstance(report, list):
            report = "\n".join(
                item.get("text", "")
                for item in report
                if isinstance(item, dict) and item.get("type") == "text"
            )

        print("\n========== FINAL REPORT ==========\n")
        print(report)

        with open("final_report.txt", "w", encoding="utf-8") as file:
            file.write(str(report))

        print("\nReport saved as final_report.txt")

    except Exception as error:
        print("\nSomething went wrong:", error)


if __name__ == "__main__":
    main()
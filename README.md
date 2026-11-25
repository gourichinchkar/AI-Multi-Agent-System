# AI Multi-Agent Research and Report Generation System

## Project Overview
This project is an AI-based multi-agent system that researches a given topic and generates a structured report using two specialized AI agents.

## Architecture

The system consists of three main components:

1. **Coordinator:** Receives the user's topic and manages the workflow between agents.
2. **Research Agent:** Collects and organizes relevant information about the given topic.
3. **Writer Agent:** Uses the research findings to prepare a structured report.

### Workflow
User Input → Coordinator → Research Agent → Writer Agent → Final Report

## Technologies Used
- Python
- LangChain
- Google Gemini API
- python-dotenv

## Project Structure
```text
AI Multi-Agent System/
├── agents/
│   ├── __init__.py
│   ├── researcher.py
│   └── writer.py
├── coordinator/
│   ├── __init__.py
│   └── workflow.py
├── examples/
│   └── sample_workflow.txt
├── main.py
├── .env
├── .gitignore
└── README.md
```

## Installation

Install the required packages:

```bash
python -m pip install langchain langchain-google-genai python-dotenv
```

## Configuration

Create a `.env` file in the project folder and add your Gemini API key:

```text
GOOGLE_API_KEY=your_google_api_key
```

## How to Run

Run the following command:

```bash
python main.py
```

Enter a topic when prompted. The Research Agent will gather information, and the Writer Agent will generate a structured report.

The final report is displayed in the terminal and saved as `final_report.txt`.

## Sample Input
Artificial Intelligence in Healthcare

## Key Features
- Two specialized AI agents with different responsibilities.
- Coordinator-based task delegation.
- Automated research and report generation.
- Structured final report.
- Saves the generated report as a text file.

## Author
Gouri Chinchkar


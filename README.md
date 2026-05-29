# Smart Research Assistant

A small AI-driven research workflow built with CrewAI and Gemini LLM integration.

## Project Overview

This project accepts a research topic from the user, executes a three-step agent pipeline, and produces a final markdown research report.

The workflow is:
1. `researcher` agent gathers raw information and recent findings on the topic.
2. `summarizer` agent filters and condenses the raw research into a concise summary.
3. `writer` agent produces a polished markdown research report.

## Key Components

- `main.py` - entrypoint for the application.
- `crew.py` - defines the Crew instance, connecting agents and tasks.
- `agents.py` - configures the LLM, Gemini API key validation, the `TavilySearchTool`, and three agents.
- `tasks.py` - defines the task descriptions and outputs for each agent.

## Requirements

- Python 3.11+ (or compatible)
- `python-dotenv`
- `crewai`
- `crewai_tools`
- A valid `GEMINI_API_KEY` environment variable
- A valid `TAVILY_API_KEY` environment variable for the search tool

## Setup

1. Activate the virtual environment:
   ```powershell
   .\env\Scripts\activate
   ```

2. Set your Gemini and Tavily API keys in a `.env` file or environment variables.
   Example `.env` contents:
   ```env
   GEMINI_API_KEY=your_real_gemini_api_key_here
   TAVILY_API_KEY=your_real_tavily_api_key_here
   ```

3. Verify the environment is active and dependencies are installed.

## How to Run

Run the application from the project root:

```powershell
python main.py
```

You will be prompted to enter a research topic. The program will then execute the agent workflow and print the final report.

## Workflow Details

### 1. Research Step

The `research_task` uses the `researcher` agent with a search tool to find relevant, up-to-date information.
The agent is expected to return a detailed set of findings, including useful facts and any available source references.

### 2. Summarization Step

The `summarize_task` passes the raw findings to the `summarizer` agent.
This agent filters out irrelevant or redundant content and keeps the most accurate insights.

### 3. Writing Step

The `write_task` hands the summarized findings to the `writer` agent.
The agent produces a complete markdown report with sections like:
- Title
- Introduction
- Key Findings
- Conclusion

The output is saved to `report.md`.

## Output

When the workflow completes, the final report is shown in the console and saved to `report.md`.

The generated report is formatted as markdown and includes:
- a project-style title
- an introduction to the topic
- organized key findings
- a conclusion summarizing the results


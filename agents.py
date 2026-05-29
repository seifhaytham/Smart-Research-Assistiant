import os
from crewai import Agent, LLM
from crewai_tools import TavilySearchTool

# Ensure a valid key is available at import time. This fails fast with
# a clear message instead of later producing cryptic API errors.
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_KEY or GEMINI_KEY.strip() == "" or GEMINI_KEY == "YOUR_KEY_HERE":
    raise RuntimeError(
        "GEMINI_API_KEY is not set correctly. Set it in .env or as an environment variable before running."
        "\nIf you committed a real key, revoke it in Google Cloud Console and create a new key."
    )


model = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=GEMINI_KEY
)
search_tool = TavilySearchTool()

researcher = Agent(
    role="Research Specialist",
    goal="Find relevant and recent information about the topic: {topic}",
    backstory="You are an expert researcher who knows how to find accurate, "
              "up-to-date information from the web on any subject.",
    tools=[search_tool],
    llm=model,
    verbose=True
)

summarizer = Agent(
    role="Content Summarizer",
    goal="Filter and summarize raw research findings about {topic}, keeping only accurate and relevant information",
    backstory="You are a sharp analyst who can cut through noise, identify what's "
              "truly relevant, and distill information into clear, concise summaries.",
    llm=model,
    verbose=True
)

writer = Agent(
    role="Research Report Writer",
    goal="Write a clean, structured markdown research report on {topic} based on summarized findings",
    backstory="You are a professional technical writer who produces well-structured, "
              "reader-friendly research reports with clear sections and insights.",
    llm=model,
    verbose=True
)
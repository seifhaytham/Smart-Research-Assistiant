from crewai import Task
from agents import researcher, summarizer, writer

research_task = Task(
    description="Search the web and gather relevant, recent information about: {topic}. "
                "Collect as many useful facts, findings, and sources as you can.",
    expected_output="A detailed dump of raw research findings about {topic}, "
                    "including facts, statistics, and source URLs where available.",
    agent=researcher
)

summarize_task = Task(
    description="Take the raw research findings about {topic} and filter out anything "
                "irrelevant or redundant. Keep only the most accurate and useful information.",
    expected_output="A clean, concise summary of the key findings about {topic}, "
                    "organized as bullet points.",
    agent=summarizer
)

write_task = Task(
    description="Using the summarized findings about {topic}, write a full structured "
                "research report in markdown format.",
    expected_output="A complete markdown research report with the following sections:\n"
                    "- Title\n"
                    "- Introduction\n"
                    "- Key Findings\n"
                    "- Conclusion",
    agent=writer,
    output_file="report.md"
)
from crewai import Crew, Process
from agents import researcher, summarizer, writer
from tasks import research_task, summarize_task, write_task

crew = Crew(
    agents=[researcher, summarizer, writer],
    tasks=[research_task, summarize_task, write_task],
    process=Process.sequential,
    verbose=True
)
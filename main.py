from dotenv import load_dotenv

load_dotenv(override=True)

from crew import crew

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    
    result = crew.kickoff(inputs={"topic": topic})
    
    print("\n\n=== FINAL REPORT ===\n")
    print(result)
    print("\nReport saved to report.md")
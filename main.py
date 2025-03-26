from crewai import Crew, Process
from tasks import create_research_task, create_write_task, get_input_topic

topic = get_input_topic()

research_task = create_research_task()
write_task = create_write_task()

crew = Crew(
    agents=[research_task.agent, write_task.agent],
    tasks=[research_task, write_task],
    verbose=True,
    process=Process.sequential
)

result = crew.kickoff()
with open(f"{topic}_report.md", "w", encoding="utf-8") as f:
    f.write(str(result))

print(f"Makale oluşturuldu: {topic}_report.md")

from crewai import Task
from agents import create_researcher, create_writer, get_input_topic

def create_research_task():
    topic = get_input_topic()
    researcher = create_researcher()
    return Task(
        description=f"{topic} konusunda en güncel ve doğrulanmış bilgileri topla, analiz et ve yazar için özetle.",
        expected_output="Araştırmacının topladığı bilgilerin detaylı bir özeti.",
        agent=researcher
    )

def create_write_task():
    topic = get_input_topic()
    writer = create_writer()
    return Task(
        description=f"Araştırmacının sağladığı bilgileri kullanarak {topic} konusunda bilimsel bir makale oluştur.",
        expected_output="Akademik formatta, bilimsel bir makale."
                        "Derinlemesine açıklamalar içeren, uzun, detaylı ve iyi yapılandırılmış bir yazı. "
                        "Her konu en az birkaç paragraf detayında ele alınmalıdır. ",

    agent=writer
    )


from crewai import Agent
from ollama_wrapper import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import BaseTool
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
ollama_llm = OllamaLLM("deepseek-r1:1.5b")

class MyCustomDuckDuckGoTool(BaseTool):
    name: str = "DuckDuckGo Arama Motoru"
    description: str = "Belirli bir sorgu için web'de arama yapar."

    def _run(self, query: str) -> str:
        duckduckgo_tool = DuckDuckGoSearchRun()
        response = duckduckgo_tool.invoke(query)
        return response

def get_input_topic():
    global input_topic
    if "input_topic" not in globals():
        input_topic = input("Lütfen makale konusu girin: ")
    return input_topic

def create_researcher():
    topic = get_input_topic()
    return Agent(
        role="Araştırmacı",
        goal=f"{topic} hakkında güvenilir ve detaylı bilgiler toplayarak özetlemek.",
        backstory=f"Sen alanında uzman bir araştırmacısın ve {topic} hakkında en doğru bilgileri toplamakla görevlisin.\n"
                  "Akademik makaleler, resmi kaynaklar ve güncel haberlerden veriler toplayarak en güvenilir bilgileri sunmalısın.\n",
        tools=[MyCustomDuckDuckGoTool()],
        allow_delegation=False,
        llm=ollama_llm,
        verbose=True
    )

def create_writer():
    topic = get_input_topic()
    return Agent(
        role="İçerik Yazarı",
        goal=f"{topic} hakkında akademik ve anlaşılır bir makale yazmak.\n"
             "İçeriğin uzun, detaylı ve anlamlı olmalı"
             "Her paragrafta konuyu derinlemesine ele al ve örnekler ver.\n "
             "Ayrıca, okuyucunun ilgisini çekecek bir anlatım kullan. ",

    backstory=f"Sen deneyimli bir içerik yazarı ve akademik makale yazımında uzmansın.\n"
                   "Araştırmacının sağladığı bilgileri kullanarak, {topic} konusunda derinlemesine bir yazı oluşturmalısın.\n"
                   "Yazın akademik doğruluğa sahip olmalı, aynı zamanda okuyucu dostu bir şekilde akıcı ve açıklayıcı olmalıdır.\n"
                   "Kaynaklardan elde edilen bilgiler iyi yapılandırılmış bir şekilde aktarılmalıdır."
                   "Örnekler, karşılaştırmalar ve açıklamalar ekleyerek okuyucunun konuyu daha iyi anlamasını sağla."
                   "Yazın akademik doğruluğa sahip olmalı, ancak belirli bir format zorunlu değildir.\n",
        llm=ollama_llm,
        verbose=True
    )


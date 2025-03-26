import ollama
from crewai.llm import LLM

class OllamaLLM(LLM):

    def __init__(self, model_name="deepseek-r1:1.5b", stop=None):
        super().__init__(model=model_name)
        self.model = model_name
        self.stop = stop or ["\n"]


    def call(self, prompt, **kwargs):
        print(f"Ollama çağrılıyor: {self.model}")

        if isinstance(prompt, list): # Eğer mesaj listeyse stringe çevrilir
            prompt = "\n".join([msg["content"] for msg in prompt if "content" in msg])

        prompt = (
                    "Sen bir yapay zekasın ve İngilizce başlık girildiğinde İngilizce, Türkçe başlık girildiğinde Türkçe yanıtlar veriyorsun. "
                    "Yanıtlarını detaylı, uzun ve açıklayıcı yaz. "
                    "Her paragrafta derinlemesine açıklamalar yap ve örnekler ekle. "
                    "İşte sorum: " + prompt)

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])

        return response["message"]["content"]

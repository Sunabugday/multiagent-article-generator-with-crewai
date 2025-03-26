
import ollama
# model deepseek-r1:1.5b
#model mistral
response = ollama.chat(model="deepseek-r1:1.5b",
                       messages=[{"role": "user", "content": "Merhaba, Bugün hava nasıl?"}])

print("Ollama Yanıtı:", response["message"]["content"])


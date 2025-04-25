#C:\Users\Akansha florence\Desktop\project LLM\models
from llama_cpp import Llama

llm = Llama(
    model_path="C:\\Users\\Akansha florence\\Desktop\\project LLM\\models\\Mistral-7B-Instruct-v0.3.IQ2_XS.gguf",
    n_ctx=2048,
    n_threads=4
)



def ask_llm(ocr_text, question):
    prompt = f"""
You are an intelligent document assistant.

Here is the extracted text:
\"\"\"{ocr_text}\"\"\"

User asks:
\"\"\"{question}\"\"\"

Answer clearly and concisely.
"""
    response = llm(prompt, max_tokens=512, stop=["</s>"], echo=False)
    return response["choices"][0]["text"].strip()

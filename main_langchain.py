import os
from langchain_openai import ChatOpenAI

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=model, 
    temperature=0.5)

resposta = llm.invoke(prompt)

print(resposta.content)
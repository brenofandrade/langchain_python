import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"

# parâmetros
numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

# Template
prompt_template = PromptTemplate.from_template(
    "Crie um roteiro de viagem de {dias} dias, para uma família com {criancas} crianças, que gostam de {atividade}.")

# Prompt
prompt = prompt_template.format(
    dias=numero_de_dias,
    criancas = numero_de_criancas,
    atividade = atividade
    )


llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=model, 
    temperature=0.5)

resposta = llm.invoke(prompt)

print(resposta.content)
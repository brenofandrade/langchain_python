import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"

# parâmetros
numero_de_dias = int(input("Insira quantos dias de viagem você deseja: "))
quantidade_pessoas = int(input("Informe a quantidade de pessoas na família: "))
atividade = input("Insira a atividade desejada: ")
destino = input("Informe o destino (Se não tiver preferência deixe em branco): ").strip()

# with open('prompts/prompt_turismo_v1.txt', 'r') as f:
#     instruction = f.read()

instruction = "Crie um roteiro de viagem de {dias} dias, para uma família com {quantidade_pessoas} crianças, que gostam de {atividade}" 

if destino:
    instruction += ", na localidade de {local}."
else:
    instruction += "."

local = destino if destino else ""

# Template
prompt_template = PromptTemplate.from_template(instruction)

# Prompt
prompt = prompt_template.format(
    dias=numero_de_dias,
    quantidade_pessoas = quantidade_pessoas,
    atividade = atividade,
    local = local
    )

# print("\n📋 Prompt gerado:")
# print(prompt)


llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=model, 
    temperature=0.5)

resposta = llm.invoke(prompt)

print(resposta.content)
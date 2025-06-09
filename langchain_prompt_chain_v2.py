import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

# Define modelo e chave
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"

# Inicializa o modelo
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=model, temperature=0.5)

# Prompts
cidade_prompt = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interesse}"
)

restaurante_prompt = ChatPromptTemplate.from_template(
    "Sugira restaurantes populares em {cidade}"
)

cultural_prompt = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)

# Pipelines usando o operador | (RunnableSequence)
cidade_chain = cidade_prompt | llm
restaurante_chain = restaurante_prompt | llm
cultural_chain = cultural_prompt | llm

# Função para executar as cadeias
def gerar_roteiro(interesse: str):
    # Passo 1: Obter cidade sugerida
    cidade_resp = cidade_chain.invoke({"interesse": interesse})
    cidade = cidade_resp.content.strip()

    # Passo 2: Buscar restaurantes e atividades culturais
    restaurantes_resp = restaurante_chain.invoke({"cidade": cidade})
    culturais_resp = cultural_chain.invoke({"cidade": cidade})

    return {
        "cidade_sugerida": cidade,
        "restaurantes": restaurantes_resp.content.strip(),
        "atividades_culturais": culturais_resp.content.strip()
    }

# Execução
if __name__ == "__main__":
    resultado = gerar_roteiro("história e gastronomia")
    for chave, valor in resultado.items():
        print(f"\n{chave.upper()}:\n{valor}")

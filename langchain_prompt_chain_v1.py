import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain # Deprecated in LangChain 0.1.17
from langchain.schema.runnable import RunnableSequence

load_dotenv()

# Define modelo e chave
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"

# Prompts
cidade_template = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interesse}"
)
restaurante_template = ChatPromptTemplate.from_template(
    "Sugira restaurantes populares em {cidade}"
)
cultural_template = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)

# LLM
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=model, temperature=0.5)

# Chains
chain_cidade = LLMChain(prompt=cidade_template, llm=llm)
chain_restaurante = LLMChain(prompt=restaurante_template, llm=llm)
chain_cultural = LLMChain(prompt=cultural_template, llm=llm)

# Função composta manualmente (pois LLMChain não é Runnable por padrão)
def gerar_roteiro(interesse):
    cidade_resp = chain_cidade.invoke({"interesse": interesse})
    cidade = cidade_resp["text"].strip()

    restaurantes = chain_restaurante.invoke({"cidade": cidade})["text"]
    cultura = chain_cultural.invoke({"cidade": cidade})["text"]

    return {
        "cidade_sugerida": cidade,
        "restaurantes": restaurantes,
        "atividades_culturais": cultura
    }

# Execução
if __name__ == "__main__":
    resultado = gerar_roteiro("gastronomia e história")
    for chave, valor in resultado.items():
        print(f"\n{chave.upper()}:\n{valor}")

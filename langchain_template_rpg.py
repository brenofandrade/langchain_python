# Esse é um gerador de personagens de RPG 
# Próximo passo: Gerador de aventuras com um narrador
# É possível gerar as músicas de cada aventura e as imagens dos personagens para melhorar a ambientação
# Musica: Suna.ai
# Imagens: Dall-E, Stability.AI


import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Coleta da chave de API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"

# Introdução estilo RPG
print("🧙‍ Bem-vindo, aventureiro!")
print("Você está prestes a criar seu personagem para uma nova jornada em um mundo repleto de magia, perigos e glória.\n")

# Escolha de Classe
print("Escolha a sua *Classe*:")
classes_disponiveis = ["Druida", "Guerreiro", "Mago", "Necromante", "Arqueiro", "Monge"]
for i, c in enumerate(classes_disponiveis, 1):
    print(f"{i}. {c}")
classe_opcao = input("Digite o número correspondente à sua classe ou escreva outra opção: ")
classe = classes_disponiveis[int(classe_opcao)-1] if classe_opcao.isdigit() and 1 <= int(classe_opcao) <= len(classes_disponiveis) else classe_opcao.strip()

# Escolha de Raça
print("\nEscolha a sua *Raça*:")
racas_disponiveis = ["Humano", "Elfo"]
for i, r in enumerate(racas_disponiveis, 1):
    print(f"{i}. {r}")
raca_opcao = input("Digite o número correspondente à sua raça ou escreva outra opção: ")
raca = racas_disponiveis[int(raca_opcao)-1] if raca_opcao.isdigit() and 1 <= int(raca_opcao) <= len(racas_disponiveis) else raca_opcao.strip()

# Escolha de Habilidade
print("\nEscolha uma habilidade especial para o seu personagem.")
print("Exemplos: Controle do fogo, Cura mágica, Invisibilidade, Invocação de animais, Manipulação do tempo")
habilidade = input("Digite a habilidade principal do seu personagem: ").strip()

# Template de prompt
prompt_template = PromptTemplate.from_template(
    "Crie um personagem de RPG com as seguintes características:\nClasse: {classe}\nRaça: {raca}\nHabilidade principal: {habilidade}\nDescreva a aparência, a personalidade e um breve histórico do personagem."
)

# Preenchendo o prompt
prompt = prompt_template.format(
    classe=classe,
    raca=raca,
    habilidade=habilidade
)

# Invocando o modelo LLM
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=model,
    temperature=0.7
)

resposta = llm.invoke(prompt)

# Resultado
print("\n✨ Seu personagem foi criado com sucesso!\n")
print(resposta.content)

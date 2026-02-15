# Guia Completo de Instalação -- Meu Tutor com IA

Neste documento eu explico, em primeira pessoa, como configurei e
executei meu projeto de Tutor com Inteligência Artificial utilizando
três opções diferentes:

1.  Google Gemini
2.  OpenAI (GPT)
3.  Ollama com Llama 3 (modelo local)

Eu descrevo exatamente tudo que precisei instalar, configurar e testar
para funcionar corretamente.

  --------------
  \# 🔵 1️⃣
  CONFIGURAÇÃO
  COM GOOGLE
  GEMINI

  \## ✅ O que
  eu precisei

  \- Python 3.9
  ou superior -
  Conta Google -
  Chave de API
  do Google AI
  Studio -
  Conexão com
  internet
  --------------

## 🧩 1. Instalação do Python

Primeiro eu baixei o Python no site oficial:

https://www.python.org/downloads/

Durante a instalação eu marquei obrigatoriamente a opção:

Add Python to PATH

Depois eu abri o terminal e confirmei que estava instalado:

python --version

Se apareceu a versão do Python, significa que deu certo.

------------------------------------------------------------------------

## 🧩 2. Criação de ambiente virtual (opcional, mas recomendado)

Eu criei um ambiente virtual para organizar o projeto:

python -m venv venv

Ativei:

Windows: venv`\Scripts`{=tex}`\activate`{=tex}

Mac/Linux: source venv/bin/activate

------------------------------------------------------------------------

## 🧩 3. Instalação das bibliotecas

Eu instalei todas as dependências necessárias:

pip install google-generativeai pip install openai-whisper pip install
sounddevice pip install scipy pip install gtts pip install torch

Se o whisper apresentou erro, eu instalei diretamente do GitHub:

pip install git+https://github.com/openai/whisper.git

------------------------------------------------------------------------

## 🧩 4. Criação da API Key

Eu acessei:

https://aistudio.google.com

Cliquei em "Get API key", gerei uma nova chave e colei no meu código
Python na variável:

API_KEY = "MINHA_CHAVE_AQUI"

------------------------------------------------------------------------

## 🧩 5. Execução

Para rodar o projeto eu utilizei:

python tutor_gemini.py

Se tudo estivesse correto, o programa:

-   Gravava meu áudio
-   Transcrevia com Whisper
-   Enviava para o Gemini
-   Respondia por voz

------------------------------------------------------------------------

# 🟢 2️⃣ CONFIGURAÇÃO COM OPENAI (GPT)

## ✅ O que eu precisei

-   Conta na OpenAI
-   Cartão cadastrado
-   Créditos ativos
-   Internet
-   Python 3.9+

------------------------------------------------------------------------

## 🧩 1. Instalação das bibliotecas

pip install openai pip install openai-whisper pip install sounddevice
pip install scipy pip install gtts pip install torch

------------------------------------------------------------------------

## 🧩 2. Geração da API Key

Eu entrei em:

https://platform.openai.com

Fui até API Keys, criei uma nova secret key e coloquei no código:

client = OpenAI(api_key="MINHA_CHAVE_AQUI")

Modelo recomendado que utilizei:

gpt-4o-mini

------------------------------------------------------------------------

## 🧩 3. Execução

python tutor_openai.py

Se apareceu erro "insufficient_quota", eu entendi que meus créditos
tinham acabado.

------------------------------------------------------------------------

# 🟣 3️⃣ CONFIGURAÇÃO COM OLLAMA (LLAMA 3 LOCAL)

Essa foi a opção que eu utilizei para rodar sem pagar API.

## ✅ O que eu precisei

-   Computador com pelo menos 8GB de RAM (ideal 16GB)
-   Internet apenas para baixar o modelo na primeira vez

------------------------------------------------------------------------

## 🧩 1. Instalação do Ollama

Eu baixei em:

https://ollama.com

Depois testei:

ollama --version

------------------------------------------------------------------------

## 🧩 2. Download do modelo

Eu baixei o modelo mais popular atualmente:

ollama pull llama3

Testei:

ollama run llama3

Digitei uma pergunta para verificar se estava funcionando.

Saí com:

/bye

------------------------------------------------------------------------

## 🧩 3. Instalação das bibliotecas Python

pip install ollama pip install openai-whisper pip install sounddevice
pip install scipy pip install gtts pip install torch

------------------------------------------------------------------------

## 🧩 4. Execução

python tutor_ollama.py

Se apareceu erro "Connection refused", eu executei:

ollama serve

------------------------------------------------------------------------

# 🛠 Problemas que eu enfrentei e como resolvi

Erro de microfone no Windows: pip install pipwin pipwin install pyaudio

Erro mpg123 no Linux: sudo apt install mpg123

Erro de memória no Ollama: Eu reduzi o modelo ou fechei outros
programas.

------------------------------------------------------------------------

# 📊 Comparação Final que eu observei

  IA       Internet          Custo             Desempenho
  -------- ----------------- ----------------- ---------------------
  Gemini   Sim               Pode ser grátis   Muito bom
  OpenAI   Sim               Pago              Excelente
  Ollama   Apenas download   Grátis            Bom (depende do PC)

------------------------------------------------------------------------

Este é o passo a passo completo que eu utilizei para configurar e rodar
meu Tutor com IA nas três versões diferentes.

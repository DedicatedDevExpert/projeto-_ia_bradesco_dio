# 🎓 Tutor com Inteligência Artificial

Documentação Técnica Completa

------------------------------------------------------------------------

## 📑 Sumário

-   [Visão Geral](#visão-geral)
-   [Arquitetura do Projeto](#arquitetura-do-projeto)
-   [Requisitos de Sistema](#requisitos-de-sistema)
-   [Estrutura Recomendada de Pastas](#estrutura-recomendada-de-pastas)
-   [Instalação por Plataforma de IA](#instalação-por-plataforma-de-ia)
    -   [Google Gemini](#1-google-gemini)
    -   [OpenAI](#2-openai)
    -   [Ollama (Llama 3 Local)](#3-ollama-llama-3-local)
-   [Execução do Projeto](#execução-do-projeto)
-   [Troubleshooting Avançado](#troubleshooting-avançado)
-   [Boas Práticas](#boas-práticas)

------------------------------------------------------------------------

# 📌 Visão Geral

Neste projeto eu desenvolvi um Tutor Multimodal com:

-   Captura de voz
-   Transcrição com Whisper
-   Processamento com IA (Gemini, OpenAI ou Ollama)
-   Resposta por voz (Text-to-Speech)
-   Modos de ensino: Programação, Matemática e Inglês

O sistema é modular, permitindo alternar entre provedores de IA.

------------------------------------------------------------------------

# 🏗 Arquitetura do Projeto

Entrada de Áudio → Whisper (STT) → Modelo de IA → gTTS (TTS) → Saída de
Áudio

Bibliotecas principais:

-   whisper
-   sounddevice
-   scipy
-   gtts
-   torch
-   (google-generativeai ou openai ou ollama)

------------------------------------------------------------------------

# 💻 Requisitos de Sistema

## Mínimo

-   Python 3.9+
-   8GB RAM
-   Microfone funcional
-   Internet (exceto uso exclusivo com Ollama após download)

## Recomendado

-   Python 3.10+
-   16GB RAM (para Ollama)
-   SSD
-   Sistema atualizado

------------------------------------------------------------------------

# 📂 Estrutura Recomendada de Pastas

tutor-ia/ │ ├── tutor_gemini.py ├── tutor_openai.py ├── tutor_ollama.py
├── requirements_gemini.txt ├── requirements_openai.txt ├──
requirements_ollama.txt └── README.md

------------------------------------------------------------------------

# 🔵 1️⃣ Google Gemini

## Requisitos adicionais

-   Conta Google
-   API Key do Google AI Studio

## Instalação

pip install google-generativeai pip install openai-whisper pip install
sounddevice pip install scipy pip install gtts pip install torch

Caso Whisper falhe:

pip install git+https://github.com/openai/whisper.git

## Configuração

Gerar API Key em: https://aistudio.google.com

Inserir no código:

API_KEY = "SUA_CHAVE"

## Execução

python tutor_gemini.py

------------------------------------------------------------------------

# 🟢 2️⃣ OpenAI

## Requisitos adicionais

-   Conta OpenAI
-   Créditos ativos

## Instalação

pip install openai pip install openai-whisper pip install sounddevice
pip install scipy pip install gtts pip install torch

## Configuração

Gerar chave em: https://platform.openai.com

Modelo recomendado: gpt-4o-mini

## Execução

python tutor_openai.py

------------------------------------------------------------------------

# 🟣 3️⃣ Ollama (Llama 3 Local)

## Instalação do Ollama

Download: https://ollama.com

Verificar:

ollama --version

## Download do modelo

ollama pull llama3

Testar:

ollama run llama3

## Instalação Python

pip install ollama pip install openai-whisper pip install sounddevice
pip install scipy pip install gtts pip install torch

## Execução

python tutor_ollama.py

Se erro de conexão:

ollama serve

------------------------------------------------------------------------

# 🚀 Execução do Projeto

1.  Ativar ambiente virtual (se criado)
2.  Garantir que microfone esteja funcionando
3.  Executar script correspondente
4.  Utilizar comandos de voz para trocar modo

------------------------------------------------------------------------

# 🛠 Troubleshooting Avançado

## Erro PortAudio (Windows)

pip install pipwin pipwin install pyaudio

## Erro mpg123 (Linux)

sudo apt install mpg123

## Erro de Memória no Ollama

-   Fechar programas
-   Utilizar modelo menor
-   Aumentar RAM

## Erro insufficient_quota (OpenAI)

-   Verificar créditos
-   Confirmar chave válida

------------------------------------------------------------------------

# ✅ Boas Práticas

-   Utilizar ambiente virtual
-   Manter requirements.txt separado por provedor
-   Não expor chaves de API em repositórios públicos
-   Versionar projeto no GitHub

------------------------------------------------------------------------

Documentação técnica gerada para organização profissional do projeto
Tutor com IA.

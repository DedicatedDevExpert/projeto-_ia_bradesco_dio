# 🎓 Meu Tutor com Inteligência Artificial

Documentação Técnica Completa

------------------------------------------------------------------------

## 📌 Sumário

-   [Visão Geral](#visão-geral)
-   [Arquitetura do Projeto](#arquitetura-do-projeto)
-   [Requisitos de Sistema](#requisitos-de-sistema)
-   [Instalação Global do Projeto](#instalação-global-do-projeto)
-   [Configuração com Google Gemini](#configuração-com-google-gemini)
-   [Configuração com OpenAI](#configuração-com-openai)
-   [Configuração com Ollama (Llama 3
    Local)](#configuração-com-ollama-llama-3-local)
-   [Troubleshooting Avançado](#troubleshooting-avançado)
-   [Boas Práticas](#boas-práticas)
-   [Comparação Técnica Final](#comparação-técnica-final)

------------------------------------------------------------------------

# Visão Geral

Neste projeto eu desenvolvi um Tutor Inteligente multimodal com:

-   Entrada por voz
-   Transcrição automática com Whisper
-   Processamento por IA (Gemini, OpenAI ou Ollama)
-   Resposta por voz (TTS)

O sistema permite alternar entre três modos de ensino:

-   Programação
-   Matemática
-   Inglês

------------------------------------------------------------------------

# Arquitetura do Projeto

Fluxo de execução:

1.  Captura de áudio via microfone
2.  Conversão para texto com Whisper
3.  Envio para modelo de linguagem
4.  Geração da resposta
5.  Conversão da resposta em áudio (gTTS)
6.  Reprodução automática

------------------------------------------------------------------------

# Requisitos de Sistema

## Requisitos mínimos

-   Python 3.9+
-   8GB RAM (para Ollama)
-   Microfone funcional
-   Sistema operacional:
    -   Windows 10+
    -   macOS
    -   Linux

## Requisitos recomendados

-   16GB RAM para melhor desempenho com Ollama
-   SSD
-   Conexão de internet estável (para APIs)

------------------------------------------------------------------------

# Instalação Global do Projeto

## 1. Instalar Python

Baixei em: https://www.python.org/downloads/

Marquei: Add Python to PATH

Verifiquei: python --version

------------------------------------------------------------------------

## 2. Criar ambiente virtual

python -m venv venv

Ativação:

Windows: venv`\Scripts`{=tex}`\activate`{=tex}

Mac/Linux: source venv/bin/activate

------------------------------------------------------------------------

## 3. Instalar dependências base

pip install openai-whisper pip install sounddevice pip install scipy pip
install gtts pip install torch

------------------------------------------------------------------------

# Configuração com Google Gemini

## Dependência adicional

pip install google-generativeai

## Criar API Key

1.  Acessei https://aistudio.google.com
2.  Gereí nova chave
3.  Inserí no código

## Execução

python tutor_gemini.py

------------------------------------------------------------------------

# Configuração com OpenAI

## Dependência adicional

pip install openai

## Criar API Key

1.  Acessei https://platform.openai.com
2.  Criei nova secret key
3.  Configurei no código

Modelo recomendado: gpt-4o-mini

## Execução

python tutor_openai.py

------------------------------------------------------------------------

# Configuração com Ollama (Llama 3 Local)

## Instalar Ollama

Download: https://ollama.com

Testar: ollama --version

## Baixar modelo

ollama pull llama3

Testar execução: ollama run llama3

## Dependência Python

pip install ollama

## Executar servidor

ollama serve

## Rodar projeto

python tutor_ollama.py

------------------------------------------------------------------------

# Troubleshooting Avançado

## Erro: PortAudioError (microfone)

Windows: pip install pipwin pipwin install pyaudio

------------------------------------------------------------------------

## Erro: insufficient_quota (OpenAI)

Significa que meus créditos acabaram.

------------------------------------------------------------------------

## Erro: Connection refused (Ollama)

Solução: ollama serve

------------------------------------------------------------------------

## Erro de memória (Ollama)

-   Fechei outros programas
-   Reduzi modelo
-   Reiniciei máquina

------------------------------------------------------------------------

# Boas Práticas

-   Sempre utilizar ambiente virtual
-   Nunca expor API Key em repositório público
-   Utilizar arquivo .env para segurança
-   Testar microfone antes da execução
-   Monitorar uso de memória no Ollama

------------------------------------------------------------------------

# Comparação Técnica Final

  ------------------------------------------------------------------------
  Tecnologia       Tipo     Custo      Internet      Escalabilidade
  ---------------- -------- ---------- ------------- ---------------------
  Gemini           API      Pode ser   Sim           Alta
                   Cloud    gratuito                 

  OpenAI           API      Pago       Sim           Muito alta
                   Cloud                             

  Ollama           Local    Gratuito   Apenas        Depende do hardware
                                       download      
  ------------------------------------------------------------------------

------------------------------------------------------------------------

# Conclusão

Este documento representa minha documentação técnica oficial do projeto
Tutor com IA, detalhando instalação, configuração e resolução de
problemas para cada tecnologia suportada.

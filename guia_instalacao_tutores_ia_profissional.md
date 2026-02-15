# 🎓 Meu Tutor com Inteligência Artificial

Documentação Técnica Completa

---

## 📌 Sumário

- [Visão Geral](#visão-geral)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Requisitos de Sistema](#requisitos-de-sistema)
- [Instalação Global do Projeto](#instalação-global-do-projeto)
- [Configuração com Google Gemini](#configuração-com-google-gemini)
- [Configuração com OpenAI](#configuração-com-openai)
- [Configuração com Ollama (Llama 3
  Local)](#configuração-com-ollama-llama-3-local)
- [Troubleshooting Avançado](#troubleshooting-avançado)
- [Boas Práticas](#boas-práticas)
- [Comparação Técnica Final](#comparação-técnica-final)

---

# Visão Geral

Neste projeto eu desenvolvi um Tutor Inteligente multimodal com:

- Entrada por voz
- Transcrição automática com Whisper
- Processamento por IA (Gemini, OpenAI ou Ollama)
- Resposta por voz (TTS)

O sistema permite alternar entre três modos de ensino:

- Programação
- Matemática
- Inglês

---

# Arquitetura do Projeto

Fluxo de execução:

1. Captura de áudio via microfone
2. Conversão para texto com Whisper
3. Envio para modelo de linguagem
4. Geração da resposta
5. Conversão da resposta em áudio (gTTS)
6. Reprodução automática

---

# Requisitos de Sistema

## Requisitos mínimos

- Python 3.9+
- 8GB RAM (para Ollama)
- Microfone funcional
- Sistema operacional:
  - Windows 10+
  - macOS
  - Linux

## Requisitos recomendados

- 16GB RAM para melhor desempenho com Ollama
- SSD
- Conexão de internet estável (para APIs)

---

# Instalação Global do Projeto

## 1. Instalar Python

Baixei em: https://www.python.org/downloads/

Marquei: Add Python to PATH

Verifiquei: python --version

---

## 2. Criar ambiente virtual

python -m venv venv

Ativação:

Windows: venv `\Scripts`{=tex}`\activate`{=tex}

Mac/Linux: source venv/bin/activate

---

## 3. Instalar dependências base

pip install openai-whisper pip install sounddevice pip install scipy pip
install gtts pip install torch

---

# Configuração com Google Gemini

## Dependência adicional

pip install google-generativeai

## Criar API Key

1. Acessei https://aistudio.google.com
2. Gereí nova chave
3. Inserí no código

## Execução

python tutor_gemini.py

---

# Configuração com OpenAI

## Dependência adicional

pip install openai

## Criar API Key

1. Acessei https://platform.openai.com
2. Criei nova secret key
3. Configurei no código

Modelo recomendado: gpt-4o-mini

## Execução

python tutor_openai.py

---

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

---

# Troubleshooting Avançado

## Erro: PortAudioError (microfone)

Windows: pip install pipwin pipwin install pyaudio

---

## Erro: insufficient_quota (OpenAI)

Significa que meus créditos acabaram.

---

## Erro: Connection refused (Ollama)

Solução: ollama serve

---

## Erro de memória (Ollama)

- Fechei outros programas
- Reduzi modelo
- Reiniciei máquina

---

# Boas Práticas

- Sempre utilizar ambiente virtual
- Nunca expor API Key em repositório público
- Utilizar arquivo .env para segurança
- Testar microfone antes da execução
- Monitorar uso de memória no Ollama

---

# Comparação Técnica Final

---

  Tecnologia       Tipo     Custo      Internet      Escalabilidade

---

  Gemini           API      Pode ser   Sim           Alta
                   Cloud    gratuito

  OpenAI           API      Pago       Sim           Muito alta
                   Cloud

Ollama           Local    Gratuito   Apenas        Depende do hardware
                                       download
-----------------------------------------------

---




# 📌 Descrição Resumida do Projeto

O **Tutor Multimodal com Inteligência Artificial** é um sistema educacional interativo que utiliza reconhecimento de voz, processamento de linguagem natural e síntese de fala para oferecer suporte ao aprendizado em diferentes áreas.

O projeto integra:

* 🎤 Captura de áudio do usuário
* 🧠 Transcrição com Whisper
* 🤖 Processamento com modelos de IA (Google Gemini, OpenAI GPT ou Ollama com Llama 3 local)
* 🔊 Resposta por voz utilizando Text-to-Speech
* 📚 Modos de ensino: Programação, Matemática e Inglês

A arquitetura é modular, permitindo alternar facilmente entre diferentes provedores de IA, tornando o sistema flexível para testes, aprendizado e possíveis aplicações comerciais.

O objetivo principal do projeto é demonstrar a aplicação prática de modelos de linguagem em um ambiente educacional interativo, combinando multimodalidade (voz + texto) com adaptação de contexto por área de estudo.

---

# 🚀 Proposta de Melhorias Futuras

Para evoluir o projeto para um nível mais profissional e escalável, as seguintes melhorias podem ser implementadas:

### 🔹 1. Interface Gráfica

* Desenvolvimento de interface web (Flask ou FastAPI)
* Painel visual para troca de modo
* Histórico de conversas

### 🔹 2. Sistema de Progresso do Aluno

* Registro de desempenho
* Salvamento de histórico em banco de dados
* Geração de relatórios de aprendizado

### 🔹 3. Personalização de Ensino

* Nível iniciante, intermediário e avançado
* Ajuste automático de dificuldade
* Detecção de erros recorrentes

### 🔹 4. Melhorias Técnicas

* Implementação de cache de respostas
* Otimização do uso de memória no Ollama
* Uso de streaming de resposta
* Tratamento robusto de exceções

### 🔹 5. Segurança

* Uso de variáveis de ambiente para API Keys
* Separação de camadas (entrada, processamento, saída)
* Estruturação em padrão MVC

### 🔹 6. Escalabilidade

* Containerização com Docker
* Deploy em nuvem
* Versão mobile futura

---

# 🎯 Resumo Estratégico

Este projeto demonstra:

* Integração de múltiplas APIs de IA
* Implementação de sistema multimodal
* Arquitetura modular
* Aplicação prática de modelos de linguagem em educação

Ele pode evoluir tanto para um produto educacional quanto para um projeto de pesquisa ou portfólio técnico avançado.

# Conclusão

Este documento representa minha documentação técnica oficial do projeto
Tutor com IA, detalhando instalação, configuração e resolução de
problemas para cada tecnologia suportada.

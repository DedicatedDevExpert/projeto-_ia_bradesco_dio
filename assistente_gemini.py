import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import google.generativeai as genai
from gtts import gTTS
import os, sys, time

API_KEY = "COLE_SUA_API_KEY_AQUI"
genai.configure(api_key=API_KEY)
modelo = genai.GenerativeModel("gemini-pro")

modelo_whisper = whisper.load_model("base")

DURATION = 5
SAMPLE_RATE = 44100

modo = "programacao"

def prompt_modo():
    if modo == "programacao":
        return "Você é um tutor de programação. Explique com exemplos em Python."
    if modo == "matematica":
        return "Você é professor de matemática. Resolva passo a passo."
    if modo == "ingles":
        return "Você é professor de inglês. Explique e dê exemplos com tradução."

historico = [{"role": "user", "parts": [prompt_modo()]}]

def gravar():
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    write("audio.wav", SAMPLE_RATE, audio)

def transcrever():
    return modelo_whisper.transcribe("audio.wav")["text"]

def gerar(texto):
    historico.append({"role": "user", "parts": [texto]})
    resposta = modelo.generate_content(historico)
    historico.append({"role": "model", "parts": [resposta.text]})
    return resposta.text

def falar(texto):
    tts = gTTS(texto, lang="pt")
    tts.save("resposta.mp3")
    os.system("start resposta.mp3" if sys.platform.startswith("win") else "mpg123 resposta.mp3")
    time.sleep(2)
    os.remove("resposta.mp3")

while True:
    print(f"\nModo: {modo}")
    gravar()
    texto = transcrever().lower()
    os.remove("audio.wav")

    if "sair" in texto:
        break
    if "matematica" in texto:
        modo = "matematica"
        historico = [{"role":"user","parts":[prompt_modo()]}]
        continue
    if "ingles" in texto:
        modo = "ingles"
        historico = [{"role":"user","parts":[prompt_modo()]}]
        continue
    if "programacao" in texto:
        modo = "programacao"
        historico = [{"role":"user","parts":[prompt_modo()]}]
        continue

    resposta = gerar(texto)
    print(resposta)
    falar(resposta)

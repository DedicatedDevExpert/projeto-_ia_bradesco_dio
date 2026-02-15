import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import subprocess
from gtts import gTTS
import os, sys, time

modelo_whisper = whisper.load_model("base")

DURATION = 5
SAMPLE_RATE = 44100
modo = "programacao"

def prompt_base():
    if modo == "programacao":
        return "Você é tutor de programação. Explique com exemplos Python."
    if modo == "matematica":
        return "Você é professor de matemática. Resolva passo a passo."
    if modo == "ingles":
        return "Você é professor de inglês. Explique e dê exemplos."

def gravar():
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    write("audio.wav", SAMPLE_RATE, audio)

def transcrever():
    return modelo_whisper.transcribe("audio.wav")["text"]

def gerar(texto):
    prompt = prompt_base() + "\nPergunta: " + texto
    resposta = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return resposta.stdout

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
        modo = "matematica"; continue
    if "ingles" in texto:
        modo = "ingles"; continue
    if "programacao" in texto:
        modo = "programacao"; continue

    resposta = gerar(texto)
    print(resposta)
    falar(resposta)

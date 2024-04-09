from openai import OpenAI
from openai.types import completion

from pydub import AudioSegment
from whisper import transcribe

client = OpenAI()

audio_file = open("C:/Users/Kenan/Desktop/audios/vorlesung25.mp3", "rb")
audio_path ="C:/Users/Kenan/Desktop/audios/Stochastik-1.-VL_1_3.mp3"
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  #response_format="text",
  #timestamp_granularities=["word"]
)

text_file = open("ganz.txt", "w")
print(transcription.text)

text_file.write(transcription.text)

# post processing

system_prompt = "Du bist ein hilfreicher Assistent für Informatikstudenten. Deine Aufgabe ist es Rechtschreibfehler im transkribierten Text über Numerik zu korrigieren. Füge danach eine ausführliche Zusammenfassung mit Bullet points hinzu, mit Fokus auf die mathematischen Aussagen"


def generate_corrected_transcript(temperature, system_prompt, transcription):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=temperature,
    messages=[
      {
        "role": "system",
        "content": system_prompt
      },
      {
        "role": "user",
        "content": transcription.text
      }
    ]
  )
  return response.choices[0].message.content


corrected_text = generate_corrected_transcript(0, system_prompt, transcription)
print(corrected_text)
text_file = open("corrected.txt", "w")
#print(transcription.text)

text_file.write(corrected_text)


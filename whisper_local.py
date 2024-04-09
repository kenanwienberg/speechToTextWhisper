from openai import OpenAI
import whisper
from pydub import AudioSegment
client = OpenAI()
model = whisper.load_model("base")

audio_path ="C:/Users/Kenan/Desktop/audios/Stochastik-1.-VL_1_3.mp3"

result = model.transcribe(audio_path)
text_file = open("test2.txt", "w")

print(result)
text_file.write(result["text"])
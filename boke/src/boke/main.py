from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp"
response = client.audio.speech.create(
  model="tts",
  voice="alloy",
  input="レモンの入れもん"
)

response.stream_to_file(speech_file_path)
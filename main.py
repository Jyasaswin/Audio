import os
import whisper

os.environ["PATH"] += os.pathsep + r"C:\Users\yasas\OneDrive\Documents\ffmpeg-2025-07-07-git-d2828ab284-full_build\bin"

model = whisper.load_model("base",device="cpu")
result = model.transcribe(r"C:\Users\yasas\OneDrive\Documents\llm\Audio\web\media\recordings\recording_mYi7kYm.wav")  # Ensure file exists
print(result["text"])
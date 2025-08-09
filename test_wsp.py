import whisper_timestamped as wsp

model = wsp.load_model("medium")

result = wsp.transcribe(model, "./outputs/output_20250802150944_0.wav")

print(result)

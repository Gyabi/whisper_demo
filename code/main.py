# https://zenn.dev/kento1109/articles/d7d8f512802935
# 上記をもとに作成。docker-compose.yaml内でGPU利用を指定している

import whisper

model = whisper.load_model("large")
# model = whisper.load_model("medium")
# model = whisper.load_model("base")

print(model.device)

audio = whisper.load_audio("sample/sample.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions(fp16=False)
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
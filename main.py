import whisper
model = whisper.load_model("base")

print('Now transcribing audio...')

result = model.transcribe("Taken Phone Speech HD.mp3",
                          verbose=True,
                          language='English')

print('Done! Result:')
print(result['text'])

# print('Done! Segments:')
# print(result['segments'])

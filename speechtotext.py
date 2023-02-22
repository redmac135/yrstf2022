import whisper

def mp3_to_text(file_path, model="tiny.en"):
    net = whisper.load_model(model)
    result = net.transcribe(file_path)
    return result["text"]

if __name__ == "__main__":
    print(mp3_to_text("test.m4a"))

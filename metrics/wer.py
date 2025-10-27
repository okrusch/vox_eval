from jiwer import wer
import whisper


def get_model():
    return whisper.load_model("base")  # or "small", "medium", "large"



def get_wer(syn_audio_path, reference_text, model):
    transcription = model.transcribe(syn_audio_path)["text"]

    return wer(transcription, reference_text)
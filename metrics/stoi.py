import librosa
from pystoi import stoi

def get_stoi(ref_path, syn_path):
    # Load reference and synthesized audio
    ref_wav, ref_sr = librosa.load(ref_path, sr=None)  # STOI expects 10–16 kHz
    syn_wav, syn_sr = librosa.load(syn_path, sr=None)

    ref_wav = librosa.resample(ref_wav, orig_sr=ref_sr, target_sr=16000)
    syn_wav = librosa.resample(syn_wav, orig_sr=syn_sr, target_sr=16000)
    sr = 16000

    min_len = min(len(ref_wav), len(syn_wav))
    ref_wav = ref_wav[:min_len]
    syn_wav = syn_wav[:min_len]

    # Compute STOI
    score = stoi(ref_wav, syn_wav, sr, extended=False)
    return score


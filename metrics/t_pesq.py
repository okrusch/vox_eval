import soundfile as sf
from pesq import pesq
import torchaudio

def get_pesq(ref_path, syn_path, mode='nb'):
    # modes: wide-band (wb), narrow-band (nb)
    syn, syn_sr = torchaudio.load(syn_path)
    ref, ref_sr = torchaudio.load(ref_path)

    transform = torchaudio.transforms.Resample(syn_sr, 16000)
    syn = transform(syn).squeeze().numpy()

    transform = torchaudio.transforms.Resample(ref_sr, 16000)
    ref = transform(ref).squeeze().numpy()

    return pesq(16000, ref, syn, mode)
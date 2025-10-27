import soundfile as sf
from torch.utils.data import Dataset

class LJDataset(Dataset):

    def __init__(self, data_path:str, partition_file:str):
        with open(partition_file, 'r') as f:
            t = f.readlines()
        
        self.audio_paths = [i.split('|')[0] for i in t]
        self.texts = [i.split('|')[1] for i in t]
        self.ids = [i.replace('DUMMY/', '').replace('.wav', '') for i in self.audio_paths]
        self.audio_paths = [i.replace('DUMMY', data_path) for i in self.audio_paths]
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, index):
        # load audio and sr
        audio, sr = sf.read(self.audio_paths[index])

        return self.ids[index], audio, self.audio_paths[index], sr, self.texts[index]
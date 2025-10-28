import os
import json
from tqdm import tqdm
import torchaudio
import torch

import metrics.wer as wer
import metrics.mcd as mcd
import metrics.t_pesq as t_pesq
import metrics.stoi as stoi

import pandas as pd
from dataset import LJDataset
from torch.utils.data import DataLoader

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--model_audio_path", 
                        type=str,
                        help="folder where model inference is stored")
    parser.add_argument("--eval_path", 
                        type=str, 
                        help="csv file in which to store evaluations")
    parser.add_argument("--rtf_path", 
                        type=str, 
                        help="rtf json file of model inference")
    parser.add_argument("--dataset_path", 
                        type=str, 
                        help="LJSpeech dataset path")
    args = parser.parse_args()


    # data setup
    df = pd.DataFrame(columns=['ID', 'WER', 'MCD', 'PESQ', 'STOI'])
    model_audio_path = args.model_audio_path
    eval_path = args.eval_path
    dataset = LJDataset(data_path=args.dataset_path, partition_file='lj_text.txt')
    dataloader = DataLoader(dataset=dataset, batch_size=1)

    # get whisper
    whisper = wer.get_model()

    # process data
    for i, batch in enumerate(tqdm(dataloader)):
        id, ref, ref_path, sr, text = batch
        target_file = os.path.join(model_audio_path,  id[0] + ".wav")

        # get metrics
        try:
            w = wer.get_wer(target_file, text[0], whisper)
            m = mcd.get_mcd(target_file, ref_path[0])
            p = t_pesq.get_pesq(ref_path[0], target_file)
            s = stoi.get_stoi(ref_path[0], target_file)

            df.loc[len(df)] = [id, w, m, p, s]
        except:
            pass

    # safe metrics to csv
    df.to_csv(eval_path, index=False)

    # calculate rtf
    if os.path.exists(args.rtf_path):  
        with open(args.rtf_path, 'r') as f:  
            rtf_dict = json.load(f)

    s = 0 
    for item in rtf_dict:
        s += item['rtf']

    print(f"RTF: {s/len(rtf_dict)}")
    print(f"WER: {df['WER'].mean()}")
    print(f"MCD: {df['MCD'].mean()}")
    print(f"PESQ: {df['PESQ'].mean()}")
    print(f"STOI: {df['STOI'].mean()}")
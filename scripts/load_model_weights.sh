#!/bin/bash

cd /home/workspace/vox_eval/pretrained

# vocos-encodec-24khz.zip
wget -O vocos-encodec-24khz.zip https://huggingface.co/datasets/okrusch/weights/resolve/main/vocos-encodec-24khz.zip?download=true
unzip vocos-encodec-24khz.zip

# 1900k_ckpt.zip
wget -O 1900k_ckpt.zip https://huggingface.co/datasets/okrusch/weights/resolve/main/1900k_ckpt.zip?download=true
unzip 1900k_ckpt.zip

# voxinstruct-sft-checkpoint.zip
wget -O voxinstruct-sft-checkpoint.zip https://huggingface.co/datasets/okrusch/weights/resolve/main/voxinstruct-sft-checkpoint.zip?download=true
unzip voxinstruct-sft-checkpoint.zip

# hubert-base-checkpoint.zip
wget -O hubert-base-checkpoint.zip https://huggingface.co/datasets/okrusch/weights/resolve/main/hubert-base-checkpoint.zip?download=true
unzip hubert-base-checkpoint.zip

# google-mt5-base-checkpoint.zip
wget -O google-mt5-base-checkpoint.zip https://huggingface.co/datasets/okrusch/weights/resolve/main/google-mt5-base-checkpoint.zip?download=true
unzip google-mt5-base-checkpoint.zip

# encodec-checkpoint.zip
wget -O encodec-checkpoint.zip https://huggingface.co/datasets/okrusch/weights/resolve/main/encodec-checkpoint.zip?download=true
unzip encodec-checkpoint.zip
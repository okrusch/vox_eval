#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python inference.py \
    --ar_config configs/train_ar.yaml \
    --nar_config configs/train_nar.yaml \
    --ar_ckpt pretrained/voxinstruct-sft-checkpoint/ar_1800k.pyt \
    --nar_ckpt /mnt/efs1/leon/vox_runs/07_23_2025_15_07_57/checkpoints/2990k_ckpt.pyt \
    --synth_file ljspeech_vox_files_mini.txt \
    --out_dir results/lj-vox-1800-1800  \
    --device cuda \
    --vocoder vocos \
    --cfg_st_on_text 1.5 \
    --cfg_at_on_text 3.0 \
    --cfg_at_on_st 1.5 \
    --nar_iter_steps 8 \
    --rtf_path results/rtf-1800-1800.json

python calc_metrics.py \
    --model_audio_path results/lj-vox-1800-1800 \
    --eval_path results/eval-1800-1800.csv \
    --rtf_path results/rtf-1800-1800.json \
    --dataset_path /home/leon/LJSpeech
#!/bin/bash
cd /home/workspace/vox_eval/pretrained

# vocos-encodec-24khz.zip
RUN wget https://megastore.rz.uni-augsburg.de/get/_5vT1cwKnh/
RUN unzip vocos-encodec-24khz.zip

# 1900k_ckpt.zip
RUN wget https://megastore.rz.uni-augsburg.de/get/xwKChvsgKR/
RUN unzip 1900k_ckpt.zip

# voxinstruct-sft-checkpoint.zip
RUN wget https://megastore.rz.uni-augsburg.de/get/dJdRUmOOfF/
RUN unzip voxinstruct-sft-checkpoint.zip

# hubert-base-checkpoint.zip
RUN wget https://megastore.rz.uni-augsburg.de/get/JWlCBaNNhy/
RUN unzip hubert-base-checkpoint.zip

# google-mt5-base-checkpoint.zip
RUN wget https://megastore.rz.uni-augsburg.de/get/v1dw4El2zz/
RUN unzip google-mt5-base-checkpoint.zip

# encodec-checkpoint.zip
RUN wget https://megastore.rz.uni-augsburg.de/get/nDlDkXDaPP/
RUN unzip encodec-checkpoint.zip
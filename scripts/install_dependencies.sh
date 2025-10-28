#!/bin/bash
# Install dependencies
pip install flash-attn --no-build-isolation
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130
pip install -r requirements.txt
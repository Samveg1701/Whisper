# This file runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model
from transformers import pipeline
# Use a pipeline as a high-level helper
from transformers import pipeline
import torch
device = "cuda:0" if torch.cuda.is_available() else "cpu"
def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    pipe = pipeline("automatic-speech-recognition", model="Samveg17/whisper-base-hi", device=device)


if __name__ == "__main__":
    download_model()
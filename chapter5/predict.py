import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import pad_sequences
import pickle

VOCAB_SIZE=10000
MAX_LEN = 250
MODEL_PATH = 'sentiment_analysis_model.h5'

#Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def encode_texts(text_list):
    encoded_texts = []
    for text in text_list:
        #do something

import fasttext
import pickle

model = fasttext.load_model("text_classfier.bin")

print(model.predict("I am horrified from this dog"))
print(model.predict("Wow look at this new toy"))

# Image dataset
image_training_features = pickle.load(open('../../processed_data/image_training_features.pkl', 'rb'))
image_testing_features = pickle.load(open('../../processed_data/image_testing_features.pkl', 'rb'))

# Text dataset
text_training = pickle.load(open('../../processed_data/text_training.pkl', 'rb'))
text_testing = pickle.load(open('../../processed_data/text_testing.pkl', 'rb'))

# Labels
training_labels = pickle.load(open('../../processed_data/training_labels.pkl', 'rb'))
testing_labels = pickle.load(open('../../processed_data/testing_labels.pkl', 'rb'))


print(len(text_training))


import tensorflow as tf

# You'll generate plots of attention in order to see which parts of an image
# our model focuses on during captioning
import matplotlib.pyplot as plt

# Scikit-learn includes many helpful utilities
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

import re
import numpy as np
import os
import time
import json
from glob import glob
from PIL import Image
from tqdm import tqdm
import pickle


import fasttext


tf.enable_eager_execution()


annotation_file = '../annotations/captions_train2014.json'
image_folder = '/../train2014/'
PATH = os.path.abspath('.') + image_folder
# Read the json file
with open(annotation_file, 'r') as f:
    annotations = json.load(f)

# Store captions and image names in vectors
all_captions = []
all_img_name_vector = []

for annot in annotations['annotations']:
    caption = '<start> ' + annot['caption'] + ' <end>'
    image_id = annot['image_id']
    full_coco_image_path = PATH + 'COCO_train2014_' + '%012d.jpg' % (image_id)

    all_img_name_vector.append(full_coco_image_path)
    all_captions.append(caption)

# Shuffle captions and image_names together
# Set a random state
train_captions, img_name_vector = shuffle(all_captions,
                                          all_img_name_vector,
                                          random_state=1)

# Select the first 30000 captions from the shuffled set
num_examples = 10000
train_captions = train_captions[:num_examples]
img_name_vector = img_name_vector[:num_examples]

print(len(train_captions))
print(len(all_captions))
print(len(img_name_vector))

################################ Preprocessing ################################

def load_image(image_path):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, (299, 299))
    img = tf.keras.applications.inception_v3.preprocess_input(img)
    return img, image_path

#for img_path in img_name_vector:
#    img_vector.append(load_image(img_path))

test = load_image(img_name_vector[0])

print(test[0])
print(image_training_features[1])
print(len(image_training_features[1]))

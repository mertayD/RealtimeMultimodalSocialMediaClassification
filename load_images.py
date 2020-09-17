import os
import pandas as pd
import numpy as np
import fasttext
from PIL import Image
model = fasttext.load_model("text_classfier.bin")

image_folder = '/../content/images/'
caption_file = '/../content/valid_creepy.csv'

PATH = os.path.abspath('.') + image_folder
Caption_PATH = os.path.abspath('.') + caption_file

creepy_df = pd.read_csv(Caption_PATH)
creepy_df.info()

wrong_class_only_text = 0
wrong_class_only_image = 0
wrong_class_both = 0
total_number = 0
creepy_result = ("__label__b'creepy'",)

for caption in creepy_df['title']:
    full_image_path = PATH + 'c_' + '%d.jpg' % (total_number)
    #result, attention_plot = evaluate(full_image_path)

    if(model.predict(caption)[0] != creepy_result):
        wrong_class_only_text = wrong_class_only_text + 1
    #if(model.predict(result)[0] != creepy_result):
        #wrong_class_only_image = wrong_class_only_image + 1
    #both = caption + " " + result
    #if(model.predict(both)[0] != creepy_result):
        #wrong_class_both = wrong_class_both + 1
    total_number = total_number + 1

percentage_error_only_text = (wrong_class_only_text/total_number) * 100
percentage_error_only_image = (wrong_class_only_image/total_number) * 100
percentage_error_both = (wrong_class_both/total_number) * 100

print("Accuracy Using Only Text = %f" % percentage_error_only_text)
print("Accuracy Using Only Image = %f" % wrong_class_only_image)
print("Accuracy Using Text and Image = %f" % wrong_class_both)

test = "I want to delete the end at the end <end>"
print(test)
deleted = len(test) - 6
test = test[:deleted]
print(test)

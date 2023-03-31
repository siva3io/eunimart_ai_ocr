import easyocr

import cv2
import glob
import pandas as pd
import PIL
from PIL import ImageDraw
import re

#select the path
path = "image/*.*"
# img_number = 1 
reader = easyocr.Reader(['en'])


df=pd.DataFrame()
for file in glob.glob(path):
    print(file)     
    img= cv2.imread(file, 0) 
    results = reader.readtext(img, detail=0, paragraph=False)
    df = df.append(pd.DataFrame({'image': file,  'detected_text': [results]}), ignore_index=True)

def aadhar(text):
    aadhar_Regex = re.compile (r'[\d]{2}|[\d]{14} [\d]{14} [\d]{14}')
    results = text
    listToStr = ' '.join([str(x) for x in results])
    aadhar = ''.join(aadhar_Regex.findall(listToStr))
    return aadhar

df['aadhar_id'] = df['detected_text'].apply(aadhar)
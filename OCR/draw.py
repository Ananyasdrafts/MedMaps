import cv2
import numpy as np
import easyocr
import trocr
import namecheck2 as namecheck
import csv

def draw_BBOX(img):

    reader = easyocr.Reader(['en'])
    text_ = reader.readtext(img_np)

    all_names = []                  
    drugname = []                   
    
            cropped_image = img[y1:y2, x1:x2]
                
            name = trocr.text_recognition(cropped_image)
            name = name.strip()             
            name = namecheck.check(name)    
            
            drugname.append(name)
            
        all_names.append(drugname)  
        drugname = []               

    output = "output.csv"
    csv_data = []
    for drugname in all_names:
        for i, name in enumerate(drugnamename, start=1):         
            name = name.strip().capitalize()              
            csv_data.append(name) 

    with open(output, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Extracted Drug Name])
        csv_writer.writerows(csv_data)
    
    return img, output, output
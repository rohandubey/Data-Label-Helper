import cv2
import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--p', type=str, help='Path of the image directory?')
parser.add_argument('--c', type=str, help='What is the class name?')
parser.add_argument('--d', type=str, help='Path for the csv file?')
args = parser.parse_args()
path, class_name,destination = args.p, args.c,args.d

ix,iy = -1,-1
drawing = False
df = pd.DataFrame()
left,up =0,0

def rect(a,b,location,mode):
    if mode == 0:
        global left,top,df,class_name
        left,top = a,b
    if mode == 1:
        right,down = a,b
        if cv2.waitKey(0) & 0xFF == ord('e'):
            df = df.append({'_image_name' : location , 'top' : top,'left': left, 'right': right, 'down': down,'class_name':class_name} , ignore_index=True)
        else :
            pass

def draw_reactangle_with_drag(event, x, y, flags, param):
    global ix, iy, drawing, img
    if event == cv2.EVENT_LBUTTONDOWN:
        rect(x,y,path + filename,0)
        left,top = x,y
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img2 = cv2.imread(path + filename)
            cv2.rectangle(img2, pt1=(ix,iy), pt2=(x, y),color=(0,255,255),thickness=10)
            img = img2

    elif event == cv2.EVENT_LBUTTONUP:
        rect(x,y,path + filename,1)
        right,down = x,y
        drawing = False
        img2 = cv2.imread(path + filename)
        cv2.rectangle(img2, pt1=(ix,iy), pt2=(x, y),color=(0,255,255),thickness=10)
        img = img2

for filename in os.listdir(path):
    img = cv2.imread(path+filename)
    cv2.namedWindow(winname= "PRESS-->      Esc : next Image    e: confirm selection      r: redo selection")
    cv2.setMouseCallback("PRESS-->      Esc : next Image    e: confirm selection      r: redo selection", draw_reactangle_with_drag)
    while True:
        cv2.imshow("PRESS-->      Esc : next Image    e: confirm selection      r: redo selection", img)
        if cv2.waitKey(10) == 27:
            break
    cv2.destroyAllWindows()
df.to_csv(destination,index=False)

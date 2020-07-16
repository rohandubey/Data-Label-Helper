# Label-Data-Helper [![](https://img.shields.io/github/license/sourcerer-io/hall-of-fame.svg)](https://github.com/rohandubey/Facial-Expression-Recognition/blob/master/LICENSE)
<br><br>
A Program that creates a bounding box that enables you to construct a predictable pipeline of high-quality training data that will teach your ML/DL-powered computer vision system to find and identify objects in image and video data.<br><br>
## Prerequisites
You need to have installed following softwares and libraries in your machine before running this project.
1. Python 3
2. Matplotlib
3. OpenCV: Image processing library.
4. Pillow(PIL)
5. Numpy
6. Pandas
## Installation
```
$ pip3 install opencv-contrib-python
```
```
$ pip3 install matplotlib
```
```
$ pip3 install pillow
```
```
$ pip3 install numpy
```
```
$ pip3 install pandas
```
// install these libraries based on your environment.
### What steps you have to follow??
- Download `main.py` file 
- Keep your `image datatset` ready in which we have all the images.
```
$ tree --dirsfirst
├── Image_directory

│	├── File_1.jpg

│	├── File_2.jpg

│	├── File_3.jpg

...	│   ...

...	│   ...

│   	└── File_n.jpg

├── main.py
```
- Execute **main.py** file using argparse commands :- ``python3 main.py --p=Image_directory/ --c=Class_name --d=CSV_file_path/file.csv``
- This will open images one by one.
- After that you have to select the portion of image by the *bounding box* through mouse click `e` to **confirm** selection.
![alt text](https://github.com/rohandubey/Label-Data-Helper/blob/master/p1.png?raw=true)
- To **redo** selection press `r` instead of `e` thus that selection won't be saved.
- A single image can have multiple bounding boxes. Like one below!
![alt text](https://github.com/rohandubey/Label-Data-Helper/blob/master/p2.png?raw=true)
- Press `Escape Key` to go to the **next** Image.
- You can **skip** an image by pressing the same `Escape key`.
- At the end of all iteartions a **".csv"** file will be created containing the following classes = **_image_name, class_name, down, left, right, top.**
- **Down**, **up**, **left** and **right** are the co-ordinates of the **annotated area** of each image with its location and class name tagged with it.

```This is the usual annotation format of major object detection models. For example, PascalVOC, MS COCO, OID, KITTI, Retinanet, Imagenet, etc.```

**This program is using argparse commands**
### Execution Command : 
`python3 main.py --p=Image_directory/ --c=Class_name --d=CSV_file_path/file.csv`
## Authors
Rohan Dubey - Complete work

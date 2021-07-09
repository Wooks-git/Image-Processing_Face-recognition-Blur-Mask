import tkinter as tk
import tkinter.font as font
import numpy as np, cv2
from PIL import Image, ImageTk
import os

path = 'picture/'
path_blur = path + 'blur/'
path_edge = path + 'edge/'
path_mask = path + 'mask/'

try:
    os.mkdir(path_blur)
    os.mkdir(path_edge)
    os.mkdir(path_mask)

except FileExistsError:
    print('dir error')

cnt = 0

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('C:/Users/ShimBoSeok/Desktop/haarcascade_frontalface_default.xml')

face_mask = cv2.imread('ga.PNG')
face_mask = np.array(face_mask, dtype=np.uint8)

click = 0

#window 설정
window = tk.Tk()
window.title('Project')
window.geometry("757x483")
window.resizable(False, False)
window.configure(bg = 'blue')

#video frame 설정
frm = tk.Frame(window, bg = 'white', width = 256, height = 20)
# frm.grid(row = 1, column = 0)
# frm.pack()
frm.place(x=0, y =0)
#video가 삽입 될 label 설정
lbl_video = tk.Label(frm)
lbl_video.grid()

my_font = font.Font(family = 'Helvetica', size = 16, weight = 'bold')
###fliters
#blur filter
def blur_f(image):
    res_frame = image.copy()
    faces = face_detector.detectMultiScale(res_frame, 1.05, 5)

    if len(faces):
        for (x,y,w,h) in faces:
            sub_face = image[y:y+h, x:x+w]

            sub_face = cv2.GaussianBlur(sub_face, (0, 0), 10)

            res_frame[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face

    return res_frame

#edge_filter
def edge_f(image):
    edge = cv2.Canny(image, 80, 150)
    return edge

#mask filter
def mask_f(image):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(image, 1.05, 5)

    try:
        for (x, y, w, h) in faces:
            frame_roi = image[y:y + h+25, x:x + w]  # 얼굴 영역 추출

            face_mask_small = cv2.resize(face_mask, (w, h+25))

            gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)

            ret, mask = cv2.threshold(gray_mask, 40, 255, cv2.THRESH_BINARY)

            mask_inv = cv2.bitwise_not(mask)

            masked_face = cv2.bitwise_and(face_mask_small, face_mask_small, mask=mask)
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)

            image[y:y + h+25, x:x + w] = cv2.add(masked_face, masked_frame)

    except cv2.error:
        print('out of range!!')

    return image
###

#button commands
def original():
    global click
    click = 0

def blur_b():
    global click
    click = 1

def edge_b():
    global  click
    click = 2

def mask_b():
    global click
    click = 3

def pic():
    global click
    click = 4
###

#buttons
btn_original = tk.Button(frm, text = 'Original', font = my_font, width = 8, height = 3, command = original)
btn_original.place(x = 642, y =1)

btn_blur = tk.Button(frm, text = 'Blur', font = my_font, width = 8, height = 3, command = blur_b)
btn_blur.place(x = 642, y = 90)

btn_edge = tk.Button(frm, text = 'Edge', font = my_font, width = 8, height = 3,command = edge_b)
btn_edge.place(x = 642, y = 180)

btn_mask = tk.Button(frm, text = 'Mask', font = my_font, width = 8, height = 3,command = mask_b)
btn_mask.place(x = 642, y = 270)

btn_pic = tk.Button(frm, text = 'Picture', font = my_font, width = 8, height = 5,command = pic)
btn_pic.place(x = 642, y = 360)

btn_empty = tk.Button(frm, font = my_font, width = 8, command = None)
btn_empty.grid(row = 1, column = 1)
###

### image index
i_ga=0
i_edge = 0
i_blur = 0
i_original = 0
###

def play():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if click == 0:
        global img_original

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img_original = Image.fromarray(frame) # numpy -> PIL 이미지로 변환
        imgtk = ImageTk.PhotoImage(image = img_original) #tk 형식으로 이미지 변환

        lbl_video.imgtk = imgtk
        lbl_video.configure(image = imgtk)


    if click == 1:
        global img_blur

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        frame = blur_f(frame)
        img_blur = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img_blur)

        lbl_video.imgtk = imgtk
        lbl_video.configure(image=imgtk)

    if click == 2:
        global img_edge

        frame = edge_f(frame)
        img_edge = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img_edge)

        lbl_video.imgtk = imgtk
        lbl_video.configure(image=imgtk)

    if click == 3:
        global img_ga

        frame = mask_f(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img_ga = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img_ga)

        lbl_video.imgtk = imgtk
        lbl_video.configure(image=imgtk)

    if click == 4:
        global i_ga
        global i_edge
        global i_blur
        global i_original
        try:
            if img_ga:
                img_ga.save(path_mask + f'/mask_img_{i_ga}.png')
                i_ga+=1
                del img_ga

        except NameError:
            print('ga')

        try:
            if img_edge:
                img_edge.save(path_edge+f'/edge_img_{i_edge}.png')
                i_edge+=1
                del img_edge
        except NameError:
            print('edge')

        try:
            if img_blur:
                img_blur.save(path_blur+f'/blur_img_{i_blur}.png')
                i_blur +=1
                del img_blur
        except NameError:
            print('blur')

    lbl_video.after(10, play)

play()
window.mainloop()
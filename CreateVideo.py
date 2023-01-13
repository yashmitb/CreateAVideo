import os
import cv2

images = []
exts = [".jpg", ".png", ".jpeg", ".jfif", ".gif"]

path = "PRO-C105-Student-Boilerplate-main/Images"

for file in os.listdir(path):
    filename, ext = os.path.splitext(file)
    if (ext in exts):
        file_path = path + "/" + file
        images.append(file_path)

print(len(images))

image = cv2.imread(images[0])
height, width, channel = image.shape
size = (width, height)

video = cv2.VideoWriter(
    "freinds1.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
# for i in range(0, len(images)-1):
#     frame = cv2.imread(images[i])
#     video.write(frame)
for i in range(len(images)-1, 0, -1):
    frame = cv2.imread(images[i])
    video.write(frame)
video.release()

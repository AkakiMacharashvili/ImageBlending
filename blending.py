from PIL import Image
import numpy
import cv2
def blend(file1, file2, file3, k):
    img1 = Image.open(file1)
    img2 = Image.open(file2)

    midWidth = int((img1.size[0] + img2.size[0]) / 2)
    midHeight = int((img1.size[1] + img2.size[1]) / 2)

    if img1.size != (midWidth, midHeight):
        img1 = img1.resize((midWidth, midHeight))
    if img2.size != (midWidth, midHeight):
        img2 = img2.resize((midWidth, midHeight))

    matrix1 = numpy.asarray(img1)
    matrix2 = numpy.asarray(img2)

    mat1 = numpy.multiply(matrix1, k)
    mat2 = numpy.multiply(matrix2, 1 - k)

    image = numpy.add(mat1, mat2)
    image = numpy.asarray(image, dtype='uint8')

    out = Image.fromarray(image)

    out.save(f"{file3}/blended_{k}.png")



file1 = input('please enter first image address: ')
file2 = input('please enter second image address: ')
file3 = input('please enter address where program should store video, blended images: ')

for i in range(0, 11):
    k = i / 10
    blend(file1, file2, file3, k)

list = []
for i in range(0, 11):
    k = i / 10
    img = cv2.imread(f"{file3}/blended_{k}.png")
    height, width, layers = img.shape
    size = (width, height)
    t = 0
    for j in range(350000):
        t += 1
    list.append(img)


img1 = Image.open(file1)
img2 = Image.open(file2)
midWidth = int((img1.size[0] + img2.size[0]) / 2)
midHeight = int((img1.size[1] + img2.size[1]) / 2)

out = cv2.VideoWriter(f'{file3}/video.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 15, (midWidth, midHeight))
for i in range(len(list)):
    out.write(list[i])
out.release()


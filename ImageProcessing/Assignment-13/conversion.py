from PIL import Image
img = Image.open('himu.jpg')
img.save("himu1.png")

img = Image.open('himu1.png')
img.save("himu.jpg")
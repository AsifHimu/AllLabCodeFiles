from PIL import Image

img = Image.open('village.jpg')
img.save('village1.png')

img = Image.open('village1.png')
img.save('village1.jpg')
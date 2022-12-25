from PIL import Image
filename = "assets/building.png"
with Image.open(filename) as img:
    img.load()

    img.rotate(45)

    type(img)

    isinstance(img, Image.Image)

    img.show()

    cropped_img = img.crop((300, 150, 700, 1000))
    cropped_img.save("cropped_image.jpg")
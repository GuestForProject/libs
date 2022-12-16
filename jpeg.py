from PIL import Image
filename = "assets/buildings.jpg"
with Image.open(filename) as img:
    img.load()

    img.rotate(90)
    img.show()

    cropped_img = img.crop((150, 150, 700, 700))
    cropped_img.save("assets/cropped_image.jpg")


from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')

#filtered_img = img.filter(ImageFilter.SHARPEN)
#filtered_img = img.filter(ImageFilter.BLUR)     comenzi
#filtered_img = img.filter(ImageFilter.SMOOTH)

filtered_img = img.convert('L') 

print(img)
print(img.format)
print(img.size)
print(img.mode)  #mode = RGB
print(dir(img))

croocked = filtered_img.rotate(90)
filtered_img.save("grey.png", 'png')
croocked.save("grey2.png", 'png')

resized = filtered_img.resize((300, 300))
resized.save("resized.png", "png")

box = (100,100,400,400)
region = filtered_img.crop(box)
region.save("cropped.png", "png")
filtered_img.show()
print(img.size)
new_image = img.resize((400,400))
new_image.save("thumbnail.jpg")

img.thumbnail((400,400))
img.save("thumbnail2.jpg")


from PIL import Image

def image_size (image_path) :
    img = Image.open(image_path)
    return img.size

height , width = image_size('input2.jpg')
print(f'image height {height} and width {width}')
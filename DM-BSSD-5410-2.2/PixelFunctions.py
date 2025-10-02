from PIL import Image, ImageDraw

# Comparison function for sorting based on the red channel
def compare_pixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]  # Compare based on the red channel

# Store pixel data in a list of tuples (RGB, position)
def storePixels(im):
    width, height = im.size
    pixel_array = []

    for i in range(width):
        for j in range(height):
            r, g, b = im.getpixel((i, j))
            pixel_array.append(((r, g, b), (i, j)))

    return pixel_array

# Convert pixels back into an image
def pixels_to_image(im, pixels):
    outimg = Image.new("RGB", im.size)
    outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg

# Apply pixel data back to the image
def pixels_to_points(im, pixels):
    for p in pixels:
        im.putpixel(p[1], p[0])

# Optional grayscale conversion
def grayscale(im, pixels):
    for color, pos in pixels:
        avg = sum(color) // 3
        gray = (avg, avg, avg)
        im.putpixel(pos, gray)

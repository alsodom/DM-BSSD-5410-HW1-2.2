from PixelFunctions import compare_pixels, storePixels, pixels_to_image, pixels_to_points, grayscale
from SearchFunction import binary_search_sub
from SortFunction import quick_sort_iterative  # or selection_sort
from PIL import Image

def main():
    IMG_NAME = 'monkey'

    print("Trying to open image:", IMG_NAME + '.jpg')

    try:
        with Image.open(IMG_NAME + '.jpg') as im:
            print("Image opened successfully")
            pixels = storePixels(im)
            print("stored")

            sorted_pixels = pixels.copy()

            # Use quick sort here
            quick_sort_iterative(sorted_pixels, compare_pixels)
            print("sorted")

            threshold = int(input("Enter the red channel threshold (0-255): "))
            red_values = [r[0][0] for r in sorted_pixels]
            subi = binary_search_sub(red_values, threshold)
            print("sublist of reds starts at:", subi)

            grayscale(im, pixels)
            pixels_to_points(im, sorted_pixels[subi:])

            im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')

    except FileNotFoundError:
        print(f"File '{IMG_NAME}.jpg' not found. Please check the filename and path.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()

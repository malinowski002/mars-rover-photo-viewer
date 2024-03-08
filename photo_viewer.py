import urllib.request
from PIL import Image
import customtkinter
import webbrowser
from api_handler import get_photos


def display_photo(photo_index, photo_urls, label_img, label_current, label_camera, label_earth_date):
    url = photo_urls[photo_index][0].replace("http://mars.jpl.nasa.gov", "https://mars.nasa.gov")
    urllib.request.urlretrieve(url, "photo")
    image = Image.open("photo")

    max_width = 650
    max_height = 650

    if image.width > max_width or image.height > max_height:
        ratio = min(max_width / image.width, max_height / image.height)
    else:
        ratio = max_width / image.width
        if (image.height * ratio) > max_height:
            ratio = max_height / image.height

    width = round(image.width * ratio)
    height = round(image.height * ratio)

    main_image = customtkinter.CTkImage(light_image=Image.open("photo"), size=(width, height))
    label_img.configure(image=main_image)
    label_img.image = main_image

    label_current.configure(text=f"{photo_index}/{len(photo_urls) - 1}")
    label_camera.configure(text=f"Camera used:\n{photo_urls[photo_index][1]}")
    label_earth_date.configure(text=f"Earth date: {photo_urls[photo_index][2]}")


def open_in_browser(photo_urls, current_photo):
    print(photo_urls[current_photo][0])
    webbrowser.open_new(photo_urls[current_photo][0])

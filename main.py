import customtkinter
from photo_viewer import display_photo, open_in_browser
from api_handler import get_photos

global current_photo, photo_urls, label_img, photos_count, label_current, label_camera, label_earth_date, slider, sol


def prev_photo():
    global photos_count, current_photo, label_current
    current_photo = (current_photo - 1) % photos_count
    display_photo(current_photo, photo_urls, label_img, label_current, label_camera, label_earth_date)


def next_photo():
    global photos_count, current_photo, label_current
    current_photo = (current_photo + 1) % photos_count
    display_photo(current_photo, photo_urls, label_img, label_current, label_camera, label_earth_date)


def slider_event(value):
    global current_photo
    current_photo = int(value)
    display_photo(current_photo, photo_urls, label_img, label_current, label_camera, label_earth_date)


def go_to_sol(sol_number):
    global photo_urls, photos_count, current_photo, label_img, label_current, label_camera, label_earth_date, slider, sol
    sol = sol_number
    photos = get_photos("DEMO_KEY", sol_number)
    photo_urls = [(photo["img_src"], photo["camera"]["full_name"], photo["earth_date"]) for photo in photos]
    photos_count = len(photo_urls)
    if photos_count > 0:
        current_photo = 0
        display_photo(current_photo, photo_urls, label_img, label_current, label_camera, label_earth_date)
        slider.configure(to=photos_count - 1)
        slider.set(0)
        label_current.configure(text=f"{current_photo}/{photos_count - 1}")
    return photos


def main():
    global current_photo, photo_urls, label_img, photos_count, label_current, label_camera, label_earth_date, slider, sol
    photos_count = 153
    sol = 711
    customtkinter.set_appearance_mode("dark")
    current_photo = 0

    root = customtkinter.CTk(fg_color="#2A2A2A")
    root.title("NASA's Curiosity Photo Viewer")
    root.geometry("952x670")

    prev_button = customtkinter.CTkButton(
        root,
        text="Previous",
        fg_color="#CB6327",
        hover_color="#A75022",
        width=130,
        corner_radius=0,
        command=prev_photo,
        font=("Helvetica SemiBold", 13),
        height=35,
        anchor="center"
    )
    prev_button.place(x=670, y=20)

    next_button = customtkinter.CTkButton(
        root,
        text="Next",
        fg_color="#CB6327",
        hover_color="#A75022",
        width=130,
        corner_radius=0,
        command=next_photo,
        font=("Helvetica SemiBold", 13),
        height=35,
        anchor="center"
    )
    next_button.place(x=810, y=20)

    label_current = customtkinter.CTkLabel(
        root,
        text=f"{current_photo}/{photos_count - 1}",
        font=("Helvetica", 16)
    )
    label_current.place(x=670, y=70)

    slider = customtkinter.CTkSlider(
        root,
        from_=0,
        to=photos_count,
        width=270,
        button_color="#CB6327",
        button_hover_color="#A75022",
        command=slider_event
    )
    slider.set(0)
    slider.place(x=670, y=100)

    label_sol = customtkinter.CTkLabel(
        root,
        text=f"Martian Sol: ",
        justify="left",
        font=("Helvetica Bold", 18)
    )
    label_sol.place(x=670, y=130)

    sol_entry = customtkinter.CTkEntry(
        root,
        placeholder_text=f"{sol}",
        corner_radius=0,
        font=("Helvetica", 16),
        width=80,
        height=35
    )
    sol_entry.place(x=670, y=180)

    sol_button = customtkinter.CTkButton(
        root,
        text="Go to chosen sol",
        fg_color="#CB6327",
        hover_color="#A75022",
        width=130,
        corner_radius=0,
        command=lambda: go_to_sol(int(sol_entry.get())),
        font=("Helvetica SemiBold", 13),
        height=35,
        anchor="center"
    )
    sol_button.place(x=760, y=180)

    label_camera = customtkinter.CTkLabel(
        root,
        text=f"Camera: ",
        justify="left",
        font=("Helvetica", 16)
    )
    label_camera.place(x=670, y=240)

    label_earth_date = customtkinter.CTkLabel(
        root,
        text=f"Earth Date: ",
        font=("Helvetica", 16)
    )
    label_earth_date.place(x=670, y=290)

    label_img = customtkinter.CTkLabel(root, text="", fg_color="black", bg_color="black")
    label_img.place(x=10, y=10)

    browser_button = customtkinter.CTkButton(
        root,
        text="Show photo in original resolution",
        fg_color="#CB6327",
        hover_color="#A75022",
        width=270,
        corner_radius=0,
        command=lambda: open_in_browser(photo_urls, current_photo),
        font=("Helvetica SemiBold", 13),
        height=35,
        anchor="center"
    )
    browser_button.place(x=670, y=340)

    photos = go_to_sol(sol)
    photo_urls = []
    for photo in photos:
        photo_urls.append((photo["img_src"], photo["camera"]["full_name"], photo["earth_date"]))
        print(photo)
    print(photo_urls)
    photos_count = len(photo_urls)

    display_photo(current_photo, photo_urls, label_img, label_current, label_camera, label_earth_date)

    root.mainloop()


if __name__ == "__main__":
    main()
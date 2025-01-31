# This is the main python script!

from utils.btn import handle_buttons
from inky.auto import auto
from utils.img import get_dir_image, get_unsplash_image, get_file_image
from utils.timer import handle_timer

def load_dir_image():
    print("Loading image from directory...")
    inky = auto(ask_user=True)
    image = get_dir_image()
    inky.set_image(image, saturation=0.6)
    inky.show()

def load_unsplash_image():
    print("Loading image from Unsplash...")
    inky = auto(ask_user=True)
    image = get_unsplash_image()
    inky.set_image(image, saturation=0.6)
    inky.show()

def handle_button(_, btn_info):
    print(f"Button {btn_info[2]} pressed!")
    (index) = btn_info[0]

    if index == 0:
        load_dir_image()

    elif index == 1:
        load_unsplash_image()

print("""
Press button 1 to load a random image from your images directory.
Press button 2 to load a random image from Unsplash.

Press Ctrl+C to exit!
""")

handle_buttons(handle_button)

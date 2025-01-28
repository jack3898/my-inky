#!/usr/bin/env python3

from inky.auto import auto
from utils.img import get_unsplash_image
from utils.btn import handle_btn

def handle_button(_, __):
    inky = auto(ask_user=True)

    image = get_unsplash_image()
    inky.set_image(image, saturation=0.6)
    inky.show()

handle_btn(handle_button)
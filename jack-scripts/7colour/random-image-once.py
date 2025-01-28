#!/usr/bin/env python3

from inky.auto import auto
from utils.img import get_unsplash_image

inky = auto(ask_user=True)

image = get_unsplash_image()

inky.set_image(image, saturation=0.6)
inky.show()

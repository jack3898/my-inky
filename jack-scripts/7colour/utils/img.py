from PIL import Image
from io import BytesIO
import requests

def get_unsplash_image():
    url = "https://picsum.photos/800/480"

    response = requests.get(url)

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        return Image.new("RGB", (800, 480), "white")
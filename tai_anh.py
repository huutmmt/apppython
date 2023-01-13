import urllib.request
import os
from PIL import Image #mở ảnh

url = "https://znews-photo.zingcdn.me/w960/Uploaded/qhj_yvobvhfwbv/2018_07_18/Nguyen_Huy_Binh1.jpg"
subfolder = "images"
filename = os.path.basename(url)
filepath = os.path.join(subfolder, filename)

if not os.path.exists(subfolder):
    os.makedirs(subfolder)

urllib.request.urlretrieve(url, filepath)


with Image.open(filepath) as im:
    im.show()
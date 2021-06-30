import PIL.ImageGrab

img = PIL.ImageGrab.grab()
import base64
aaa=img.tobytes()

print(aaa)
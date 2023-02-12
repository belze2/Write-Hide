from time import sleep
import picturekeys
import pyperclip
data = pyperclip.paste()
decoder = picturekeys.Materials()
print(decoder.decrypt(data))
sleep(35)
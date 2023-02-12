from io import StringIO
from time import sleep
import picturekeys
import pyperclip
import sys

def put():
    print("You can enter your message now! Take your time...")
    textline = input('*')
    buffer.write(textline)
    size = sys.getsizeof(buffer)
    if 0 < size <= 1028: return True
    else: return False

encoder = picturekeys.Materials()
buffer = StringIO()

# write to clipboard
savety = None
if put():
    buffer.seek(0)
    savety = encoder.encrypt(buffer.read())
    pyperclip.copy(savety)
else:
    print('Your message must be 1 and 1028 characters...')

# finsh
buffer.close()
if savety: print('*Your clipboard now contains your ENCRYPTED MESSAGE. bye')

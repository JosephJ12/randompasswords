#__main__.py for randompasswords

from randompasswords.passwordgenerator import *
from faker import Faker
from InputFrame import *
import wx

def main():

    #fake = Faker()
    app = wx.App()
    frame = InputFrame()
    app.MainLoop()
"""
    with open("randompasswords.txt", "w+") as fh:    # open or create a textfile to store inputted keywords
        inputKeywords(fh)
        fh.write(fake.email() + "\n")
        fh.write(fake.address() + "\n")
        fh.write(str(fake.longitude()) + "\n")
        fh.write(str(fake.latitude()) + "\n")

    with open("randompasswords.txt", "r+") as fh:    # takes keywords and puts them in data structures to prepare for generating pws
        storage = storeKeywords(fh)

    passwords = generatePasswords(storage)
    print("\nPrinting passwords now\n\n")

    with open("randompasswords.txt", "a") as fh:
        storePasswords(fh, passwords)
"""

if __name__ == "__main__":
    main()

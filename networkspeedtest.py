from tkinter import *
from speedtest import Speedtest


def test():
    s = Speedtest()
    download = s.download()
    upload = s.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    download_label.config(text="Download speed: \n-" +
                          str(download_speed) + "MBPs")
    upload_label.config(text="Upload speed: \n-" + str(upload_speed) + "MBPs")


root = Tk()
root.title("Speed Test")
root.geometry("300x400")

button = Button(root, text="Tap to know your internet speed",
                command=test, font=("Arial", 24))
button.pack(side=BOTTOM, pady=40)

download_label = Label(root, text="Download speed: \n-", font=("Arial", 24))
download_label.pack(pady=50)

upload_label = Label(root, text="Upload speed: \n", font=("Arial", 24))
upload_label.pack(pady=(10, 0))

root.mainloop()

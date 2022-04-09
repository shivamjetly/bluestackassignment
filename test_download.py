from tkinter import *
import requests


# Defining  Downloder Class
class Downloader:
    # Defining Constructor
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("Downloader Application")
        # Window Geometry
        self.root.geometry("700x200+300+300")
        # Declaring Url Variable
        self.url = StringVar()
        # Declaring Status Variable
        self.status = StringVar()
        # Initialising Status Variable
        self.status.set('--------')
        # Creating Frame for downloader
        download_frame = Frame(self.root, background="red", width=700, height=200).place(x=0, y=0)
        # Adding text widget lable for url
        Label(download_frame, text="URL", compound=LEFT, font=("Calibri", 15, "bold"), bg="white", fg="black").grid(
            row=1, column=0, padx=10, pady=10)
        # Adding text widget for url
        Entry(download_frame, bd=2, width=25, textvariable=self.url, relief=RIDGE, font=("Calibri", 15)).grid(row=1,
                                                                                                               column=1,
                                                                                                               padx=10,
                                                                                                               pady=10)
        # Adding the Download button
        Button(download_frame, text="Download", activebackground='brown', activeforeground='yellow', command=self.download, width=10, font=("Calibri", 14, "bold"),
               bg="white", fg="navyblue").grid(row=1, column=2, padx=10, pady=10)
        # Adding the Status Label
        Label(download_frame, textvariable=self.status, font=("Calibri", 14, "bold"), bg="grey", fg="white").grid(row=2,
                                                                                                                  column=1)

    # Defining Download Function
    def download(self):
        # Cheaking if URL Entry is not Null
        if self.url.get() == "":
            self.status.set("Please enter valid URL")
        else:
            try:
                # Updating Status
                self.status.set("Downloading in progress...")
                self.root.update()
                # Getting the response of request
                Request = requests.get(self.url.get())
                # Checking if status code is not bad
                if Request.status_code == requests.codes.ok:
                    # Opening File to write bytes
                    with open("download", mode='wb') as file:
                        file.write(Request.content)
                    # Updating Status
                    self.status.set("Successfully Downloaded")
                else:
                    self.status.set(Request.status_code)
            except:
                self.status.set("Error in Downloading")


# Creating TK Container
r = Tk()
# Passing Root to Downloader Class
Downloader(r)
# Root Window Looping
r.mainloop()

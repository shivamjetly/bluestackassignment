from tkinter import *
import requests


class Downloader():
  def _init_(self,root):
    self.root = root
    self.root.title("Downloader Application")
    self.root.geometry("600x100+200+200")
    self.url = StringVar()
    # Declaring Status Variable
    self.status = StringVar()
    self.status.set("--/--")

    download_frame = Frame(self.root,background="blue",width=600,height=100).place(x=0,y=0)
    url_lbl = Label(download_frame,text="URL",compound=LEFT,font=("times new roman",15,"bold"),bg="whitw",fg="orange").grid(row=1,column=0,padx=10,pady=10)
    url_txt = Entry(download_frame,bd=2,width=25,textvariable=self.url,relief=SUNKEN,font=("times new roman",15)).grid(row=1,column=1,padx=10,pady=10)
    # Adding the Download button
    dwn_btn = Button(download_frame,text="Download",command=self.download,width=10,font=("times new roman",14,"bold"),bg="gold",fg="navyblue").grid(row=1,column=2,padx=10,pady=10)
    # Adding the Status Label
    status_lbl = Label(download_frame,textvariable=self.status,font=("times new roman",14,"bold"),bg="grey",fg="white").grid(row=2,column=1)

  # Defining Download Function
  def download(self):
    # Cheaking if URL Entry is not Null
    if self.url.get()=="":
      self.status.set("URL NOT SPECIFIED")
    else:
      try:
        # Updating Status
        self.status.set("Downloading...")
        self.root.update()
        # Getting the response of request
        Request = requests.get(self.url.get())
        # Cheaking if status code is not bad
        if Request.status_code == requests.codes.ok:
          # Opening File to write bytes
          file = open("download","wb")
          file.write(Request.content)
          file.close()
          # Updating Status
          self.status.set("Download Completed")
        else:
          self.status.set(Request.status_code)

      except:
        self.status.set("Error in Downloading")

# Creating TK Container
root = Tk()
# Passing Root to Downloader Class
Downloader()
# Root Window Looping
root.mainloop()

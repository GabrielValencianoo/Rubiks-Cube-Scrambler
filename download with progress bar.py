import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
import threading
import urllib
class DownloadApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.var = tk.StringVar()
        self.url_entry = ttk.Entry(self)
        self.url_entry.pack()
        self.filename_entry = ttk.Entry(self)
        self.filename_entry.pack()
        self.progress = ttk.Progressbar(self, length=200)
        self.progress.pack()
        self.Labelprogress = ttk.Label(self, textvariable=self.var)
        self.Labelprogress.pack()
        self.download_button = ttk.Button(self, text="Download", command=self.start_download)
        self.download_button.pack()

    def download_file(self, url, filename):
        response = urllib.request.urlopen(url)
        total = int(response.info().get('Content-Length', 0))
        self.progress['maximum'] = total
        downloaded = 0
        with open(filename, 'wb') as f:
            while True:
                data = response.read(1024)
                downloaded += len(data)
                f.write(data)
                self.progress['value'] = downloaded
                self.var.set(downloaded)
                self.update_idletasks()
                if not data:
                    break

    def start_download(self):
        url = self.url_entry.get()
        filename = self.filename_entry.get()
        threading.Thread(target=self.download_file, args=(url, filename)).start()

app = DownloadApp()
app.mainloop()

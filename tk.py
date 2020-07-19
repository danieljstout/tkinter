import tkinter as tk
import speedtest
import asyncio

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.create_data()

    def create_data(self):
        self.my_number = 0

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.reset = None

        self.start_test = tk.Button(self)
        self.start_test["text"] = "start speed test"
        self.start_test["command"] = self.speed_test
        self.start_test.pack(side = "bottom")
        self.download_result = tk.Label(self)
        self.download_result.pack(side = "bottom")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def number_words(self, num):
        if num == 1:
            return "once"
        elif num == 0:
            return None
        else:
            return f"{num} times"

    def say_hi(self):
        self.my_number += 1
        self.hi_there["text"] = f"You just got clicked {self.number_words(self.my_number)}!"

        if not self.reset:
            self.reset = tk.Button(self)
            self.reset["text"] = "click to reset"
            self.reset["command"] = self.reset_number
            self.reset.pack(side="right")
    
    def reset_number(self):
        self.my_number = 0
        self.hi_there["text"] = "Hello World\n(click me)"
        self.reset.destroy()
        self.reset = None

    
    def speed_test(self):
        servers = []
        threads = 1

        s = speedtest.Speedtest()
        print("hello")
        s.get_servers(servers)
        s.get_best_server()
        s.download(threads=threads)
        s.upload(threads=threads)
        s.results.share()

        results_dict = s.results.dict()
        download_simple = f"{results_dict['download'] / 1_000_000}MBps"

        self.download_result["text"] = download_simple

        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
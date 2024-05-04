
import tkinter as tk

class CounterApp:
    def __init__(self, master):
        self.master = master
        self.counter = 0
        
        self.label = tk.Label(master, text="Counter: 0")
        self.label.pack()
        
        self.button = tk.Button(master, text="Click Me!", command=self.increment_counter)
        self.button.pack()
    
    def increment_counter(self):
        self.counter += 1
        self.label.config(text=f"Counter: {self.counter}")

def main():
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

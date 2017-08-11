import Tkinter as tk

counter = 0
def counter_num(num):
    def count():
        global counter
        counter += 1
        num.config(text=str(counter))
        num.after(1000,count)
    count()

root = tk.Tk()
root.title("Counting Seconds")
num = tk.Label(root, fg="dark green")
num.pack()
counter_num(num)
button = tk.Button(root, text='Stop',width=25, command=root.destroy)
button.pack()
root.mainloop()

from tkinter import *
import tkinter
# from tkinter import ttk
from PIL import Image, ImageTk
global label_result

window1 = Tk()
window1.title("MATHEMATICIAN MASON")
window1.geometry('600x500+200+250')

frame = Frame(window1)
frame.pack(side=TOP)

b1 = tkinter.Button(window1, text="Exit", command=window1.destroy)
b1.pack(side=BOTTOM)
image = Image.open('../virtualbrickwallproject/BRICK WALL SIMULATION.png')
photo = ImageTk.PhotoImage(image)
label = tkinter.Label(window1, image=photo)
label.pack()


def open2():
    window1.withdraw()
    root = tkinter.Tk()
    root.title("Brick Wall")
    # root.config(background="blue")
    root.geometry("500x500")

    label1 = tkinter.Label(root, text="Width of wall:")
    label1.grid(row=0, column=0)
    label1.config(font=("Courier", 15))

    entry1 = tkinter.Entry(root)
    entry1.grid(row=0, column=1)

    label2 = tkinter.Label(root, text="Height of wall:")
    label2.grid(row=1, column=0)
    label2.config(font=("Courier", 15))

    entry2 = tkinter.Entry(root)
    entry2.grid(row=1, column=1)

    label3 = tkinter.Label(root, text="Number of type 3 bricks:")
    label3.grid(row=2, column=0)
    label3.config(font=("Courier", 15))

    entry3 = tkinter.Entry(root)
    entry3.grid(row=2, column=1)

    label4 = tkinter.Label(root, text="Number of type 2 bricks:")
    label4.grid(row=3, column=0)
    label4.config(font=("Courier", 15))

    entry4 = tkinter.Entry(root)
    entry4.grid(row=3, column=1)

    label5 = tkinter.Label(root, text="Number of type 1 bricks:")
    label5.grid(row=4, column=0)
    label5.config(font=("Courier", 15))

    entry5 = tkinter.Entry(root)
    entry5.grid(row=4, column=1)

    label_type3 = tkinter.Label(root)
    label_type3.grid(row=6, column=0)

    label_type2 = tkinter.Label(root)
    label_type2.grid(row=7, column=0)

    label_type1 = tkinter.Label(root)
    label_type1.grid(row=8, column=0)

    label_wall = tkinter.Label(root, text="")
    label_wall.grid(row=6, column=1, rowspan=3)

    global label_result
    label_result = tkinter.Label(root, fg="red")
    label_result.grid(row=9, column=1)

    button = tkinter.Button(root, bg="green", fg="white", text="Build wall", command=lambda: open3(int(entry1.get()),
                                                                                                   int(entry2.get()),
                                                                                                   int(entry3.get()),
                                                                                                   int(entry4.get()),
                                                                                                   int(entry5.get())))
    button.grid(row=5, column=1)
    button.configure(width=15, height=2)


def open3(N1, N2, N3, N4, N5):
    total_area = N1 * N2
    if N3 * 3 + N4 * 2 + N5 * 1 < total_area:
        label_result.config(text="CANNOT BE DONE")
    else:
        wall = []
        for i in range(N2):
            row = ""
            width = 0
            while width < N1:
                if N3 > 0 and width + 3 <= N1:
                    row += "▦▦▦"
                    N3 -= 1
                    width += 3
                elif N4 > 0 and width + 2 <= N1:
                    row += "▧▧"
                    N4 -= 1
                    width += 2
                elif N5 > 0 and width + 1 <= N1:
                    row += "▩"
                    N5 -= 1
                    width += 1
            wall.append(row)

        # create a new window for displaying the wall

        wall_window = Tk()
        wall_window.title("Brick Wall")
        wall_window.geometry("600x500")
        wall_window.config(background='white')

        # create labels for displaying the types of bricks used
        label_type3 = tkinter.Label(wall_window, text="Type 3 brick " + "▦▦▦", bg="white", font=(15))
        label_type3.pack()
        label_type2 = tkinter.Label(wall_window, text="Type 2 brick " + "▧▧", bg="white", font=(15))
        label_type2.pack()
        label_type1 = tkinter.Label(wall_window, text="Type 1 brick " + "▩", bg="white", font=(15))
        label_type1.pack()

        # create a label for displaying the wall
        label_wall = tkinter.Label(wall_window, text="\n".join(wall), bg="white", fg="brown", width=60, height=60)
        label_wall.pack()

        # update the result label in the main window
        label_result.config(text="Wall built successfully!")


b2 = tkinter.Button(frame, text="Enter", command=open2)
b2.grid(row=1, column=0, pady=10)


window1.mainloop()

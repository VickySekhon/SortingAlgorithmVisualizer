from tkinter import * 
from tkinter import ttk 

import random 

from colors import *

# import all sorting algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort
from algorithms.insertionSort import insertion_sort
from algorithms.shellSort import shell_sort
from algorithms.selectionSort import selection_sort
from algorithms.quickSort import quick_sort

window = Tk()

# window title 
window.title("Sorting Algorithm Visualizer By: Vicky Sekhon")

# maximum size of window 
window.maxsize(1920,1130)

# background color
window.config(background=BLACK)

# colors used for data elements
COLORS = [RED, BLUE, LIGHT_GREEN, YELLOW, DARK_BLUE, WHITE, PINK, PURPLE]

# algorithms available 
algorithm_name = StringVar()
algorithm_list = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort', 'Shell Sort']

# list of speeds to sort data at
speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

# array to store data within 
data = []

# display array 
def draw_array(data, colorArray):
     canvas.delete("all")
     canvas_width = 1900
     canvas_height = 1000
     x_width = canvas_width / (len(data) + 1)
     offset = 4 
     spacing = 2 
     normalizedData = [i / max(data) for i in data]
     
     for i, height in enumerate(normalizedData):
          x0 = i * x_width + offset + spacing 
          y0 = canvas_height - height * 890
          x1 = (i+1) * x_width + offset 
          y1 = canvas_height 
          canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
     
     window.update_idletasks()

# generate random values for the array 
def generate():
     global data
     data = []
     for i in range(0, 300):
          data.append(random.randint(100,500))
          
     draw_array(data, [COLORS[random.randint(0,7)] for x in range(len(data))])
     
# sorting speed 
def sort_speed():
     if speed_menu.get() == 'Slow':
          return 0.3 
     elif speed_menu.get() == 'Medium':
          return 0.1 
     else: 
          return 0.001

# sort using desired algorithm 
def sort():
     global data
     timeTick = sort_speed()
     
     if algorithm_menu.get() == 'Bubble Sort':
          bubble_sort(data, draw_array, timeTick)
     elif algorithm_menu.get() == 'Merge Sort':
          merge_sort(data, 0, len(data) - 1, draw_array, timeTick)
     elif algorithm_menu.get() == 'Insertion Sort':
          insertion_sort(data, draw_array, timeTick)
     elif algorithm_menu.get() == 'Shell Sort':
          shell_sort(data, draw_array, timeTick)
     elif algorithm_menu.get() == 'Selection Sort':
          selection_sort(data, draw_array, timeTick)
     elif algorithm_menu.get() == 'Quick Sort':
          quick_sort(data, 0, len(data) - 1, draw_array, timeTick)
                  
# user interactable elements
UI_frame = Frame(window, width = 900, height = 300, background=BLACK) 
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# styling for the combobox to match the black theme
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= BLACK, background= WHITE, foreground = WHITE)

# title 
l0 = Label(UI_frame, text="Sorting Algorithm By Vicky Sekhon", font=100, background=BLACK, foreground=WHITE)
l0.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky=W)   

# algorithm list 
l1 = Label(UI_frame, text="Algorithm: ", background=BLACK, foreground=WHITE)
l1.grid(row=1, column=0, padx=10, pady=5, sticky=W)    
algorithm_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algorithm_list)
algorithm_menu.grid(row=1, column=1, padx=5, pady=5)
algorithm_menu.current(0)

# speed list
l2 = Label(UI_frame, text="Sorting Speed: ", background=BLACK, foreground=WHITE)
l2.grid(row=2, column=0, padx=10, pady=5, sticky=W)    
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=2, column=1, padx=5, pady=5)
speed_menu.current(0)

# sorting button 
b1 = Button(UI_frame, text="Sort", command=sort, background=WHITE)
b1.grid(row=3, column=1, padx=5, pady=5)

# array generator button 
b3 = Button(UI_frame, text="Generate Array", command=generate, background=WHITE)
b3.grid(row=3, column=0, padx=5, pady=5)  

# canvas 
canvas = Canvas(window, width=2000, height=1000, background=BLACK, highlightthickness=0)
canvas.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

window.mainloop()

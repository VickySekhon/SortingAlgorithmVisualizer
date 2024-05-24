import random
from tkinter import *
from tkinter import ttk

# import sorting algorithms
from algorithms.bubbleSort import bubble_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.selectionSort import selection_sort
from algorithms.shellSort import shell_sort

# import colors to use throughout the project
from colors import *

window = Tk()

window.title("Sorting Algorithm Visualizer By: Vicky Sekhon")

CANVAS_WIDTH = 1900

CANVAS_HEIGHT = 700

OFFSET = 4

SPACING = 2

window.maxsize(1920, 1130)

window.config(background=BLACK) # set background color 

COLORS = [RED, BLUE, LIGHT_GREEN, YELLOW, DARK_BLUE, WHITE, PINK, PURPLE]

algorithm_name = StringVar()
# define algorithms
algorithm_list = [ 
    "Bubble Sort",
    "Insertion Sort",
    "Merge Sort",
    "Quick Sort",
    "Selection Sort",
    "Shell Sort",
] 

speed_name = StringVar()
speed_list = ["Fast", "Medium", "Slow"] # define sorting speeds

data = [] # array to store data 

def draw_single_data_element(element, height, x_width, colorArray):
    
    # starting x coordinate 
    x0 = element * x_width + OFFSET + SPACING
    
    # starting y coordinate
    y0 = CANVAS_HEIGHT - height * 890
    
    # ending x coordinate 
    x1 = (element + 1) * x_width + OFFSET
    
    # ending y coordinate 
    y1 = CANVAS_HEIGHT
    
    # draw rectangle using starting and ending x,y coordinates 
    canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[element])
    

# display array
def draw_array(data, colorArray):
    
    # clear canvas
    canvas.delete("all")
    
    # width to ensure data elements are included on the canvas
    x_width = CANVAS_WIDTH / (len(data) + 1)
    
    # create sizing relative to the largest data element 
    relativelySizedData = [i / max(data) for i in data]

    for i, height in enumerate(relativelySizedData):
        draw_single_data_element(i, height, x_width, colorArray)
        
    window.update_idletasks()


# generate random values for the array
def generate():
    global data
    data = []
    
    # get no. of data elements to generate 
    number_of_elements = data_elements.get()
    
    # get max magnitude of data elements to generate
    magnitude = max_magnitude.get()
    
    # check if no. of data elements entered is valid
    if number_of_elements.isalpha() or magnitude.isalpha():
        print("Invalid input")
        return
    else:
        number_of_elements = int(number_of_elements)
        magnitude = int(magnitude)
        
    # add data elements to array to sort
    for i in range(0, number_of_elements):
        data.append(random.randint(0, magnitude))

    # draw the array onto the screen
    draw_array(data, [COLORS[random.randint(0, 7)] for x in range(len(data))])


# sorting speed
def sort_speed():
    if speed_menu.get() == "Slow":
        return 0.3
    elif speed_menu.get() == "Medium":
        return 0.1
    else:
        return 0.001

# sort using desired algorithm
def sort():
    global data
    timeTick = sort_speed()

    if algorithm_menu.get() == "Bubble Sort":
        bubble_sort(data, draw_array, timeTick)
    elif algorithm_menu.get() == "Merge Sort":
        merge_sort(data, 0, len(data) - 1, draw_array, timeTick)
    elif algorithm_menu.get() == "Insertion Sort":
        insertion_sort(data, draw_array, timeTick)
    elif algorithm_menu.get() == "Shell Sort":
        shell_sort(data, draw_array, timeTick)
    elif algorithm_menu.get() == "Selection Sort":
        selection_sort(data, draw_array, timeTick)
    elif algorithm_menu.get() == "Quick Sort":
        quick_sort(data, 0, len(data) - 1, draw_array, timeTick)


# user interactable elements
UI_frame = Frame(window, width=900, height=300, background=BLACK)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# styling for the combobox to match the black theme
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground=BLACK, background=WHITE, foreground=WHITE)

# title
l0 = Label(
    UI_frame,
    text="Sorting Algorithm By Vicky Sekhon",
    font=100,
    background=BLACK,
    foreground=WHITE,
)
l0.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky=W)

# algorithm list
l1 = Label(UI_frame, text="Algorithm: ", background=BLACK, foreground=WHITE)
l1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
algorithm_menu = ttk.Combobox(
    UI_frame, textvariable=algorithm_name, values=algorithm_list
)
algorithm_menu.grid(row=1, column=1, padx=5, pady=5)
algorithm_menu.current(0)

# speed list
l2 = Label(UI_frame, text="Sorting Speed: ", background=BLACK, foreground=WHITE)
l2.grid(row=2, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=2, column=1, padx=5, pady=5)
speed_menu.current(0)

# no. of data elements input box
l3 = Label(UI_frame, text="Data Elements: ", background=BLACK, foreground=WHITE)
l3.grid(row=3, column=0, padx=10, pady=5, sticky=W)
data_elements = ttk.Entry(UI_frame)
data_elements.grid(row=3, column=1, padx=5, pady=5)

# max magnitude of data elements input box
l4 = Label(UI_frame, text="Max Magnitude: ", background=BLACK, foreground=WHITE)
l4.grid(row=4, column=0, padx=10, pady=5, sticky=W)
max_magnitude = ttk.Entry(UI_frame)
max_magnitude.grid(row=4, column=1, padx=5, pady=5)

# sorting button
b1 = Button(UI_frame, text="Sort", command=sort, background=WHITE)
b1.grid(row=5, column=1, padx=5, pady=5)

# array generator button
b3 = Button(UI_frame, text="Generate Array", command=generate, background=WHITE)
b3.grid(row=5, column=0, padx=5, pady=5)

# canvas
canvas = Canvas(window, width=2000, height=1000, background=BLACK, highlightthickness=0)
canvas.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

window.mainloop()
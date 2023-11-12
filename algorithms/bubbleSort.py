import time 
from colors import *
def bubble_sort(arr, draw_array, timeTick):
     """Sorts a List Using the Bubble Sort Algorithm 
     
     Description:
          Sorts the list by comparing adjacent elements, 
          largest elements simply "bubble" up at the end 
          of the array with each iteration.
     Args:
         arr (int): Array containing more than one element 
     """
     for i in range(len(arr)):
          for j in range(i + 1, len(arr)):
               ele1 = arr[i]
               ele2 = arr[j]
               if (ele1 > ele2):
                    arr[i] = ele2 
                    arr[j] = ele1
                    draw_array(arr, [YELLOW if x == i else DARK_BLUE if x == j else BLUE for x in range(len(arr))])
                    time.sleep(timeTick)
     
     draw_array(arr, [BLUE for x in range(len(arr))])
     
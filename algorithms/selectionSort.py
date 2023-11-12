import time 
from colors import * 
def selection_sort(arr, draw_array, timeTick):
     """Sorts a List Using the Selection Sort Algorithm.
     
     Description:
          Sorts the list by using a minimum value pointer.
          Compares subsequent values with the minimum value
          and swaps the positions of the leftmost value with 
          the minimum value with each iteration.
     Args:
         arr (int): Array containing more than one element.
     """
     for i in range(len(arr)):
          minIndx = i  
          for j in range(i+1, len(arr)):
               if arr[j] < arr[minIndx]:
                    minIndx = j
                    draw_array(arr, [YELLOW if x == j else  BLUE for x in range(len(arr))])
          arr[minIndx], arr[i] = arr[i], arr[minIndx]
          draw_array(arr, [RED if x == minIndx 
                    else PURPLE if x == i else BLUE for x in range(len(arr))])
          time.sleep(timeTick)

     draw_array(arr, [BLUE for x in range(len(arr))])
     
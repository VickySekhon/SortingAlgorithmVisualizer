import time 
from colors import *
def insertion_sort(arr, draw_array, timeTick):
     """Sorts a List Using the Insertion Sort Algorithm 
     
     Description:
          Sorts the list by comparing the current element 
          to the elements behind it. If the value of the 
          current element is less than the element before 
          it, the values are swapped. This is repeated until 
          the front of the array is reached.
     Args:
         arr (int): Array containing more than one element 
     """
     for i in range(1, len(arr)):
          curr = arr[i]
          indx = i - 1 
          comp = arr[indx]
          while (curr < comp and indx >= 0):
               arr[indx+1] = comp
               arr[indx] = curr
               indx -= 1
               comp = arr[indx]
               draw_array(arr, [YELLOW if x == arr.index(curr) else PURPLE if x == arr.index(comp) else BLUE for x in range(len(arr))])
               time.sleep(timeTick)

     draw_array(arr, [BLUE for x in range(len(arr))]) 
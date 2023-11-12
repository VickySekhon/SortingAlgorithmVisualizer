import time 
import math 
from colors import * 
def shell_sort(arr, draw_array, timeTick):
     """Sorts a List Using the Shell Sort Algorithm.
     
     Description:
          Sorts the list by comparing elements "gap" spaces
          away. The gap is calculated as the length of the 
          array divided by 2. Elements before the gap and 
          elements after the gap are compared and switched 
          accordingly. The gap slowly approaches 0 as it is 
          divided by 2 every iteration. 
     Args:
         arr (int): Array containing more than one element. 
     """
     gap = math.floor(len(arr) / 2)
     while gap > 0:
          for i in range(gap, len(arr)):
               curr = arr[i]
               j = i  
               while j >= gap and arr[j-gap] > curr:
                    arr[j] = arr[j-gap]
                    j -= gap
               draw_array(arr, [YELLOW if x == j else PURPLE if x == j-gap
                         else RED if x == i else BLUE for x in range(len(arr))])
               time.sleep(timeTick)     
               arr[j] = curr 
          gap = math.floor(gap/2) 
     
     draw_array(arr, [BLUE for x in range(len(arr))])
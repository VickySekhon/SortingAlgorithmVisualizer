import time 
from colors import *
def merge_sort(arr, lBound, uBound, draw_array, timeTick):
     """Sorts a List Using the Merge Sort Algorithm.
     
     Description:
          Sorts the list by breaking it in half until a single 
          element is recursively found.
     Args:
         arr (int): Array containing more than one element.
         lBound (int): The beginning index of the array to sort.  
         uBound (int): The ending index of the array to sort.
     """
     if lBound < uBound: 
          mid = (lBound + uBound) // 2
          merge_sort(arr, lBound, mid, draw_array, timeTick)
          merge_sort(arr, mid+1, uBound, draw_array, timeTick)   
          merge(arr, mid+1, draw_array, timeTick)
          
          draw_array(arr, [PURPLE if x >= lBound and x < mid else YELLOW if x == mid 
                    else DARK_BLUE if x  > mid and x <= uBound else BLUE for x in range(len(arr))])
     
          time.sleep(timeTick)
          
     draw_array(arr, [BLUE for x in range(len(arr))])
     
def merge(arr, mid, draw_array, timeTick):
     """Backbone of the Merge Sort Algorithm.
     
     Description:
          External function for the Merge Sort Algorithm,
          compares subarrays and sort each subarray appropriately.
     Args:
         arr (int): Array containing more than one element.
         mid (int): The middle index of the array to sort.  
     """
     left = arr[:mid]
     right = arr[mid:]
     i = j = k = 0 
     while (i < len(left) and j < len(right)):
          if (left[i] < right[j]):
               arr[k] = left[i]
               i += 1 
               k += 1 
          else:
               arr[k] = right[j]
               j += 1
               k += 1
     while (i < len(left)):
          arr[k] = left[i]
          i += 1 
          k += 1 
     while (j < len(right)):
          arr[k] = right[j]
          j += 1 
          k += 1 
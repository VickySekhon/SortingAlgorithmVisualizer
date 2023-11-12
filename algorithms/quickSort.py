import time 
from colors import * 
def quick_sort(arr, lBound, uBound, draw_array, timeTick):
     """Sorts a List Using the Quick Sort Algorithm.
     
     Description:
          Sorts the list by selecting a "pivot" element at 
          which elements less than the "pivot" are placed 
          before the "pivot" and elements greater then the 
          "pivot" are placed after the "pivot". The partition
          function is then called.
     Args:
         arr (int):    Array containing more than one element.
         lBound (int): An index to begin sorting at.
         uBound (int): An index to finish sorting at.
     """
     if lBound < uBound:
          end = partition(arr, lBound, uBound, draw_array, timeTick)
          quick_sort(arr, lBound, end - 1, draw_array, timeTick)
          quick_sort(arr, end + 1, uBound, draw_array, timeTick)
          draw_array(arr, [YELLOW if x == lBound else DARK_BLUE if x <= lBound else PURPLE if 
                    x == uBound else BLUE for x in range(len(arr))])
          time.sleep(timeTick)
     draw_array(arr, [BLUE for x in range(len(arr))])

def partition(arr, lBound, uBound, draw_array, timeTick):
     """Backbone of the Quick Sort Algorithm.
     
     Description:
          Uses two pointers, start and end, to compare to the 
          pivot element. The start pointer iterates until a 
          pointer greater than the pivot is encountered and the 
          end pointer iterates until a pointer less than the pivot 
          is encountered. The start and end pointers are then 
          swapped. When the start index is surpasses the the end
          index, the end pointer is swapped with the pivot.
     Args:
         arr (int):    Array containing more than one element.
         lBound (int): An index to begin sorting at.
         uBound (int): An index to finish sorting at.
     """
     pivot = arr[lBound]
     start = lBound
     end = uBound
     while start < end:
          while start < end and arr[start] <= pivot:
               start += 1
          while arr[end] > pivot:
               end -= 1
          if start < end:
               arr[start], arr[end] = arr[end], arr[start]
     temp2 = arr[end]
     arr[end] = pivot
     arr[lBound] = temp2
     return end
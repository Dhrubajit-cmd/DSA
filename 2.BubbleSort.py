# In this we shall learn about the Bubble Sort Algorithm : 

def bubble_sort() : 
   list = [12,3,46,76,889,645,8,98,240,120]
   sorted_list = list[:]

   for i in range(0,len(sorted_list)):
      # Checks if swapping is done or not 
      swapped = False 

    # Main code : 
      for j in range(0,len(sorted_list)-i-1):
          if sorted_list[j] > sorted_list[j+1] :
             sorted_list[j] , sorted_list[j+1] = sorted_list[j+1] , sorted_list[j]
             swapped = True 

      if not swapped :
            break 
          
   return sorted_list 
   
print(bubble_sort())
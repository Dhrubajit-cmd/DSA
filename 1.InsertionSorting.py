# This is called insertion sorting : 
list = []
while True :
    value = int(input("Enter the value : \n"))
    list.append(value)
    end = input("Is this it ? : \n")
    if end == "Yes" or end == "yes" :
        break
    else :
        continue
sorted_list = list[:]

for i in range(1,len(sorted_list)) :
    key = sorted_list[i]
    j = i - 1

    while j >= 0 and key < sorted_list[j] :
        sorted_list[j+1] = sorted_list[j]
        j = j - 1

    sorted_list[j+1] = key
print(f"List entered by you is : {list}. \n")
print(f"Sorted list is : {sorted_list}. \n")



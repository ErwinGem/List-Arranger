def ascend(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] >= list[j]: #if the variable is greater than the next variable, this activate
                list[i], list[j] = list[j], list[i] #switch positions
def descend(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] <= list[j]: #if the variable is lesser than the next variable, this activate
                list[i], list[j] = list[j], list[i] #switch positions

list = []
n = int(input("Enter the number for elements required for the list: "))

for i in range(0, n):
    ele = int(input("Enter the content of your list: "))
    list.append(ele)
print("Original List: ", list)

ascend(list)
print("Ascending Form: ", list)
descend(list)
print("Descending Form: ", list)
print("Thanks for using this program!\n")
input("Press any key to end program.")

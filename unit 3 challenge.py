# Linear Search in Python


def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
print("-----Program for printing student name with marks using list-----")
  
# create an empty dictionary
D = {}
  
n = int(input('How many student record you want to store?? '))
  
# create an empty list
# Add student information to the list
ls = []
  
for i in range(0, n):
    
      # Take combined input name and 
    # percentage and split values 
    # using split function.
    x,y = input("Enter the student name and it's percentage: ").split()
      
    # Add name and marks stored in x, y
    # respectively using tuple to the list
    ls.append((y,x))
      
# sort the elements of list
# based on marks
ls = sorted(ls, reverse = True)
  
print('Sorted list of students according to their marks in descending order')
  
for i in ls:
    
    # print name and marks stored in 
    # second and first position 
    # respectively in list of tuples.
    print(i[1], i[0])
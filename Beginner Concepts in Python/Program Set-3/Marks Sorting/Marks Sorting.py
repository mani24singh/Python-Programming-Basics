# PROGRAM TO SORT THE MARKS OF THE STUDENTS GIVEN BY USER INPUT

# Input Function for the user and Converting the string into integer :
M1 = int(input('Enter The Marks Obtained by Student Number 1 : '))  
M2 = int(input('Enter The Marks Obtained by Student Number 2 : '))
M3 = int(input('Enter The Marks Obtained by Student Number 3 : '))
M4 = int(input('Enter The Marks Obtained by Student Number 4 : '))
M5 = int(input('Enter The Marks Obtained by Student Number 5 : '))
M6 = int(input('Enter The Marks Obtained by Student Number 6 : '))

Mark_List = [M1,M2,M3,M4,M5,M6] # Putting marks into an list
Mark_List.sort()   # Sorting the List
print(Mark_List)   # Print the list





# PROGRAM TO CHECK WHETHER THE GIVEN NAME IS PRESENT IN THE ATTENDANCE LIST

# creating a name-list
name_list = ['ram', 'ruchi', 'karan', 'raj', 'preeti', 'sonam', 'kriti', 'aishwarya']

# input fucntion
n = input('Please enter the name to check from the list : ')

if (n in name_list):
    print('The given name is present in the name-list')
else:
    print('Sorry!!! No name found in the list')
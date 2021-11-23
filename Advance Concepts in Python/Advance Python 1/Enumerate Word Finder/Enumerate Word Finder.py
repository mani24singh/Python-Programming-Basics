# PROGRAM TO SOLVE THE FOLLOWING PROBLEM STATEMENT
'''
PROBLEM STATEMENT : Write a program to print third, fifth and 
seventh element from a list using enumerate function.
'''

list = ['Spiderman', 'batman', 'wonderwomen', 'flash',
        'Ironman', 78.56, 'CaptainAmerica', 'DoctorStrange', 'Hulk', 306]

for index, item in enumerate(list):
    if index==2 or index==4 or index==6:
        # print(index, item)
        print(f"The element in list at position-{index+1} is {item}")

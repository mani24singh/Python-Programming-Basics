# PROGRAM TO LOOP ITEMS ENTERED BY A USER IN THE LIST USING FOR-LOOP

# Creating an input function for the items
i1 = input('Enter the item no.1 : \n')
i2 = input('Enter the item no.2 : \n')
i3 = input('Enter the item no.3 : \n')
i4 = input('Enter the item no.4 : \n')
i5 = input('Enter the item no.5 : \n')
i6 = input('Enter the item no.6 : \n')

l = [i1,i2,i3,i4,i5,i6]  # entering the items in the list

print('The items entered are :')

# creating a for loop for items to print
for items in l:
    print(items)
else:
    print('The list has been completed.')

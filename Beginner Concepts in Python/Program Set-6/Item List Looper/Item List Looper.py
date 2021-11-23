# PROGRAM TO PRINT A LIST OF CONTENTS USING A WHILE LOOP

# Creating a list:

furniture = ['chair','table','sofa','bed','Air-conditioner','refrigerator','dinning-table',
    'cupboard','washing-machine','geyser','dressing-table','television']

# Creating a while looper for the list
i = 0

while i<len(furniture):
    print(furniture[i])
    i = i+1

print('List completed.')  # printing the ending comment
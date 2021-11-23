# PROGRAM TO BUILD A MULTIPLICATION FILES IN A TABLE FOLDER

'''
Problem statement: write a program to generate multiplication tables from 1 to 30.
write it to the different files and place these files in a folder for a small kid.
'''
for i in range(1,31):
    with open(f'tables/Multiplication-Table_Of_{i}.txt','w') as f:
        for j in range(1,11):
            f.write(f'{i} X {j} = {i*j}')
            if j!=10:
                f.write('\n')
print('Done. Please check tables folder.')

# PROGRAM TO PRINT A MULTIPLICATION TABLE OF N-NUMBER USING FOR-LOOP IN REVERSE ORDER


num = int(input('Enter the number: '))  # input number function

for i in range(10,0,-1):    # using negative -1 index for reversing process
    print(f'{num}*{i}={num*i}')

print('Done')
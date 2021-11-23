# PROGRAM TO PRINT A MULTIPLICATION TABLE OF A GIVEN NUMBER USING FOR LOOP

# user input
num = int(input('Please enter a number whose table you wish to print :\n'))

# for loop
for i in range(1,11):
    #print(str(num)+'X'+str(i)+'='+ str(num*i))
    print(f"{num}X{i}={num*i}")     # using f-string 
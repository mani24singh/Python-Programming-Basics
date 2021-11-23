# PROGRAM TO FIND THE GREATEST AMONG THREE NUMBERS USING FUNCTION
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))

def greatest(n1,n2,n3):
    if (n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3 

result = greatest(a,b,c)
print('The greatest of the three given number is :', result)

# PROGRAM TO CONVERT CELCIUS TO FEHRENHEIT USING FUNCTION

n = int(input('Enter the degree celcius temperature: '))

def conv(cel):
    feh = (cel*(9/5))+32
    return feh
    

f = conv(n)
print('The fehrenheit temperature is : ',f)


# PROGRAM TO SHOWCASE THE USE OF FILTER FUNCTION

def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


l = [1, 22, 33, 4, 45, 6, 937, 8, 877, 54, 32, 56]

print(list(filter(greater_than_5,l)))

#   FILTER SYNTAX : list(filter(function,l))

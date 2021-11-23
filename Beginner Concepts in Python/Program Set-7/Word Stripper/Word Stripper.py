# PROGRAM TO REMOVE A WORD FROM A GIVEN STRING AND STRIP IT AT SAME TIME


def remove_strip(string, word):
    newstr = string.replace(word,"")
    return newstr.strip()

sen = "        i am learning python programming        "
n = remove_strip(sen,"python programming")
print(n)


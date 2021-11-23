# PROGRAM TO CREATE A COPY OF A TEXT FILE 

with open('myfile.txt') as f:
    content = f.read()

with open('copy.txt', 'w') as f:
    f.write(content)


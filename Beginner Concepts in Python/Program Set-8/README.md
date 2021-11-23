## File I/O :
- The random access memory is volatile, and all its contents are lost once a program terminates.
- In order to persist the data forever, we use files. A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.
- Types of Files :
   - There are 2 types of files:
     1. Text files (.txt, .c, etc)
     2. Binary files (.jpg, .dat, etc)
- Python has a lot of functions for reading, updating, and deleting files :
- Opening a file : Python has an open() function for opening files. It takes 2 parameters: filename and mode.
- Reading a file in Python : 
   - Opens the file in r mode and Read its content. 
   - We can also specify the number of characters in read() function to Read characters as required.
   - We can also use f.readline() function to read one full line at a time.
- Modes of opening a file :
   1. r – open for reading
   2. w – open for writing
   3. a – open for appending
   4. '+' will open for updating
   5. ‘rb’ will open for read in binary mode
   6. ‘rt’ will open for read in text mode
- Writing Files in Python : In order to write to a file, we first open it in write or append mode, after which, we use the python’s f.write() method to write to the file.
- With statement : The best way to open and close the file automatically is the “with” statement as there is no need to write f.close() as it is done automatically.

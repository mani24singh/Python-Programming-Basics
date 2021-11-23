# PROGRAM TO CHECK RESULT(PASS/FAIL) TAKING STUDENT MARKS AS INPUT FROM USER
''' 
Condition 1 : total passing percentage is atleast 40%.
Condition 2 : Subject-wise passing is atleast 33% in each subject.
Assumption : Consider 3-subjects and each subject being total of 100 marks.
'''

# user input function:
sub1 = int(input('Enter the secured marks for the English subject : '))
sub2 = int(input('Enter the secured marks for the Mathematics subject : '))
sub3 = int(input('Enter the secured marks for the Science subject : '))

m = (sub1+sub2+sub3)/3   # as (total secured marks for 3-subjects)/total * 100 = total/300*100 

if (sub1<33 or sub2<33 or sub3<33):
    print("You are failed due to securing marks less than 33 in one of the subject")

elif m <= 40:

    print("You are failed due to total marks less than 40 percent")

else:
    print("Congrats!! You are Passed with " + str(m) +'%')

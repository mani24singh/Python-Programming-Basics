# Program To Automate A Job-Selection Mail Letter Template:

mail = '''Hello, |GREETING| |NAME|
This mail is regarding your selection for the desired role as |JOBROLE| .
Your joining date is : |JOINDATE| .
we wish a very good luck for the selection.
Have a Great day ahead. Thankyou

Regards,
|HR_Name|
Human Resource Head
|Mobile No|
Kotak Mahindra(Mumbai)

Date : |todayDate|
'''
greeting = input('Enter the Greeting :\n')
name = input('Enter the Candidate Name :\n')
jobrole = input('Enter the Job Role :\n')
joindate = input('Enter the Joining Date :\n')
hr = input('Enter the HR-head name :\n')
contact = input('Enter the HR contact number :\n')
date = input("Enter today's date :\n")

mail = mail.replace('|GREETING|',greeting) 
mail = mail.replace('|NAME|',name)
mail = mail.replace('|JOBROLE|',jobrole)
mail = mail.replace('|JOINDATE|',joindate)
mail = mail.replace('|HR_Name|',hr)
mail = mail.replace('|Mobile No|',contact)
mail = mail.replace('|todayDate|',date)

print(mail)



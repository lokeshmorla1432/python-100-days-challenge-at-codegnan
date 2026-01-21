#get number of students in the class
'''n=int(input("Enter number of students in the class: "))
present_count=0
absent_count=0
for rollno in range(1,n+1):
    print("Enter roll no student",rollno,"is present or absent and select following option 1 or 2 \n 1.present \n 2.absent")
    status =input()
#check status
    if status =='1':
        present_count +=1
    elif status == '2':
        print("please select either 1 or 2 options")
print("Total students in the class:",n)
print("Number of students present:",present_count)
print("Number of students absent:",absent_count)
percentage=(present_count /n)*100
print("Attendence Report:",percentage)'''



#get number of students in the class
'''n=int(input("Enter number of students in the class: "))
present_count=0
absent_count=0
rollno =1#initialization
while rollno<=n:#condition
    print("Enter roll no student",rollno,"is present or absent and select following option 1 or 2 \n 1.present \n 2.absent")
    status =input()
#check status
    if status =='1':
        present_count +=1
        rollno +=1#increment
    elif status == '2':
        absent_count +=1
        rollno +=1 #increment
        print("please select either 1 or 2 options")
print("Total students in the class:",n)
print("Number of students present:",present_count)
print("Number of students absent:",absent_count)
percentage=(present_count /n)*100
print("Attendence Report:",percentage)'''


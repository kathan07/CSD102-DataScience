i =int(input("Enter a number:"))
b =i
c =0
while(i>0):
    d=i%10
    c=c*10+d
    i =i//10
if(b==c):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

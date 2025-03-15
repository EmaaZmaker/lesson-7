mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
total=mark1+mark2+mark3+mark4+mark5
avg=total/5
if avg>=91 and avg<=100:
    print("you are in grade A1")
elif avg>=81 and avg<91:
    print("you are in grade A2")
elif avg>=71 and avg<81:
    print("you are in grade B1")
elif avg>=61 and avg<71:
    print("you are in grade B2")
elif avg>=51 and avg<61:
    print("you are in grade C1")
elif avg>=41 and avg<51:
    print("you are in grade C2")
elif avg>=33 and avg<41:
    print("you are in grade D")
elif avg>=21 and avg<33:
    print("you are in grade E1")
elif avg>=0 and avg<21:
    print("you are in grade E2")
else:
    print("Invalid input")
    


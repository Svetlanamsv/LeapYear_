print("Input year : ")
y = int(input())
if y % 4 != 0:
    print("The year is ordinary")
elif y % 100 == 0:
    if y % 400 == 0:
        print("The is leap")
    else:
        print("The year is ordinary")
else:
    print("The is leap")
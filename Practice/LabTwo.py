# Amount Discount

amount = int(input("Enter Amount: "))

if amount < 1000:
    discount = amount * 0.05
    print("Discount ", discount)
elif amount < 5000:
    discount = amount * 0.10
    print("Discount ", discount)
else:
    discount = amount * 0.5
    print("Discount", discount)

print("Net Payable: ", amount - discount)

# Age Category 

age = int(input("Enter Amount: "))

if age < 13:
    print("Child")
elif 13 < age < 19:
    print("Teenager")
elif 20 < age < 59:
    print("Adult")
else:
    age >= 60
    print("Senior", age)

# For Lopp

colors = ["red", "yellow", "blue"]
for x in colors:
    print(x)

# Min Max

MyList = [5, 47, 98, 3, 2, 5, 0 ,1]

print("Min: ", min(MyList))
print("Max: ", max(MyList))

# Min Max With For

MyList = [5, 47, 98, 3, 2, 5, 0 ,1]

min = 0
max = 0

for x in MyList:
    if(x < min):
        min = x
    if(x > max):
        max = x
        
        
print(min)
print(max)

# Function

def addTwoNum(a, b):
    c = a + b
    print(c)
    
addTwoNum(2, 3)

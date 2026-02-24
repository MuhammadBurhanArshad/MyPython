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




def check_number(x):
    if(x < 0):
        return "Negative"
    elif(x > 0):
        return "Positive"
    else:
        return "Zero"
        
print(check_number(0))





def check_even_odd(n):
    if(n % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(check_even_odd(1))




def get_age_category(age):
    if age < 13:
        return "Child"
    elif 13 < age >= 19:
        return "Teenager"
    elif 20 < age >= 59:
        return "Adult"
    else:
        age >= 60
        return "Senior"

        
print(get_age_category(10))





def compare_numbers(a, b):
    if(a > b):
        return "First is Greater"
    elif(b > a):
        return "Second is Greater"
    else:
        return "Both are Equal"
    
print(compare_numbers(2,3))



#5


def validate_login(username, password):
    correct_username = "admin"
    correct_password = "1234"
    
    if username != correct_username:
        return "Invalid Username"
    elif password != correct_password:
        return "Invalid Password"
    else:
        return "Login Successful"
    
print(validate_login("admin", "1234"))





#6



def check_temperature(temp):
    if temp <= 0:
        return "Freezing"
    elif 1 <= temp <= 15:
        return "Cold"
    elif 16 <= temp <= 30:
        return "Warm"
    else:
        return "Hot"

    
print(check_temperature(-5))



# 7



def calculate_shipping(order_amount):
    if order_amount < 1000:
        shipping = 200
    elif 1000 <= order_amount <= 4999:
        shipping = 100
    else:
        shipping = 0
    
    total = order_amount + shipping
    return f"Total Payable Amount: {total} (Shipping: {shipping})"


print(calculate_shipping(800))

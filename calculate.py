def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y == 0:
       print("Error! Division by zero is not allowed.")
       return
   else:
       return x / y

# �׽�Ʈ �ڵ�
print(add(5, 3))      # ���: 8
print(subtract(5, 3)) # ���: 2
print(multiply(5, 3)) # ���: 15
print(divide(5, 3))   # ���: �� 1.66667 

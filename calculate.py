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

# 테스트 코드
print(add(5, 3))      # 출력: 8
print(subtract(5, 3)) # 출력: 2
print(multiply(5, 3)) # 출력: 15
print(divide(5, 3))   # 출력: 약 1.66667 

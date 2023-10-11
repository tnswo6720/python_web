from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# 예시로 1990년 3월 15일에 태어난 사람의 나이를 계산
birthdate = date(1990, 3, 15)
print(calculate_age(birthdate))

from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# ���÷� 1990�� 3�� 15�Ͽ� �¾ ����� ���̸� ���
birthdate = date(1990, 3, 15)
print(calculate_age(birthdate))

def calculate_bmi(height, weight):
    bmi = weight / height ** 2
    if bmi <= 18:
        category = "small"
    elif bmi <= 25:
        category = "medium"
    else:
        category = "big"
    print(f"your category is {category}")
    return bmi


result = calculate_bmi(1.8, 70)
print(f"{result:.2f}")

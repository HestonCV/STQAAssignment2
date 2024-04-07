def categorize_bmi(bmi):
    if bmi <= 18.4:
        return "Underweight"
    elif 18.4 < bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
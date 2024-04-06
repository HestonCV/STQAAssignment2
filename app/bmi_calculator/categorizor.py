def categorize_bmi(bmi):
    if bmi < 18.4: # Changed here
        return "Underweight"
    elif 18.4 <= bmi < 25: # And here
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
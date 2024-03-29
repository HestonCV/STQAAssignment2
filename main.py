from bmi_calculator import calculate_bmi
from bmi_category import categorize_bmi

def main():
    while True:
        try:
            height = float(input('Enter your height in inches: '))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    while True:
        try:
            weight = float(input('Enter your weight in pounds: '))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    bmi = round(calculate_bmi(height, weight), 2)
    category = categorize_bmi(bmi)
    print(bmi, category)

if __name__ == "__main__":
    main()
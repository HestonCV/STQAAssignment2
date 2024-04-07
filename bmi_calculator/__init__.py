try:
    from bmi_calculator.calculator import calculate_bmi
    from bmi_calculator.categorizor import categorize_bmi
except ImportError:
    from calculator import calculate_bmi
    from categorizor import categorize_bmi

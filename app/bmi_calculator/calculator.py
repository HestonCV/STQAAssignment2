# Calculation is based on the information attached to the assignment

def calculate_bmi(height, weight):
    kilos = weight * 0.45
    
    # Convert inches to meters
    meters = height * 0.025

    return kilos / meters**2

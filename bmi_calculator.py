def calculate_bmi(height, weight):
    kilos = weight * 0.45
    
    # Convert feet and inches to meters
    feet = height[0]
    inches = height[1] + feet*12
    meters = inches * 0.025

    return kilos / meters**2

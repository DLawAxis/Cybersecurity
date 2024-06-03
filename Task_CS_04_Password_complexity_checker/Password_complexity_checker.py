import re

def password_strength(password):
    # Initialize variables
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Calculate strength score
    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    # Determine strength based on score
    if score == 0:
        strength = "Very Weak"
    elif score == 1:
        strength = "Weak"
    elif score == 2:
        strength = "Moderate"
    elif score == 3:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return strength

def provide_feedback(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not re.search(r'\d', password):
        feedback.append("Password should contain at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should contain at least one special character.")
    
    return feedback

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    feedback = provide_feedback(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")

  
main()
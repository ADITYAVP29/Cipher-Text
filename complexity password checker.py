def check_password_complexity(password):
    if len(password) < 8:
        return "THE Password is too short.It should be at least 8 characters long."
    
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*()-_=+[{]};:\'",<.>/?`~' for char in password)
    
    if not has_lowercase:
        return "Password should contain at least one lowercase letter."
    if not has_uppercase:
        return "Password should contain at least one uppercase letter."
    if not has_digit:
        return "Password should contain at least one digit."
    if not has_special:
        return "Password should contain at least one special character."
    
    return "Password meets complexity requirements."

password = input("Enter the password: ")
result = check_password_complexity(password)
print(result)

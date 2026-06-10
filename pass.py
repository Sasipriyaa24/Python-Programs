# Valid Password Problem
# Password should be at least 8 characters long.
# Password should contain at least one digit.
# Password should contain at least one uppercase letter.
# Password should contain at least one lowercase letter.
# Password should contain at least one special character.
# Password should not contain spaces.

def valid_passoword(password):
    if len(password)<8:
        return False
    digit = False
    upper = False
    lower = False
    special = False
    special_chars = ['!','@','#','$','%','^','&',
                     '*','(',')','_','-','+','=']
    for i in password:
        if i>='0' and i<='9':
            digit = True
        elif i>='A' and i<='Z':
            upper = True
        elif i>='a' and i<='z':
            lower = True
        elif i in special_chars:
            special = True
        else:
            return False
    if digit and upper and lower and special:
        return True
    else:
        return False

password = "bc@hgvjbk32"
print(valid_passoword(password))
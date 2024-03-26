def is_nneg_float(s):
    hasAtLeastOneDigit = False
    for char in s:
        if char.isdigit() == False:
            if char != ".":
                return False
        else:
            hasAtLeastOneDigit = True
            
    if hasAtLeastOneDigit: return True
    
    return False

def get_nneg_float(prompt):
    inputString = input(prompt)
    while is_nneg_float(inputString) == False:
        print("must be a flaot value; please try again.\n\n")
        inputString = input(prompt)
    return float(inputString)
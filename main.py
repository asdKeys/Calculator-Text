value1 = 0
value2 = 0
sign = "e"
stop_calculator = "no"
keep = "yes"

def input_first_value():
    global value1
    global keep
    if keep == "no":
        print("First Number: ", value1)
    else:
        value1 = float(input("Enter First Number: "))
    
def input_sign():
    global sign
    sign = input("Enter Sign(+, -, *, /): ")
    if sign not in ["+", "-", "*", "/"]:
        print("Invalid Input")
        sign = input("Re-Enter Sign Or Type 'help' For A List Of Inputs: ")
    while sign not in ["+", "-", "*", "/"]:
        if sign == "help":
            print("Type '+' To Add")
            print("Type '-' To Subtract")
            print("Type '*' To Multiply")
            print("Type '/' To Divide")
        sign = input("Re-Enter Sign Or Type 'help' For A List Of Inputs: ")
        
def input_second_value():
    global value2
    value2 = float(input("Enter Second Number: "))
    
def finish_equation():
    global sign
    global value1
    global value2
    if sign == "+":
        value1 = value1 + value2
    elif sign == "-":
        value1 = value1 - value2
    elif sign == "*":
        value1 = value1 * value2
    else:
        value1 = value1 / value2
    print(value1)
    
def clear_calculator():
    global value1
    global value2
    global sign
    global keep
    print("ALERT, An Invalid Input Will Clear Your Calculator Here")
    keep = input("Clear Calculator?(type 'yes' or 'no'): ")
    if keep == "no":
        print("Your Data Has Been Saved")
    else:
        print("Your Data Has Been Cleared")
        
def main_loop():
    global value1
    global value2
    global sign
    global stop_calculator
    global keep
    while stop_calculator == "no":
        input_first_value()
        input_sign()
        input_second_value()
        finish_equation()
        print("ALERT, An Invalid Input Will End Your Session Here")
        stop_calculator = input("End Session?(type 'yes' or 'no': ")
        if stop_calculator == "no":
            clear_calculator()
    
main_loop()


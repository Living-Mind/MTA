import re

def phone_matcher(phone_number):
    #if re.match("^[+]?(359)?\s?[0-9]{9,10}$", phone_number) == True:
    if re.fullmatch("(^[+](359)?\s?[0-9]{9}$)|^[0-9]{10}$", phone_number):
        print("Valid number")
    else:
        print("Not Valid number")

    #print(phone_number)

#phone_matcher("4")
phone_matcher("+359 887605061")
phone_matcher("0887582381")
phone_matcher("+3529 887605061")
phone_matcher("08873582381")
phone_matcher("+35288760061")
phone_matcher("088582381")

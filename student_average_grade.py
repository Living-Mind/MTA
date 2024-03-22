data = {
    "Alice": 85,
    "Bob": 75,
    "Charlie": 90
}

#print(len(list(data.values())))

#values_calc = sum(list(data.values()))/

#print(values_calc)

def average_calc():
    #print(data)
    calc = sum(list(data.values()))/len(list(data.values()))
    print(calc)
    

average_calc()
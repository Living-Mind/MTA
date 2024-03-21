entry = int(input("Input: "))
x = 1

if entry < 0:
    print("The num is negative")
else:
    for i in range(1, entry + 1):
        #print(i)
        x *= i
        #print(x)
        
print("Output: " + str(x))

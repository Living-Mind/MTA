even_list = []

for i in range(2,22,2):
    #print(i)
    even_list.append(i)

for z in even_list:
    if z % 5 == 0:
        even_list.remove(z)

print(even_list)
from math import pi
def calculate_area(shape :str, radius :float, length :int, width :int):

    if shape == "circle":
        print(f'The calculated area {float(pi * radius ** 2)}')

    elif shape == "ractangle":
        print(f'The calculated area {float(length * width)}')

    else:
        print("Choose circle or ractangle")

calculate_area("circle", 1.1, 0, 0)
calculate_area("ractangle", 0, 4, 7)

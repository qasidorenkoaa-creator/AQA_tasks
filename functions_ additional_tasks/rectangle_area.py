def rectangle_area (length, width):
    return length * width
length = 5
width = 3
area = rectangle_area (length, width)
print(f"Площадь прямоугольника с длиной {length} и шириной {width} равна {area}.")

# вариант 2 ( я бы сделал так но по условию нужно использовать return
def rectangle_area(length, width):
    area = length * width
    print(f"Площадь прямоугольника с длиной {length} и шириной {width} равна {area}.")
rectangle_area(5, 3)

# вариант 3 ()
def rectangle_area (length, width):
    return length * width
area = rectangle_area (5, 3)
print(f"Площадь прямоугольника с длиной 5 и шириной 3 равна {area}.")
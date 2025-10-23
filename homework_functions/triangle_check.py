def check_triangle():
    side_a = int and float(input("Введите длину первой стороны: "))
    side_b = int and float(input("Введите длину второй стороны: "))
    side_c = int and float(input("Введите длину третьей стороны: "))
    if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
        if side_a == side_b == side_c:
            print("Результат: Треугольник равносторонний")
        elif side_a == side_b or side_a == side_c or side_b == side_c:
            print("Результат: Треугольник равнобедренный")
        elif side_a != side_b != side_c:
            print("Результат: Треугольник разносторонний")
    else:
        print("Треугольник не возможно построить")
check_triangle()
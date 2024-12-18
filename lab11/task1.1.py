def find_elliptic_curve_points(p):
    points = [(None, None)]  # Нескінченно віддалена точка 0
    for x in range(p):
        right_side = (x ** 3 + x + 1) % p
        for y in range(p):
            if (y * y) % p == right_side:
                points.append((x, y))

                if y > 0 and y != p - y:
                    points.append((x, p - y))
    return points


p = 23
curve_points = find_elliptic_curve_points(p)

print(f"Точки еліптичної кривої y^2 = (x^3 + x + 1) mod {p}:")
for point in curve_points:
    if point[0] is not None:
        print(f"({point[0]}, {point[1]})")
    else:
        print("Нескінченно віддалена точка 0")

print(f"\nЗагальна кількість точок: {len(curve_points)}")
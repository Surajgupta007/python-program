def generate_pascals_triangle(num):
    pascal_triangle = []

    for i in range(num):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = pascal_triangle[i - 1]
                row.append(prev_row[j - 1] + prev_row[j])
        pascal_triangle.append(row)

    return pascal_triangle

def print_pascals_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

try:
    num = int(input("Enter the number of rows for Pascal's Triangle: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        pascal_triangle = generate_pascals_triangle(num)
        print_pascals_triangle(pascal_triangle)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

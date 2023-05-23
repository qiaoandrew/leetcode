def generate(num_rows):
    rows = [[1]]

    for row in range(2, num_rows + 1):
        new_row = [1] * row

        for col in range(1, row - 1):
            new_row[col] = rows[-1][col - 1] + rows[-1][col]

        rows.append(new_row)

    return rows


print(generate(5))
print(generate(1))
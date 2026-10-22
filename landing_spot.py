def find_landing_spot(matrix):
    best_spot = None
    lowest_danger = None

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                continue  # Skip non-zero cells

        danger = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[row]):
                danger += matrix[r][c]

            if lowest_danger is None or danger < lowest_danger:
                lowest_danger = danger
                best_spot = (row, col)  

        return best_spot

print(find_landing_spot([[0, 1, 2], [3, 0, 4], [5, 6, 0]]))  # Example usage
def number_pattern(n):
    if not isinstance(n, int):
        return 'The input should be an integer'
    if n <= 0:
        return 'The input should be a positive integer'
    
    pattern = ''
    for num in range(1, n+1):
        pattern += str(num) + ' '
    return pattern.strip()
print(number_pattern(12))
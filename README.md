# Exoplanet Search Explanation

This project contains a function named `has_exoplanet(readings)` in [exoplanet_search.py](./exoplanet_search.py).

## What the code does

The function takes a string as input and checks whether any character meets a specific mathematical condition.

```python
def has_exoplanet(readings):
    values = [int(char, 36) for char in readings]

    total = sum(values)
    count = len(values)

    for value in values:
        if value * 5 * count <= 4 * total:
            return True
    return False

print(has_exoplanet("freecodecamp"))
```

## Step by step

### 1. Convert each character to a number

```python
values = [int(char, 36) for char in readings]
```

This turns each character into a number using base-36 conversion.

Examples:

- `int('a', 36)` = 10
- `int('z', 36)` = 35
- `int('0', 36)` = 0
- `int('f', 36)` = 15

This means that letters and digits are converted into numeric values based on their position in the base-36 system.

### 2. Calculate the total and count

```python
total = sum(values)
count = len(values)
```

- `total` is the sum of all converted values.
- `count` is how many characters are in the string.

### 3. Check the condition

```python
for value in values:
    if value * 5 * count <= 4 * total:
        return True
return False
```

For each character value, the program checks whether this inequality is true:

`value * 5 * count <= 4 * total`

If the condition is true for even one character, the function returns `True`.
If none of the values match the condition, it returns `False`.

In plain English, the function is testing whether there is at least one character that is small enough compared to the total sum to satisfy the rule.

## Example

```python
print(has_exoplanet("freecodecamp"))
```

This runs the function against the string `"freecodecamp"` and prints the result.

## Notes

- The line `#return readings` is commented out and does not affect the program.
- This code is a simple custom logic check, not a real exoplanet detection algorithm.

## Landing Spot Explanation

The file [landing_spot.py](./landing_spot.py) contains a function named
`find_landing_spot(matrix)`. It is intended to find the safest location in a
grid.

```python
def find_landing_spot(matrix):
    best_spot = None
    lowest_danger = None

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                continue

            danger = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = row + dr, col + dc
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[row]):
                    danger += matrix[r][c]

            if lowest_danger is None or danger < lowest_danger:
                lowest_danger = danger
                best_spot = (row, col)

    return best_spot
```

### Step by step

1. `best_spot` stores the coordinates of the safest location found so far.
2. `lowest_danger` stores the smallest danger score found so far.
3. The nested `for` loops visit every cell in the matrix.
4. A cell is considered a possible landing spot only when its value is `0`.
5. The four neighboring directions are checked:
   - `(-1, 0)` means up.
   - `(1, 0)` means down.
   - `(0, -1)` means left.
   - `(0, 1)` means right.
6. The values of valid neighboring cells are added to `danger`.
7. If the current danger score is lower than the previous best score, the
   function saves the current coordinates.
8. After every cell has been checked, the function returns the safest
   coordinates as `(row, column)`.

For example:

```python
print(find_landing_spot([[0, 1, 2], [3, 0, 4], [5, 6, 0]]))
```

### Important indentation issue

In the current version of `landing_spot.py`, the danger calculation is
indented outside the inner `for col` loop. This means it does not correctly
calculate danger for every cell. The `return best_spot` statement is also
inside the outer row loop, so the function returns too early, after checking
only the first row.

To work as intended, the danger calculation and the comparison that updates
`best_spot` must be inside the inner loop, while `return best_spot` must come
after both loops have finished.

## Launch Fuel Explanation

The file [launch_fuel.py](./launch_fuel.py) contains a function named
`launch_fuel(payload)`. It calculates how much fuel is needed to launch a
payload, including the fuel's own weight.

```python
def launch_fuel(payload):
    fuel = payload / 5

    while True:
        needed = (payload + fuel) / 5
        additional = needed - fuel
        fuel = needed

        if additional < 1:
            break

    return round(fuel, 1)
```

### Step by step

1. The function receives the payload weight.
2. It starts with an initial estimate:

   ```python
   fuel = payload / 5
   ```

3. The `while True` loop repeatedly improves the estimate.
4. `needed = (payload + fuel) / 5` calculates the fuel required for both the
   payload and the fuel already estimated.
5. `additional = needed - fuel` calculates how much the estimate changed.
6. `fuel = needed` updates the fuel estimate.
7. The loop stops when the change is less than `1` unit of fuel.
8. `round(fuel, 1)` returns the result rounded to one decimal place.

For a payload of `50`, the estimates become approximately:

```text
10 -> 12 -> 12.4 -> 12.48 -> 12.496
```

The final estimate is rounded to `12.5`.

The example call:

```python
print(launch_fuel(50))
```

prints:

```text
12.5
```

In summary, the function uses repeated approximation to account for the fuel
needed to carry both the payload and the fuel itself.

## Battle of Words Explanation

The file [battle_of_words.py](./battle_of_words.py) contains two functions:
`word_value(word)`, which calculates a score for a word, and
`battle(our_team, opponent_team)`, which compares two teams of words.

```python
def word_value(word):
    total = 0

    for char in word:
        value = ord(char.upper()) - ord("A") + 1
        if char.isupper():
            value *= 2
        total += value

    return total


def battle(our_team, opponent_team):
    our_wins = 0
    their_wins = 0

    for ours, theirs in zip(our_team.split(), opponent_team.split()):
        our_score = word_value(ours)
        their_score = word_value(theirs)

        if our_score > their_score:
            our_wins += 1
        elif their_score > our_score:
            their_wins += 1

    if our_wins > their_wins:
        return "We win!"
    if our_wins < their_wins:
        return "We lose!"
    return "It's a tie!"
```

### `word_value(word)`

The function starts `total` at zero and processes each character in the word.
It converts the character to uppercase and uses its alphabet position:

- `A` has a value of `1`.
- `B` has a value of `2`.
- `Z` has a value of `26`.

Uppercase characters are worth twice as much as lowercase characters. For
example, `H` is worth `16`, while `h` is worth `8`. The value of every
character is added to `total`, which is returned as the word's score.

### The `ord()` function

The code uses `ord()` to convert a one-character string into its Unicode code
point:

```python
ord("A")  # 65
ord("a")  # 97
```

The built-in documentation can be displayed with:

```python
help(ord)
```

Its description is essentially:

```text
ord(c) -> integer
```

`ord(c)` returns the Unicode code point of the character `c`. The argument must
be a string containing exactly one character. In this program, subtracting
`ord("A")` from the uppercase character's code point converts alphabetic
characters into values starting at zero; adding `1` changes those values into
alphabet positions from `1` to `26`.

### `battle(our_team, opponent_team)`

The function separates both team strings into words with `.split()`. It then
uses `zip()` to pair the corresponding words from each team. Each pair is a
round:

1. Both words receive a score from `word_value()`.
2. The team with the higher score wins that round.
3. Equal scores do not increase either team's win count.
4. After all rounds, the function compares `our_wins` and `their_wins`.

It returns `"We win!"`, `"We lose!"`, or `"It's a tie!"`.

### The `zip()` function

The code uses `zip()` to combine corresponding words from the two teams:

```python
zip(our_team.split(), opponent_team.split())
```

The built-in documentation can be displayed with:

```python
help(zip)
```

Its description is essentially:

```text
zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.
```

`zip()` creates an iterator that combines items from multiple iterables into
tuples. For example:

```python
list(zip(["Hello", "World"], ["hello", "world"]))
# [("Hello", "hello"), ("World", "world")]
```

By default, `zip()` stops when the shortest iterable is exhausted. Therefore,
if the two team strings contain different numbers of words, extra words in
the longer team are ignored.

### Important correction

The line `help.ord` is invalid and should be removed. `help` is a built-in
helper function, so documentation is requested by calling `help(ord)`, not by
accessing `ord` as an attribute with `help.ord`.

The example:

```python
print(battle("Hello World", "hello world"))
```

prints:

```text
We win!
```

The words on our team contain uppercase letters, which receive double points.

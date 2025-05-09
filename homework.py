# Method 1: Using temporary variable
def swap_three_temp(a, b, c):
    print(f"Before swapping: a={a}, b={b}, c={c}")
    temp = a
    a = b
    b = c
    c = temp
    print(f"After swapping: a={a}, b={b}, c={c}")
    return a, b, c

# Method 2: Using arithmetic operations
def swap_three_arithmetic(a, b, c):
    print(f"Before swapping: a={a}, b={b}, c={c}")
    a = a + b + c
    b = a - (b + c)
    c = a - (b + c)
    a = a - (b + c)
    print(f"After swapping: a={a}, b={b}, c={c}")
    return a, b, c

# Method 3: Using Python's multiple assignment
def swap_three_pythonic(a, b, c):
    print(f"Before swapping: a={a}, b={c}, c={c}")
    a, b, c = b, c, a
    print(f"After swapping: a={a}, b={b}, c={c}")
    return a, b, c

# Test the functions
a, b, c = 10, 20, 30

print("Method 1 - Using temporary variable:")
swap_three_temp(a, b, c)

print("\nMethod 2 - Using arithmetic operations:")
swap_three_arithmetic(a, b, c)

print("\nMethod 3 - Using Pythonic way:")
swap_three_pythonic(a, b, c)
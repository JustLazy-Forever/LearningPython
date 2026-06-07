"""
    By      > Darshan Sherstha
    Roll    > KCED081BCT010
"""

import pandas as pd

def func(x):            # -1 and -1.2
    return x**6 + 10 * x**4 - 4 * x**2 + 8 * x - 1

def regula_falsi(a: float, b: float, Es: float = 1e-5, max_iter: int = 100):
   
    a_list = []
    b_list = []
    c_list = []
    i_list = []
    func_c_list = []

    for i in range(1, max_iter + 1):
        func_a = func(a)
        func_b = func(b)

        if func_b - func_a == 0:
            raise ValueError("Division by zero encountered in regula_falsi formula")

        c = (a * func_b - b * func_a) / (func_b - func_a)
        func_c = func(c)

        # record
        i_list.append(i)
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)
        func_c_list.append(func_c)

        if abs(func_c) < Es or func_c == 0:
            print(f"\n---> ROOT FOUND: {c:.5f}")
            break

        if func_a * func_c < 0:
            b = c
        else:
            a = c

    return {"Iter.": i_list, "a": a_list, "b": b_list, "c": c_list, "func(c)": func_c_list}


def display_table(table: dict):
    """Display the iteration results using a pandas DataFrame."""
    df = pd.DataFrame(table)
    print(df.to_string(index=False))

def get_input():
    while True:
        try:
            vals = input("Enter initial guesses a and b separated by space:\n> ").strip().split()
            if len(vals) != 2:
                print("Please enter exactly two numbers.")
                continue
            a, b = map(float, vals)

            if func(a) * func(b) >= 0:
                print("Product of functional values of initial guesses must be less than zero. Try again.\n")
                continue
            
            return a, b
        except ValueError:
            print("Invalid numbers. Try again.")


def main():
    a, b = get_input()
    table = regula_falsi(a, b)
    display_table(table)


if __name__ == '__main__':
    main()

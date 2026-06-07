"""
    By      > Darshan Sherstha
    Roll    > KCED081BCT010
"""
import pandas as pd

def func(x):        # 0 and -1
    return x**5 + 7 * x**4 - 1

def get_input():
    print("f(x) = x**5 + 7 * x**4 - 1")

    try:
        while True:
            guesses = input("Enter initial guesses:\n> ").strip().split()

            if len(guesses) != 2:
                print("\n---> Print exaclty two numbers! <---")
                continue
            X0, X1 = map(float, guesses)

            if func(X0) * func(X1) >= 0:
                print("\n--> The product of funcitonal values of guesses should be strictly less than zero. <---\n")
            else:
                break
    except ValueError:
        print("\n---> Invalid numbers; try again. <---\n")
        
    return [X0, X1]

def use_secant(X0, X1):
    TOL = 10*-5
    iter_list = []
    x0_list = []
    x1_list = []
    x2_list = []

    func_x0_list = []
    func_x1_list = []
    func_x2_list = []

    for iteration in range(1, 101):

        func_X0 = func(X0)
        func_X1 = func(X1)

        if func_X0 == func_X1: continue

        iter_list.append(iteration)

        x0_list.append(X0)
        x1_list.append(X1)

        func_x0_list.append(X0)
        func_x1_list.append(X1)
        
        X2 = X1 - func_X1 * (X1-X0)/(func_X1 - func_X0)
        func_X2 = func(X2)
        
        x2_list.append(X2)
        func_x2_list.append(func_X2)

        if ( abs(func_X2) < TOL or abs(func_X2) == 0): break;

        X0 = X1
        X1 = X2

    return {"Iter." : iter_list, "X,i-1" : x0_list, "X,i" : x1_list, 
            "func(X,i-1)": func_x0_list, "func(X,i)" : func_x1_list,
            "X,i+1" : x2_list,"func(X,i+1)" : func_x2_list
            }
    
def display_table(table:dict): 
    df = pd.DataFrame(table)
    print(df.to_string(index=False))

    print(f"\n---> ROOT = {df['X,i+1'].iat[-1]:.6f}")

def main():
    X0, X1 = get_input()
    table = use_secant(X0, X1)
    display_table(table)
    
if __name__ == "__main__":
    main()
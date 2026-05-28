import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys


def function(x):
	return x**2 - 5 * x + 5


def main() -> None:
	x = np.linspace(0, 10, 100)
	y = function(x)

	plt.plot(x, y)
	plt.title("Bisection Method")
	plt.grid()
	plt.xlabel("x ->")
	plt.ylabel("f(x) ->")

	check = True
	while check:
		initGuess_1 = float(input("Enter the 1st initial guess "))
		initGuess_2 = float(input("Enter the 2nd initial guess "))

		if function(initGuess_1) * function(initGuess_2) >= 0:
			print("Error; the product of the functional value of inputs must be strictly less than 0")
		else:
			check = False

	TOLERABLE_ERROR = 10**-5
	a = initGuess_1
	b = initGuess_2

	i = 0
	while True:
		m = (a + b) / 2
		func_a = function(a)
		func_b = function(b)
		func_m = function(m)

		if func_m * func_a < 0:
			b = m
		else:
			a = m

		i += 1
		if abs(func_m) < TOLERABLE_ERROR:
			print("Root Found")
			break

	print(m)
	print(f"Ran {i} iterations")
	plt.show()


if __name__ == "__main__":
	main()

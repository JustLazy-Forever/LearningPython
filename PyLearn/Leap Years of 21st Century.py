count = 0


def is_leap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


for year in range(2001, 2101):
    leap = is_leap(year)
    if leap:
        count += 1
    print(year, " -> ", leap)


print("Total number of leap years in the 21st Century: ", count)

# import time
# import sys

# print("Loading", end="", flush=True)

# for i in range(10):
#     for dots in range(4):
#         # Print dots
#         print("." * dots, end="", flush=True)
#         time.sleep(0.3)
#         # Backspace the dots to reset for the next loop
#         print("\b" * dots, end="", flush=True)

# print(" Done!")

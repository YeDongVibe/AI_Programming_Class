import random

LOWER = 0
UPPER = 100

def main():
    n = int(input("Enter the number of cities: "))
    filename = input("Enter the file name to store a new problem: ")
    outfile = open(filename, 'w')
    outfile.write(str(n) + "\n")  # n at the first line
    locations = []
    while n > 0:
        x = random.randint(LOWER, UPPER)
        y = random.randint(LOWER, UPPER)
        z = (x, y)
        loc = str(z) + "\n"
        if loc not in locations:
            locations.append(loc)
            n -= 1
    outfile.writelines(locations)
    outfile.close()

main()

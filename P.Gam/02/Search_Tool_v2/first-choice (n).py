#import numeric
from problem.problem import Numeric
LIMIT_STUCK = 100

def main():
    # Create an instance of numerical optimization problem
    p = Numeric()   # 'p': (expr, domain)
    p.setVariables()
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    p.storeResult(solution, minimum)
    p.describe()
    displaySetting(p)
    # Report results
    p.report()

def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of values
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC


def displaySetting(p):
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())
    print("Max evaluations with no improvement: {0:,} iterations"
          .format(LIMIT_STUCK))

main()

#first-choice: 단순, 제일 좋진 않아도 좋으면 고!! 따라서, steepest ascent보다 짧게 걸린다.
#steepest ascent: 제일 좋은 걸 찾아서 고!!
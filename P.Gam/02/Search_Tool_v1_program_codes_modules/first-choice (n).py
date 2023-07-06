from problem.numeric import *

def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)

def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of values
    valueC = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

def randomMutant(current, p): ###
    i = rd.randint(0, len(current) - 1) #우리는 0,1,2,3,4를 뽑아내야대기 때문에 '-1'해줘야한다.
    # d = rd.uniform(-DELTA, DELTA)
    if rd.uniform(0,1) > 0.5:
        d = DELTA
    else:
        d = -DELTA
    return mutate(current, i, d, p) # Return a random successor

main()

#first-choice: 단순, 제일 좋진 않아도 좋으면 고!! 따라서, steepest ascent보다 짧게 걸린다.
#steepest ascent: 제일 좋은 걸 찾아서 고!!
from problem.tsp import *

def main():
    # Create an instance of TSP
    p = createProblem()    # 'p': (numCities, locations, table(-> 직선거리 미리계산))
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)

def steepestAscent(p):
    current = randomInit(p)   # 'current' is a list of city ids
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def mutants(current, p): # Apply inversion
    n = p[0]
    neighbors = []
    count = 0
    triedPairs = [] #비교해서 같은 값이 있는지 없는지 체크용
    while count <= n:  # Pick two random loci for inversion
        i, j = sorted([random.randrange(n) for _ in range(2)]) #random 하게 2개 값을 뽑아냄
        if i < j and [i, j] not in triedPairs:
            triedPairs.append([i, j])
            curCopy = inversion(current, i, j) #뽑은 구간을 inversion한다.뒤집기 고고
            count += 1
            neighbors.append(curCopy)
    return neighbors #n개의 후보를 뽑게 됨

def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = evaluate(best, p)

    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue

    return best, bestValue

main()

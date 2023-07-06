from problem.numeric import *

def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain) #튜플은 값 변환이 안됨
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)

def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of values, 계속 업데이트되는 파트/ randomInit()-> 시작점을 모르기 떄매 random하게 넣어쥼
    valueC = evaluate(current, p) #valueC 시작점에 해당하는 함수값
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p) #successor(제일 좋은 변수), valueS(제일 좋은 함수값)
        if valueS >= valueC: #현재보다 좋은지 비교(후보값: valueS)
            break #후보값이 더 크면 나빠진 것임으로 탈출
        else:
            current = successor
            valueC = valueS
    return current, valueC

def mutants(current, p): ###
    neighbors = []
    for i in range(len(current)):
        mutant = mutate(current, i, DELTA, p)
        neighbors.append(mutant)
        mutant = mutate(current, i, -DELTA, p)
        neighbors.append(mutant)

    return neighbors     # Return a set of successors

def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = evaluate(best, p)

    # for successor in range(1, len(neighbors)):
    #     successorVal = evaluate(successor, p)
    #     if successorVal < bestValue:
    #         best = successor
    #         bestValue = successorVal     

    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue

    return best, bestValue

main()

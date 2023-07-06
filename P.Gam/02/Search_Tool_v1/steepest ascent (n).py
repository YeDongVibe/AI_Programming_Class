import random as rd
import math 

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)


def createProblem():
    ## Read in an expression and its domain from a file.
    filename = input("파일명을 입력하세요 : ")
    filename = f"C:/Ye_Dong/AI_Programming/P.Gam/Search_Tool_v1/problem/{filename}.txt"
    infile = open(filename, 'r')
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    expression = infile.readline().strip()  # 파일 첫번째 줄 읽기, strip()으로 공백 제거
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## 'varNames' is a list of variable names.
    ## 'low' is a list of lower bounds of the variables.
    ## 'up' is a list of upper bounds of the variables.
    varName = []
    low = []
    up = []
    line = infile.readline().strip()  # strip()으로 공백 제거
    while line != '':
        data = line.split(',')
        varName.append(data[0])
        low.append(float(data[1]))
        up.append(float(data[2]))
        line = infile.readline().strip()  # strip()으로 공백 제거

    domain = [varName, low, up]
    infile.close()
    return expression, domain



def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of values # 현재의 시작점
    valueC = evaluate(current, p) # 시작점에 해당하는 함수값
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p) # successor : 제일 좋은 변수 / valueS : 제일 좋은 함수값
        if valueS >= valueC: # 현재보다 좋은지 비교
            break # 후보값이 더 크면 나빠진 것음으로 탈출
        else:
            current = successor
            valueC = valueS
    return current, valueC


def randomInit(p): 
    init = [] # 초기화
    domain = p[1] # low 정보
    low = domain[1]
    up = domain[2] # up 정보
    for i in range(len(low)):
        r = rd.uniform(low[i], up[i])
        init.append(r)

    return init    # Return a random initial point as a list of values

def evaluate(current, p): # current : x의 값이 저장 / p : xn저장
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval # 함수 내부에서 값이 바뀔때는 global 선언을 해줘야 함
    
    NumEval += 1 # 호출 될 때마다 1씩 증가
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment) # exec : statement 계산 (String 형태)
    return eval(expr) # eval : expression 계산(string 형태)


def mutants(current, p): 
    neighbors = []
    for i in range(len(current)):
        mutant = mutate(current, i, DELTA, p)
        neighbors.append(mutant)
        mutant = mutate(current, i, -DELTA, p)
        neighbors.append(mutant)
    
    return neighbors     # Return a set of successors


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

def bestOf(neighbors, p): 
    best = neighbors[0]
    bestValue = evaluate(best, p)
    
    for i in range(1, len(neighbors)):
        val = evaluate(neighbors[i],p)
        if(val < bestValue):
            best = neighbors[i]
            bestValue = val
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()

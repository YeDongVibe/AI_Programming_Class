from problem.problem import *
from Optimizer import *


def main():
    p, alg = readPlanAndCreate()  # Setup and create (problem, algorithm)
    conductExperiment(p, alg)     # Conduct experiment & produce results
    p.describe()                  # Describe the problem solved
    alg.displayNumExp()           # Total number of experiments
    alg.displaySetting()          # Show the algorithm settings
    p.report()                    # Report result

def readPlanAndCreate():
    parameters = readValidPlan()  # Read and store in 'parameters'
    p = createProblem(parameters)
    alg = createOptimizer(parameters)
    return p, alg

def readValidPlan():  # Gradient Descent cannot solve TSP
    while True:
        parameters = readPlan() # save file's data in dictionary.
        if parameters['pType'] == 2 and parameters['aType'] == 4:
            print("You cannot choose Gradient Descent")
            print("       unless your want a numerical optimization.")
        else:
            break
    return parameters

def readPlan():
    fileName = input("Enter the file name of experimental setting: ")    
    # fileName = f"C:/K-Digital3/AI_Programming/Mr.Gam/Search Tool v4/{fileName}.txt"    
    infile = open(fileName, 'r')
    parameters = { 'pType':0, 'pFileName':'', 'aType':0, 'delta':0,
                   'limitStuck':0, 'alpha':0, 'dx':0, 'numRestart':0,
                   'limitEval':0, 'numExp':0 }
    parNames = list(parameters.keys())
    for i in range(len(parNames)):
        line = lineAfterComments(infile)
        if parNames[i] == 'pFileName':
            parameters[parNames[i]] = line.rstrip().split(':')[-1][1:]
        else:
            parameters[parNames[i]] = eval(line.rstrip().split(':')[-1][1:])
    infile.close()
    return parameters             # Return a dictionary of parameters        # Return a dictionary of parameters

def lineAfterComments(infile):    # Ignore lines beginning with '#'
    line = infile.readline()      # and then return the first line
    while line[0] == '#':         # with no '#'
        line = infile.readline()
    return line

def createProblem(parameters): ###
    # Create a problem instance (a class object) 'p' of the type as 
    # specified by 'pType', set the class variables, and return 'p'.
    pType = parameters['pType']
    if(pType == 1):
        p = Numeric()
    elif(pType == 2):
        p = Tsp()
    else:
        print("Choose from the number given")
    
    p.setVariables(parameters)

    return p

def createOptimizer(parameters): ###
    # Create an optimizer instance (a class object) 'alg' of the type  
    # as specified by 'aType', set the class variables, and return 'alg'.
    aType = parameters['aType']
    optimizers = {1 : 'SteepestAscent()', 2 : 'FirstChoice()', 3 : 'Stochastic()', 4 : 'GradientDescent()'}
    alg = eval(optimizers[aType])
    alg.setVariables(parameters)
    
    return alg

def conductExperiment(p, alg): # 주석처리는 Simulated Annealing과 random~~ 파트에서 사용
    # aType = alg.getAType()
    alg.randomRestart(p)
    # if 1 <= aType <= 4:
    #     alg.randomRestart(p)
    # else:
    #     alg.run(p)
    bestSolution = p.getSolution()
    bestMinimum = p.getValue()    # First result is current best
    numEval = p.getNumEval()
    sumOfMinimum = bestMinimum    # Prepare for averaging
    sumOfNumEval = numEval        # Prepare for averaging
    # sumOfWhen = 0                 # When the best solution is found
    # if 5 <= aType <= 6:
    #     sumOfWhen = alg.getWhenBestFound()
    
    # numExp >= 2 이면 실행
    numExp = alg.getNumExp()
    for i in range(1, numExp):
        alg.randomRestart(p)
        # if 1 <= aType <= 4:
        #     alg.randomRestart(p)
        # else:
        #     alg.run(p)
        newSolution = p.getSolution()
        newMinimum = p.getValue()  # New result
        numEval = p.getNumEval()
        sumOfMinimum += newMinimum
        sumOfNumEval += numEval
        # if 5 <= aType <= 6:
        #     sumOfWhen += alg.getWhenBestFound()
        if newMinimum < bestMinimum:
            bestSolution = newSolution  # Update the best-so-far
            bestMinimum = newMinimum
    # 평균값
    avgMinimum = sumOfMinimum / numExp
    avgNumEval = round(sumOfNumEval / numExp)
    # avgWhen = round(sumOfWhen / numExp)
    results = (bestSolution, bestMinimum, avgMinimum, avgNumEval, sumOfNumEval, '''avgWhen''')
    p.storeExpResult(results)

main()

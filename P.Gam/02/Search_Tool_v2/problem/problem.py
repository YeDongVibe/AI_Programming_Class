import math
import random

# interface
class Problem:
    def __init__(self): # 생성자 
        self._solution = [] # 변수 앞에 언더바(_)를 붙이는 이유는 class변수임을 명시하는 것
        self._value = 0
        self._numEval = 0
        
    def setVariables(self): # createProblem
        pass
    
    def randomInit(self):
        pass
    
    def evaluate(self):
        pass
    
    def mutants(self):
        pass
    
    def randomMutant(self):
        pass
    
    def describe(self): # describeProblem : 어떤 문제를 풀었는지 출력해주는 함수
        pass
    
    def storeResult(self, solution, value): # 최종 솔루션을 저장하는 함수
        self._solution = solution
        self._value = value
    
    def report(self): # numEval을 출력해주는 함수
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))

class Numeric(Problem): # Problem에서 상속을 받겠다
    def __init__(self):
        Problem.__init__(self) # important
        self._expression = ''
        self._domian = []
        self._delta = 0.01

class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locaions = []
        self._distanceTable = []

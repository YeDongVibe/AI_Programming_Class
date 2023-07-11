import math
import random as rd

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
        Problem.__init__(self) # important : super class의 initialize한 걸 쓰겠다.
        self._expression = ''
        self._domian = []
        self._delta = 0.01
        self._Limit = 100
    
    def getDelta(self): # displaysetting에서 delta를 사용하기 위해
        return self._delta
    
    def getLimit(self):
        return self._Limit
     
    def setVariables(self): # createProblem
        ## Read in an expression and its domain from a file.
        fileName = input("Enter the filename of a fuction: ")
        fileName = f"C:/Ye_Dong/AI_Programming/P.Gam/02/Search_Tool_v2/problem/{fileName}.txt"
        # fileName = f"C:/K-Digital3/AI_Programming/Mr.Gam/Search Tool v1 - program codes/problem/{fileName}.txt"
        infile = open(fileName, 'r')
        ## Then, return a problem 'p'.
        ## 'p' is a tuple of 'expression' and 'domain'.
        ## 'expression' is a string.
        self._expression = infile.readline().strip()
        ## 'domain' is a list of 'varNames', 'low', and 'up'.
        ## 'varNames' is a list of variable names.
        varNames = []
        ## 'low' is a list of lower bounds of the varaibles.
        low = [] 
        ## 'up' is a list of upper bounds of the varaibles.
        up = []

        line = infile.readline().strip()
        while line != '':
            data = line.split(',')
            varNames.append(data[0])
            low.append(float(data[1])) #Convert to float
            up.append(float(data[2])) #Convert to float
            line = infile.readline().strip()
    

        self._domain = [varNames, low, up]
        infile.close()
    
    def randomInit(self):
        domain = self._domain # domain : [varNames, low, up]
        low = domain[1]
        up = domain[2]
        
        init = []
        for i in range(len(low)):
            r = rd.uniform(low[i], up[i]) #uniform low bound, upper bound 에서 수를 랜덤하게 뽑아냄
            init.append(r)

        return init    # Return a random initial point
                    # as a list of values
    
    def evaluate(self, current):
        ## Evaluate the expression of 'p' after assigning
        ## the values of 'current' to the variables
        self._numEval += 1
        expr = self._expression # p[0] is function expression
        # domain = p[1] # p[1] is domain
        # varNames = domain[0]  
        varNames = self._domain[0]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i]) #ex. 'x1 = 3.2' 이런식으로 들어감
            exec(assignment) #exec함수: statement 계산 (String 값) -> 문자열로 표현된 식을 exec함수가 계산 가능한 함수로 인식
        return eval(expr) 
        #eval함수: expression 계산 (String 값) -> 문자열로 표현된 식을 exec함수가 계산 가능한 함수로 인식

    
    def mutants(self, current): # 주변의 값 뽑아내기
        neighbors = []
        for i in range(len(current)):
            mutant = self.mutate(current, i, self._delta)
            neighbors.append(mutant)
            mutant = self.mutate(current, i, -self._delta)
            neighbors.append(mutant)
            
        return neighbors
    
    
    def mutate(self, current, i, d):
        curCopy = current[:]
        domain = self._domain # [VarNames, low, up]
        l = domain[1][i]     # Lower bound of i-th
        u = domain[2][i]     # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy
            
    def randomMutant(self, current):
        i = rd.randint(0, len(current) - 1) #우리는 0,1,2,3,4를 뽑아내야대기 때문에 '-1'해줘야한다.
        # d = rd.uniform(-DELTA, DELTA)
        if rd.uniform(0,1) > 0.5:
            d = self._delta
        else:
            d = -self._delta
        return self.mutate(current, i, d) # Return a random successor

    
    def describe(self): # describeProblem : 어떤 문제를 풀었는지 출력해주는 함수
        print()
        print("Objective function:")
        print(self._expression)   # Expression
        print("Search space:")
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]

        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i])) 
    
    
    def report(self): # numEval을 출력해주는 함수
        print()
        print("Solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value)) # self._value는 minimun을 의미
        Problem.report(self) # == super().report

    def coordinate(self):
        c = [round(value, 3) for value in self._solution] # self._solution의 각각의 값을 value
        return tuple(c)  # Convert the list to a tuple
    
class Tsp(Problem): # Problem에서 상속을 받겠다
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []
        self._distanceTable = []

    
    def setVariables(self):
        ## Read in a TSP (# of cities, locatioins) from a file.
        ## Then, create a problem instance and return it.
        fileName = input("Enter the file name of a TSP: ")
        #fileName = 'problem/{filename}.txt'
        fileName = f"C:/Ye_Dong/AI_Programming/P.Gam/02/Search_Tool_v2/problem/{fileName}.txt"
        infile = open(fileName, 'r')
        # First line is number of cities
        self._numCities = int(infile.readline()) #첫번째 라인: 도시수

        line = infile.readline()  # The rest of the lines are locations
        while line != '': #라인이 끝날때까지
            self._locations.append(eval(line)) # Make a tuple and append eval(line) -> string으로 들어감
            line = infile.readline()
        infile.close()
        self._distanceTable = self.calcDistanceTable()
    
    
    def calcDistanceTable(self): ###
        table = [] #2d
        locations = self._locations
        for i in range(self._numCities):
            row = []
            for j in range(self._numCities):
                dx = locations[i][0] - locations[j][0]
                dy = locations[i][1] - locations[j][1]
                d = round(math.sqrt(dx**2 + dy**2), 1) #거리 계산 후 소수 첫째자리까지 표시!!
                row.append(d)
            table.append(row)

        #table 각각 도시 간의 거리
        return table # A symmetric matrix of pairwise distances
    
    def randomInit(self):   # Return a random initial tour
        n = self._numCities #도시 수
        init = list(range(n)) #0~n-1까지의 리스트가 만들어짐
        rd.shuffle(init)
        return init
    
    def evaluate(self, current): ###
        self._numEval += 1
        n = self._numCities
        table = self._distanceTable
        cost = 0 #인접한 도시들의 거리를 더한 것
        # 되기는 하는데 이해는 못하는 내가 짠 코드
        # numCities, _, table = p
        # for i in range(numCities - 1):
        #    r = current[i]
        #    rr = current[i + 1]
        #    cost += table[r][rr]
        ## Calculate the tour cost of 'current'
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
        for i in range(n-1):
            locFrom = current[i]
            locTo = current[i+1]
            cost += table[locFrom][locTo]
        cost += table[current[n-1]][current[0]] #맨 마지막에 돌아가야 하기 때문에 처음으로 돌아가는 거리를 더해쥼.
        return cost
    
    def mutants(self, current): # Apply inversion
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = [] #비교해서 같은 값이 있는지 없는지 체크용
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([rd.randrange(n) for _ in range(2)]) #random 하게 2개 값을 뽑아냄
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j) #뽑은 구간을 inversion한다.뒤집기 고고
                count += 1
                neighbors.append(curCopy)
        return neighbors #n개의 후보를 뽑게 됨
    
    def inversion(self, current, i, j):  ## Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i] #i번째 j번째 해당하는 값 한번에 바꿔버리기
            i += 1
            j -= 1
            ##-- 양쪽에서 좁혀오면서 양쪽끝단들을 서로 바꿔치기 하는 중
        return curCopy #뽑아내서 inversion 한 변경된current(curCopy) 그잡채를 return 함, current 자체를 변경하여 업데이트 해버리면 원 데이터를 잃어버릴수 있음으로 curCopy에 저장
    
    def randomMutant(self, current): # Apply inversion
        while True:
            i, j = sorted([rd.randrange(self._numCities)
                        for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    def describeProblem(self):
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()
                
                
    def report(self): # numEval을 출력해주는 함수
        print()
        print("Best order of visits:")
        self.tenPerRow()       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._value)))
        Problem.report(self)

    def tenPerRow(self):
        for i in range(len(self._solution)):
            print("{0:>5}".format(self._solution[i]), end='')
            if i % 10 == 9:
                print()
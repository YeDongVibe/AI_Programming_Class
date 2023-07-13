from problem.problem import *
from Optimizer import *

def main():
    p, pType = selectProblem() # 문제(파일) 선택
    alg = selectAlgorithm(pType) # 알고리즘 선택
    
    alg.run(p) # 알고리즘 동작
    
    p.describe() # 어떤 문제를 풀었는지 출력
    alg.displaySetting() # 알고리즘을 보여줌
    p.report() # 결과 출력


def selectProblem(): # Numeric인지 TSP인지 선택
    print('Select the problem type : ')
    print('1. Numeric')
    print('2. TSP')
    
    pType = int(input('Enter the number : ')) # 숫자입력
    
    if(pType == 1):
        p = Numeric()
    elif(pType == 2):
        p = Tsp()
    else:
        print("Choose from the number given")
    
    p.setVariables()
    return p, pType

def selectAlgorithm(pType): # 알고리즘 선택
    print('Select the Algorithm : ')
    print('1. Steepest Ascent')
    print('2. First Choice')
    print('3. Gradient Descent')
    
    aType = int(input('Enter the numver : '))
    
    # Dictionary 이용해 선택지 만들기
    optimizers = {1 : 'SteepestAscent()', 2 : 'FirstChoice()', 3 : 'GradientDescent()'}
    
    alg = eval(optimizers[aType]) # optimizers[aType]는 String이 선택되기에 이에 해당하는 숫자를 위해 eval사용
    
    alg.setVariables(pType) # 알고리즘 실행?
    return alg
    
    # if(aType == 1):
    #     alg = SteepestAscent()
    # elif(aType == 2):
    #     alg = FirstChoice()
    # elif(aType == 3):
    #     alg = GradientDescent()
    # else:
    #     print("Choose from the number given")
    
    # return alg, aType
    
    
main()
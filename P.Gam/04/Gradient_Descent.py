from problem.problem import Numeric

def main():
    # Create an instance of numerical optimization problem
    p = Numeric()
    p.setVariables() # 'p': (expr, domain) #튜플은 값 변환이 안됨
    # Call the search algorithm
    solution, minimum = gradientDescent(p) #
    # Show the problem and algorithm settings
    p.storeResult(solution, minimum)
    p.describe()
    displaySetting(p)
    # Report results
    p.report()


def gradientDescent(p):
    current = p.randomInit() # 'current' is a list of values, 계속 업데이트 되는 파트/ randomInit()-> 시작점을 모르기 떄매 random하게 넣어쥼
    valueC = p.evaluate(current) #valueC 시작점에 해당하는 함수값
    while True:
        successor = p.takeStep(current, valueC) # 한번더 값을 계산하는것을 방지하기 위해 valueC추가
        valueS = p.evaluate(successor) #successor(제일 좋은 변수), valueS(제일 좋은 함수값)
        if valueS >= valueC: #현재보다 좋은지 비교(후보값: valueS)
            break #후보값이 더 크면 나빠진 것임으로 탈출
        else:
            current = successor
            valueC = valueS
    return current, valueC


def displaySetting(p):
    print()
    print("Search algorithm : Gradient Descent")
    print()
    print("step size:", p.getalpha())
    
main()

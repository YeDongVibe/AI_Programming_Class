from abc import * # abstractBaseClass 불러오기

class Student(metaclass=ABCMeta):
    def __init__(self, name="", midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final = final
      
    def setName(self, name):
        self._name = name

    def setMidterm(self, midterm):
        self._midterm = midterm

    def setFinal(self, final):
        self._final = final

    def getName(self):
        return self._name     
    
    @abstractmethod    
    def calcSemGrade(self):
        pass
        # raise NotImplementedError("You must 뭐시기") # rasie : 사용자가 직접 에러를 일으킴
    
    def __str__(self):
        return self._name + "\t" + self.calcSemGrade()
     
class LGstudent(Student):
    
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

class PFstudent(Student):
        
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 60:
            return "Pass"
        else:
            return "Fail"



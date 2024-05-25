class Calcnums():
      def __init__(self, num1, num2, action):
        self.num1 = num1
        self.action = action
        self.num2 = num2
      def result_nums(self):
          self.num1=int(self.num1)
          self.num2=int(self.num2)
          if self.action == "+": 
            return sum([self.num1,self.num2])
          elif self.action == "*": 
            return (self.num1*self.num2)
          elif self.action == "/":
             return (self.num1/self.num2)
          elif self.action == "-":
             return(self.num1-self.num2)
             
        
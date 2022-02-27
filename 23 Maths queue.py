import random

class queue:
    def __init__(self):
        self.queue = [['',0] for x in range (5)]
        self.front = 0
        self.back = 0
        self.enqueue()
        
    def enqueue(self):
        questions = [['Find the highest common factor of 72 and 90',1],['Find the exact value of tan30 x sin60',1],['Write 180 minutes in hours',1],['Find the first 3 terms, in ascending powers of x, of the binomial expansion of (2 + (3x/4))^6',2],['Find the coordinates of the centre of the circle x^2 + y^2 - 4x + 8y - 8 = 0',2],['Prove that (x - 4) is a factor of 2x^3 - 13x^2 + 8x + 48',2],['Prove that tan3A = (3tan(A) - tan^3(A)) / (1 - 3tan^2(A))',3],['Given that (x + 3) is a factor of 3x^3 + 2ax^2 - 4x + 5a, find the value of the constant a',3],['Write 2x^2 + 4x + 9 in the form of a(x + b)^2 + c, where a, b and c are integers to be found',3]]
        while self.back != len(self.queue):
            self.queue[self.back] = questions.pop(random.randint(0,len(questions)-1))
            index = self.back
            while index != self.front and self.queue[index][1] < self.queue[index-1][1]:
                    temp = self.queue[index]
                    self.queue[index] = self.queue[index-1]
                    self.queue[index-1] = temp
                    index -= 1
            self.back += 1
        self.dequeue()
    
    def dequeue(self):
        print('Questions:')
        print()
        while self.front != 5:
            print('Question ' + str(self.front+1))
            print(self.queue[self.front][0])
            if self.queue[self.front][1] == 1:
                print('Difficulty: Easy')
            elif self.queue[self.front][1] == 2:
                print('Difficulty: Medium')
            else:
                print('Difficulty: Hard')
            print()
            self.queue[self.front] = ['',0]
            self.front += 1
        choice = input('Type 1 to generate another quiz: ')
        print()
        if choice == '1':
            self.front = 0
            self.back = 0
            self.enqueue()
        
queue = queue()
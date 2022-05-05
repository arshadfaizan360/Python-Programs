print('How far to count?')
HowFar = int(input()) #Correct prompt followed by HowFar assigned value entered by user
while HowFar < 1: #While loop with correct condition to terminate
  print('Not a valid number, please try again.')
  HowFar = int(input()) #Correct prompt followed by HowFar being assigned value entered by the user
for MyLoop in range (1, HowFar+1): #For loop including correct range
  if MyLoop % 3 == 0 and MyLoop % 5 == 0: #Correct syntax for MOD used in an if statement
    print('FizzBuzz')
  elif MyLoop % 3 == 0:
    print('Fizz')
  elif MyLoop % 5 == 0:
    print('Buzz') #Correct output for all cases
  else:
    print(MyLoop) #Correct output for else case

#(a) = 8/8
#(b) = 1/1

#(c) because the number of loops is known = 1/1
#(d) a letter [give example] could make the program crash, this can be prevented using exception handling (try and except) [or test the inputs to see if digits only] = 1/3
#(e) functions and commands are similar to English, decimal numbers can be used instead of binary, variables can be used instead of having to manipulate memory [identation, comments, procedures] = 0/3
#(f) aaab = YES, abbab = NO, bbbbba = YES; = 3/3
#(g) an odd number of a and any number of b = 2/2
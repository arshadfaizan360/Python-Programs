sumofsquares = 0
squareofsum = 0
for x in range(1,101):
    sumofsquares += x**2
    squareofsum += x
squareofsum = squareofsum ** 2
print(squareofsum - sumofsquares)
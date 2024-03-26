def calculateInitialDeposit(futureValue, intrest , numOfYears):
    return futureValue/(1+intrest)**numOfYears

futureValue = float(input("Enter the desired future value:"))
intrest =float(input("Enter the annual interest rate:"))
numOfYears = int(input("Enter the number of years the money will grow:"))
initialDeposit = calculateInitialDeposit(futureValue, intrest, numOfYears)
print(f'You will need to deposit this amount: {initialDeposit:0.8f}')

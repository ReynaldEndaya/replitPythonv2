print('This is a loan calculator!')
print()

loanAmount = float(input('How much is the loan amount? '))
loanTerm = int(input('How long is the loan term? '))
apr = float(input('What is the loan APR? Enter as whole number (ex. 5 for 5%) '))

print()
print('Year : Amount Owed')

for year in range(loanTerm):
    loanAmount += loanAmount * (apr/100)
    print(year+1,':',round(loanAmount,2))
    
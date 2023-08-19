print('30 Days Down')
print()
# def day_comment(comment):
    
for day in range(1,31):
    print(f'Day {day}')
    comment = input()
    print()
    response = f"You thought day {day} is {comment}"
    textLength = int(len(response))+10
    print(f"{response: ^{textLength}}")
    print()

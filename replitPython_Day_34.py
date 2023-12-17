# Let's extend this program and build option 4: "Get SPAMMING".

# Print out the first 10 email addresses with a custom email sent to each of those people.
# Print one email at a time, pause, and then clear the screen before the next email is printed.
# Example:

# Dear john@test.com
# It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.
# Love and hugs,
# Ian Spammington III

import os, time

emailAddress = ['test1','test2']

def printList():
    for index in range(len(emailAddress)):
        print(f"{index+1} {emailAddress[index]}")
        time.sleep(1)
        
printList()    
print('Please think of a number between 0 and 1000!')
upperbound = 1000
lowerbound = 0
while True:
    mid = (upperbound - lowerbound)/2 + lowerbound
    guess = input("your number is 'less' or 'equal' or 'more' than %s?" % mid)
    if guess == 'less':
        upperbound = mid
    elif guess == 'more':
        lowerbound = mid
    elif guess == 'equal':
        print('your number was: ' + str(mid))
        break
    else:
        print('no answer')
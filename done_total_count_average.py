num = 0
total = 0.0
print('Once you are done entering numbers, please write "done".')
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input!')
        continue
    num = num + 1
    total =  total + fval

print('\nTotal sum of numbers counted:', total, '\nNumber of values counted:', num, '\nAverage of numbers counted:', total/num)

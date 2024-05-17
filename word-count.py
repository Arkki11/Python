fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip()
    words = line.split()
    for word in words :
        # retrieve/create/update counter
        di[word] = di.get(word, 0) + 1

# the most common word
largest = -1
theword = None
for key, value in di.items() :
    if value > largest :
        largest = value
        theword = key # capture/remeber the word that was largest

print(theword, largest)

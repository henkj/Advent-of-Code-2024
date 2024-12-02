
def checkSafety(values):
    sortedValues = sorted(values)
    revSortedValues = sorted(values, reverse=True)
    if sortedValues != values and revSortedValues != values:
        return False

    foundIssue = False
    for n in range(1, len(values)):
        distance = abs(values[n] - values[n-1])
        if distance < 1 or distance > 3:
            foundIssue = True
    if not foundIssue:
        return True


def part(input):
    count = 0
    count2 = 0
    with open(input) as f:
        for line in f.readlines():
            values = [int(s) for s in line.split()]
            if checkSafety(values):
                count += 1

            for n in range(len(values)):
                newValues = values[:]
                newValues.pop(n)
                if checkSafety(newValues):
                    count2 += 1
                    break


        print(count)
        print(count2)


            
                


   

    
                
part('Day02/input/input.txt')

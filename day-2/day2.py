def part1():
    with open("/Users/juiceppe/Documents/Development/AdventOfCode2020/day-2/inputs.txt", "r") as passwordDatabase:
        password = passwordDatabase.readlines()
        validPassword = 0;  
        for i in password:
            policy = i.split(": ")[0]
            # 1-3 a
            targetLetter = policy.split(" ")[1]
            # a
            minMax = policy.split(" ")[0]
            #'1-3'
            minVal = minMax.split("-")[0]
            maxVal = minMax.split("-")[1]
            psw = i.split(": ")[1]
            timesFound = 0
            for letter in psw:
                if letter == targetLetter:                
                    timesFound += 1
            if timesFound >= int(minVal) and timesFound <= int(maxVal):
                validPassword += 1
    print("Answer to part 1: " + str(validPassword))
part1()

def part2():
    with open("/Users/juiceppe/Documents/Development/AdventOfCode2020/day-2/inputs.txt", "r") as passwordDatabase:
        password = passwordDatabase.readlines()
        validPassword = 0;  
        for i in password:
            policy = i.split(": ")[0]
            # 1-3 a
            targetLetter = policy.split(" ")[1]
            # a
            coordinates = policy.split(" ")[0]
            #'1-3'
            firstPosition = int(coordinates.split("-")[0])
            lastPosition = int(coordinates.split("-")[1])
            psw = i.split(": ")[1]
            if targetLetter in psw and (psw[firstPosition - 1] == targetLetter or psw[lastPosition - 1] == targetLetter) and psw[firstPosition -1] != psw[lastPosition - 1]:
                validPassword += 1
    print("Answer to part 2: " + str(validPassword))
part2()



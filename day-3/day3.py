def part1():
    slopes = []
    while True:
        if len(slopes) < 5:
            right = int(input("Enter coordinates X: "))
            down = int(input("Enter coordinates Y: "))
            with open("/Users/juiceppe/Documents/Development/AdventOfCode2020/day-3/inputs.txt", "r") as trees:
                t =  [z for z in trees.read().split("\n")[::down]] #Reading file and splitting by new line
            obstacles = 0
            x = 0
            for y in t:
                obstacles += (y[x % len(t[0])] == "#") #If we encounter a tree we add 1 to the obstacles
                x += right 
            slopes.append(obstacles)
            print("Result: " + str(obstacles))
            print(str(slopes))
        else:
            return slopes

def part2(slopes):
    result = 1
    for x in slopes:
         result = result * x 
    print("Trees encountered: " + str(result))
slopes = part1()
part2(slopes)



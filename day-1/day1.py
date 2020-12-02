def part1(): 
    with open("/Users/juiceppe/Documents/Development/AdventOfCode2020/day-1/inputs.txt", "r") as expenseReport:
        report = expenseReport.readlines()
        for i in report:
            for t in report:
                c = int(i) + int(t) 
                if c == 2020:
                    result = int(i) * int(t)
                    print(result)
part1()

def part2():
    with open("/Users/juiceppe/Documents/Development/AdventOfCode2020/day-1/inputs.txt", "r") as expenseReport:
        report = expenseReport.readlines()
        for i in report:
            for z in report:
                for t in report:
                    c = int(i) + int(t) + int(z)
                    if c == 2020:
                        result = int(i) * int(t) * int(z)
                        print(result)
part2()
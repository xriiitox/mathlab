import math
import sympy as sym
import random
import sys


def main():
    finalValue = []

    with open(sys.argv[1]) as file:
        operations = [line.rstrip() for line in file]

    if operations[0] != "!~mathlab":
        print("Not a valid !~mathlab file. Exiting...")
        return
    operations[0] = " "

    for op in operations:
        if op[0] in "0123456789":
            fullExp = []
            firstNum = []
            secondNum = []
            for char in op:
                if char in "0123456789" and "^" not in fullExp and "*" not in fullExp:
                    firstNum.append(char)
                    fullExp.append(char)
                elif char in "0123456789":
                    secondNum.append(char)
                    fullExp.append(char)
                elif char == "!":
                    firstNum = int("".join(firstNum))
                    finalValue.append(math.factorial(firstNum) % 127)
                    continue
                elif char == "^" or char == "*":
                    fullExp.append(char)
            if "^" in fullExp:
                fullExp[fullExp.index("^")] = "**"
                finalValue.append(eval("".join(fullExp)) % 127)
                continue
            elif "*" in fullExp:
                finalValue.append(eval("".join(fullExp)) % 127)
                continue
        else:
            global prevChar
            thingToDo = []
            num = []
            secondNum = []
            prevChar = ""
            prevPrevChar = ""
            thingToDone = False
            for char in op:
                if char not in "0123456789" and char != " " and not thingToDone:
                    thingToDo.append(char)
                    prevChar = char
                    continue
                if char == " ":
                    thingToDone = True
                    prevPrevChar = prevChar
                    prevChar = char
                    continue
                match "".join(thingToDo):
                    case "sqrt":
                        if char == ";":
                            finalValue.append(int(math.sqrt(int("".join(num)))) % 127)
                            continue
                        if char in "0123456789":
                            num.append(char)
                            continue
                    case "cbrt":
                        if char == ";":
                            finalValue.append(int(round(int("".join(num))**(1/3))) % 127)
                            continue
                        if char in "0123456789":
                            num.append(char)
                            continue
                    case "log":
                        if char == ";":
                            finalValue.append(int(math.log(int("".join(secondNum)), int("".join(num)))) % 127)
                            continue
                        elif secondNum:
                            secondNum.append(char)
                            prevChar = char
                            continue
                        elif prevChar == " " and prevPrevChar != "g":
                            secondNum.append(char)
                            prevChar = char
                            continue
                        elif char != " ":
                            num.append(char)
                            prevChar = char
                            continue
                        """
                        case "cos":
                            if char == ";":
                                finalValue.append(int(math.cos(int("".join(num)))) % 127)
                                continue
                            if char in "0123456789":
                                num.append(char)
                                continue
                        case "sin":
                            if char == ";":
                                finalValue.append(int(math.sin(int("".join(num)))) % 127)
                                continue
                            if char in "0123456789":
                                num.append(char)
                                continue
                        case "tan":
                            if char == ";":
                                finalValue.append(int(math.tan(int("".join(num)))) % 127)
                                continue
                            if char in "0123456789":
                                num.append(char)
                                continue
                            finalValue.append(int(math.tan(int("".join(num)))) % 127)
                        """
                    case "rand":
                        if char == ";":
                            finalValue.append(random.randint(0, 127))
                            continue
                    case "lim":
                        if char == ";":
                            x = 0
                            finalValue.append(int(sym.limit(x, x, int("".join(secondNum))) % 127))
                            continue
                        elif secondNum:
                            secondNum.append(char)
                            prevChar = char
                            continue
                        elif prevChar == " " and prevPrevChar != "m":
                            secondNum.append(char)
                            prevChar = char
                            continue
                        elif char != " ":
                            num.append(char)
                            prevChar = char
                            continue
    for value in finalValue:
        print(chr(value), end="")
    print()


if __name__ == '__main__':
    main()

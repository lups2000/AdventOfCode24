from collections import deque


def perform_instruction(instr, operand, registers):
    operands = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: registers['A'],
        5: registers['B'],
        6: registers['C'],
        7: None
    }

    if instr == 0:  # adv
        numerator = registers['A']
        denominator = 2 ** operands[operand]
        registers['A'] = numerator // denominator
    elif instr == 1:  # bxl
        registers['B'] = registers['B'] ^ operand
    elif instr == 2:  # bst
        registers['B'] = operands[operand] % 8
    elif instr == 3:  # jnz
        pass
    elif instr == 4:  # bxt
        registers['B'] = registers['B'] ^ registers['C']
    elif instr == 5:  # out
        return operands[operand] % 8
    elif instr == 6:  # bdv
        numerator = registers['A']
        denominator = 2 ** operands[operand]
        registers['B'] = numerator // denominator
    elif instr == 7:  # cdv
        numerator = registers['A']
        denominator = 2 ** operands[operand]
        registers['C'] = numerator // denominator
    return None


with open("./input.txt", "r") as fileToRead:
    registers = {'A': 0, 'B': 0, 'C': 0}
    program = []

    for line in fileToRead.readlines():
        line = line.strip()
        if "A" in line:
            registers['A'] = int(line[11:])
        elif "B" in line:
            registers['B'] = int(line[11:])
        elif "C" in line:
            registers['C'] = int(line[11:])
        elif "Program" in line:
            program = [int(el) for el in line[8:].split(",")]
 
    def find_A(program, ans):
        if not program:
            return ans
        for t in range(8):
            a = ans << 3 | t
            b = a % 8
            b = b ^ 1
            c = a >> b
            b = b ^ c
            b = b ^ 6
            if b % 8 == program[-1]:
                sub = find_A(program[:-1], a)
                if not sub:
                    continue
                return sub
            
    print(find_A(program, 0))
"""

Program: 2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0

- instr: 2 , operand: 4 (register A) --> modify register B
- instr: 1, operand: 1 -> modify register B
- instr: 7, operand: 5 (register B) -> modify register C
- instr: 4, operand: 0 -> modify register B
- instr: 0, operand: 3 -> modify register A
- instr: 1, operand: 6 -> modify register B
- instr: 5, operand: 5 (register B) -> print
- instr: 3, operand: 0 -> jump

this is repeated until A is 0

do:
    b = a % 8
    b = b ^ 1
    c = a // (2**b)
    b = b ^ c
    a = a // 8
    b = b ^ 6
    out(b % 8)
while A != 0

"""

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

i = 0
outputs = []
while i < len(program) - 1:
    instruction = program[i]
    operand = program[i + 1]
    res = perform_instruction(instruction, operand, registers)

    if res is not None:
        outputs.append(res)

    if instruction == 3 and registers['A'] != 0:
        i = operand
    else:
        i += 2

print(",".join(map(str, outputs)))

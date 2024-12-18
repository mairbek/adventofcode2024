import sys

def run(a, b, c, program):
    output = []
    ptr = 0
    def pow2(n):
        if n == 0:
            return 1
        return 2 << (n - 1)
    while True:
        if ptr < 0 or ptr >= len(program):
            break
        opcode = program[ptr]
        literal_op = program[ptr + 1]
        combo_op = literal_op
        # print("opcode = {}, literal_op = {}, combo_op = {}".format(opcode, literal_op, combo_op))
        if literal_op == 4:
            combo_op = a
        elif literal_op == 5:
            combo_op = b
        elif literal_op == 6:
            combo_op = c
        if opcode == 0:
            a = a // pow2(combo_op)
        elif opcode == 1:
            b = b ^ literal_op
        elif opcode == 2:
            b = combo_op % 8
        elif opcode == 3:
            if a > 0:
                ptr = literal_op
                # skip ptr += 2
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(combo_op % 8)
        elif opcode == 6:
            b = a // pow2(combo_op)
        elif opcode == 7:
            c = a // pow2(combo_op)
        ptr += 2
    # print("a = {}, b = {}, c = {}".format(a, b, c))
    return output

lines = sys.stdin.read().strip().split('\n')

a = b = c = None
program = []

for line in lines:
    line = line.strip()
    if line.startswith("Register A:"):
        # Extract the number after the colon and space
        a = int(line.split(":")[1].strip())
    elif line.startswith("Register B:"):
        b = int(line.split(":")[1].strip())
    elif line.startswith("Register C:"):
        c = int(line.split(":")[1].strip())
    elif line.startswith("Program:"):
        # Extract the sequence of integers
        prog_str = line.split(":", 1)[1].strip()
        program = list(map(int, prog_str.split(",")))

result = run(a, b, c, program)
print(','.join([str(i) for i in result]))

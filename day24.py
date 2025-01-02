import sys


class Node:
    def __init__(self, label, val, op, left, right):
        self.label = label
        self.val = val
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        if self.op:
            return f"{self.label} = {self.left} {self.op} {self.right}"
        return f"{self.label} {self.val}"

    def __repr__(self):
        return self.__str__()


nodes = {}
vals = True


def eval_node(node, nodes):
    if node.val is not None:
        return node.val
    left = eval_node(nodes[node.left], nodes)
    right = eval_node(nodes[node.right], nodes)
    val = None
    if node.op == "AND":
        val = left & right
    elif node.op == "OR":
        val = left | right
    elif node.op == "XOR":
        val = left ^ right
    else:
        raise ValueError(f"Unknown operator {node.op}")
    node.val = val
    return val


def parse_line(line: str) -> Node:
    expression, label = line.split("->")
    expression = expression.strip()
    label = label.strip()
    tokens = expression.split()
    left, op, right = tokens
    return Node(label, None, op, left, right)


for line in sys.stdin:
    ls = line.strip()
    if not ls:
        vals = False
        continue
    if vals:
        label, value = ls.split(":")
        nodes[label] = Node(label, int(value), None, None, None)
    else:
        node = parse_line(ls)
        nodes[node.label] = node

print(nodes)

i = 0
result = 0
base = 1
while True:
    znode = f"z{i:02d}"
    if znode not in nodes:
        break
    v = eval_node(nodes[znode], nodes)
    result += v * base
    base = base << 1
    i += 1
print(result)

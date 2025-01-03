import sys
from collections import defaultdict


class Node:
    def __init__(self, label, val, op, left, right):
        self.label = label
        self.autolabel = None
        self.child_labels = []
        self.child_ops = []
        self.val = val
        self.op = op
        self.left = left
        self.right = right
    
    def is_xy(self):
        return self.label[0] == "x" or self.label[0] == "y"

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


def eval_label(node, nodes):
    if node.val is not None:
        node.autolabel = node.label
        node.child_labels = [node.label]
        return node.label
    left = eval_label(nodes[node.left], nodes)
    right = eval_label(nodes[node.right], nodes)
    node.autolabel = f"{left} {node.op} {right}"
    node.child_labels = (
        [] + nodes[node.left].child_labels + nodes[node.right].child_labels
    )
    node.child_ops = [nodes[node.left].op, nodes[node.right].op]
    return node.autolabel


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

i = 0
while True:
    znode = f"z{i:02d}"
    if znode not in nodes:
        break
    v = eval_label(nodes[znode], nodes)
    i += 1
usage = defaultdict(set)

for n in nodes.values():
    if n.op is None:
        continue
    usage[n.left].add(n.op)
    usage[n.right].add(n.op)


errors = []
for n in nodes.values():
    if n.op is None:
        continue

    if n.left == "x00" or n.left == "y00" or n.right == "x00" or n.right == "y00":
        if (n.left[0] == "x" and n.right[0] == "y") or (
            n.left[0] == "y" and n.right[0] == "x"
        ):
            if n.op != "XOR" and n.op != "AND":
                errors.append(n.label)
        continue

    if n.op == "XOR":
        if n.left[0] == "x" or n.left[0] == "y":
            if n.right[0] != "x" and n.right[0] != "y":
                errors.append(n.label)
            if n.label[0] == "z":
                errors.append(n.label)
            if "AND" not in usage[n.label] or "XOR" not in usage[n.label]:
                errors.append(n.label)
        elif n.label[0] != "z":
            errors.append(n.label)

    elif n.op == "OR":
        if (
            n.left[0] == "x"
            or n.left[0] == "y"
            or n.right[0] == "x"
            or n.right[0] == "y"
            or n.label[0] == "z"
        ):
            errors.append(n.label)
        if "AND" not in usage[n.label] or "XOR" not in usage[n.label]:
            errors.append(n.label)

    elif n.op == "AND":
        if n.left[0] == "x" or n.left[0] == "y":
            if n.right[0] != "x" and n.right[0] != "y":
                errors.append(n.label)
        if "OR" not in usage[n.label]:
            errors.append(n.label)

errors = sorted(list(set(errors)))

for i in range(len(errors)):
    if i == len(errors) - 1:
        print(errors[i])
    else:
        print(errors[i], end=",")


# i = 0
# result = 0
# base = 1
# while True:
#     znode = f"z{i:02d}"
#     if znode not in nodes:
#         break
#     v = eval_node(nodes[znode], nodes)
#     result += v * base
#     base = base << 1
#     i += 1
# print(result)

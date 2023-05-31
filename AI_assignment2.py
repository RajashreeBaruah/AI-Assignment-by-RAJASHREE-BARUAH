import math

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def is_terminal(self):
        return not self.children

def build_game_tree(depth):
    if depth == 0:
        value = int(input("Enter leaf node value: "))
        return Node(value)

    value = int(input("Enter node value: "))
    node = Node(value)
    num_children = int(input("Enter the number of children for this node: "))
    for _ in range(num_children):
        child = build_game_tree(depth - 1)
        node.children.append(child)

    return node

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():  #Checks if the current node is a terminal node (i.e., game over)
        return node.value

    if maximizing_player:
        value = -math.inf
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        for child in node.children:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


depth = int(input("Enter the desired depth: "))
root = build_game_tree(depth)
alpha = -math.inf
beta = math.inf
maximizing_player = True

best_value = alpha_beta(root, depth, alpha, beta, maximizing_player)
print("Optimal value is:", best_value)
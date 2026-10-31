class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

treeA = Tree(1, Tree(2), Tree(3))

def total(tree):
    if tree is None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

treeB = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))

def print_tree(tree):
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)

'''
print_tree(treeA)
print()
print_tree(treeB)
'''

def print_tree_postorder(tree):
    if tree is None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=" ")

'''
print_tree_postorder(treeA)
print()
print_tree_postorder(treeB)
'''

def print_tree_inorder(tree):
    if tree is None: return
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)
#Omitted the use of parentheses (important for understanding in infix expression)

'''
print_tree_inorder(treeA)
print()
print_tree_inorder(treeB)
'''

def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

'''
print_tree_indented(treeA)
print()
print_tree_indented(treeB)
'''

# Sections 27.5 ans 27.6 explain how to parse infix expressions, 
# build the corresponding expression trees, and handle errors.

# 27.7. The animal tree:

def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    # Start with a singleton
    root = Tree("bird")

    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # Get new information
        prompt  = "What is the animal's name? "
        animal  = input(prompt)
        prompt  = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        # Add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)

animal()


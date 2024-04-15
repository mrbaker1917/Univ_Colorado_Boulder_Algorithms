# class for Red-Black Tree

def is_red(node):
    return node and node.color == 'red'

def is_black(node):
    return node and node.color == 'black'

def is_none(node):
    return node is None

def is_left(node):
    return node is node.parent.left
def insert_case1(node):
    if node.parent is None:
        node.color = 'black'
    else:
        insert_case2(node)

def insert_case2(node):
    if is_black(node.parent):
        return
    else:
        insert_case3(node)

def insert_case3(node):
    if is_red(node.uncle):
        node.parent.color = 'black'
        node.uncle.color = 'black'
        node.grandparent.color = 'red'
        insert_case1(node.grandparent)
    else:
        insert_case4(node)
def insert_case4(node):
    if node is node.parent.right and node.parent is node.grandparent.left:
        rotate_left(node.parent)
        node = node.left
    elif node is node.parent.left and node.parent is node.grandparent.right:
        rotate_right(node.parent)
        node = node.right
    insert_case5(node)

def insert_case5(node):
    node.parent.color = 'black'
    node.grandparent.color = 'red'
    if node is node.parent.left and node.parent is node.grandparent.left:
        rotate_right(node.grandparent)
    else:
        rotate_left(node.grandparent)
def rotate_right(node):
    pivot = node.left
    pivot.parent = node.parent
    if node.parent is None:
        root = pivot
    elif node is node.parent.left:
        node.parent.left = pivot
    else:
        node.parent.right = pivot
    node.left = pivot.right
    if pivot.right is not None:
        pivot.right.parent = node
    node.parent = pivot
    pivot.right = node

def rotate_left(node):  # symmetric to rotate_right function
    pivot = node.right
    pivot.parent = node.parent
    if node.parent is None:
        root = pivot
    elif node is node.parent.right:
        node.parent.right = pivot
    else:
        node.parent.left = pivot
    node.right = pivot.left
    if pivot.left is not None:
        pivot.left.parent = node
    node.parent = pivot
    pivot.left = node
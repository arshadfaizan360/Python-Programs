#[value,left_index,right_index]
tree = [[8,1,2],[3,3,4],[10,-1,5],[1,-1,-1],[6,6,7],[14,8,-1],[4,-1,-1],[7,-1,-1],[13,-1,-1]]


def inorder_traverse(tree,pointer):
  if tree[pointer][1] != -1:
    inorder_traverse(tree,tree[pointer][1])
  print(tree[pointer][0])
  if tree[pointer][2] != -1:
    inorder_traverse(tree,tree[pointer][2])

def preorder_traverse(tree,pointer):
  print(tree[pointer][0])
  if tree[pointer][1] != -1:
    preorder_traverse(tree,tree[pointer][1]) 
  if tree[pointer][2] != -1:
    preorder_traverse(tree,tree[pointer][2])

def postorder_traverse(tree,pointer):
  if tree[pointer][1] != -1:
    postorder_traverse(tree,tree[pointer][1]) 
  if tree[pointer][2] != -1:
    postorder_traverse(tree,tree[pointer][2])
  print(tree[pointer][0])

choice = '1'
while choice != '0':
  choice = input('''Choose an option:
                 
1. Preorder traversal
2. Inorder traversal
3. Postorder traversal
4. View tree
0. Exit
                 
''')
  print()
  if choice == '1':
    preorder_traverse(tree,0)
  elif choice == '2':
    inorder_traverse(tree,0)
  elif choice == '3':
    postorder_traverse(tree,0)
  elif choice == '4':
    print(tree)
  elif choice != '0':
    print('That is not a valid option')
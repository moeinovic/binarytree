from binarytree import Node

mio = Node(10)
mio.insert(5)
mio.insert(15)
mio.insert(2)
mio.insert(13)
mio.insert(22)
mio.insert(1)
mio.insert(14)
mio.insert(4)
mio.insert(12)
mio.insert(21)
mio.insert(3)

#prettyprint
mio.prettyPrint(1)

#get height
print(mio.getHeight())

#get size
print(mio.getSize())

#find
print(mio.find(10))

#inorder print
mio.inorder()

#get minimum
print(mio.getMin())

#get maximum
print(mio.getMax())

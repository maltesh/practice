class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    ct = 0
    while True :
        if node :
            ct = ct+1
            node = node.next       
        else:
            break
    return ct
  
def count(node, data):
    ct = 0
    while True :
        if node :
            if node.data == data:
            ct = ct+1
            node = node.next       
        else:
            break
    return ct



import unittest

class LinkCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(length(None), 0, "Length of null list should be zero.")
        
        print length(Node(99)), ' --->>'
        self.assertEqual(length(Node(99)), 1, "Length of null list should be zero.")
        

if __name__ == '__main__':
    unittest.main()


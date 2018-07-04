# http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree/train/python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    if head is None:
        nd = Node(data)
        return nd
    nd = Node(data)
    
    if head.data > data:
        nd.next  = head 
        return nd
    nd.next = head
    return nd


  
def build_one_two_three():
    return push(push(push(None,3),2),1)


if __name__ == '__main__':
   t = build_one_two_three()
   print t.data
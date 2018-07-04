# https://www.codewars.com/kata/linked-lists-sorted-insert/train/python



class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    if head is None:
        head = Node(data)
        return head
    else:
        if head.data > data:
            new_nd = Node(data)
            new_nd.next = head
            return new_nd
        head.next  = sorted_insert(head.next,data)
        return head

    # def recur(node, data):
    #         if not node:
    #             return Node(data)
    #         if node.data > data:
    #             node_new = Node(data)
    #             node_new.next = node
    #             return node_new
    #         node.next = recur(node.next, data)
    #         return node

    return recur(head, data)

if __name__ == '__main__':
    head = Node(1)
    t =  sorted_insert(head,0.5)
    print t.data,  t.next.next


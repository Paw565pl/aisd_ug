class Node:
    def __init__(self, x):
        self.key = x
        self.next = None
        self.prev = None


# lista dwukierunkowa cykliczna z wartownikiem
class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def wstaw(self, *args):
        nodes = reversed([Node(arg) for arg in args])

        for x in nodes:
            x.next = self.head.next
            x.prev = self.head
            self.head.next.prev = x
            self.head.next = x

    def drukuj(self):
        x = self.head.next

        nodes = []
        while x is not self.head:
            nodes.append(x.key)
            x = x.next
        print(nodes)

    def szukaj(self, k):
        x = self.head.next
        while x is not self.head and x.key != k:
            x = x.next
        return x

    def usuń(self, x):
        if x is not self.head:
            x.prev.next = x.next
            x.next.prev = x.prev

    def bezpowtorzeń(self):
        start = self.head.next

        unique = []
        while start is not self.head:
            if start.key not in unique:
                unique.append(start.key)
            start = start.next

        new_list = LinkedList()
        new_list.wstaw(*unique)
        return new_list

    def scal(self, other_list):
        # start_self = self.head.next
        # items_self = []
        # while start_self is not self.head:
        #     items_self.append(start_self.key)
        #     start_self = start_self.next
        #
        # start_other_list = other_list.head.next
        # items_other_list = []
        # while start_other_list is not other_list.head:
        #     items_other_list.append(start_other_list.key)
        #     start_other_list = start_other_list.next
        #
        # list_sum = items_self + items_other_list
        # new_list = LinkedList()
        # new_list.wstaw(*list_sum)
        # return new_list

        self.head.prev.next = other_list.head.next
        other_list.head.next.prev = self.head.prev
        self.head.prev = other_list.head.prev
        other_list.head.prev.next = self.head
        other_list.head = Node(None)
        return self


l = LinkedList()
l.wstaw("abc", "def", "c")
l.wstaw("def")
l.drukuj()
l.usuń(l.szukaj("def"))
l.drukuj()
l.wstaw("abc", "def", "bc", "bc", "c")
l.drukuj()
l.bezpowtorzeń().drukuj()

print("")

l1 = LinkedList()
l1.wstaw("a", "aa", "aa", "a")
l1.drukuj()

l2 = LinkedList()
l2.wstaw("b")
l2.wstaw("ab")
l2.wstaw("b")
l2.wstaw("c", "cc", "abc")
l2.drukuj()

l3 = l1.scal(l2)
l3.drukuj()

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
    def __str__(self):
        return "(val:" + str(self.x) + " random:" + self.random.__str__() + " next:" + self.next.__str__() + ")"

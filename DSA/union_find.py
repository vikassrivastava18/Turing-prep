# Implement Union Find
class QuickFindUF:
    """
    Save all objects as indexes from 0 to n - 1
    Perform the Union and Find operation
    """
    def __init__(self, n):
        self.ids = [i for i in range(n)]

    def find(self, p, q):
        # Return True if ID of p is same as q
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        id_p = self.ids[p]
        id_q = self.ids[q]
        # Update one component with all it's elements pointing to other components ID
        for i in range(len(self.ids)):
            if self.ids[i] == p:
                self.ids[i] = q


class QuickUnionUF:
    """
        Save all objects as indexes from 0 to n - 1
        Keep track of the root object, all objects point to a root object
        For Union of (p, q), set the id of p's root same as q's root
        For Find of (p, q), check if p and q have the same root
    """

    def __init__(self, n):
        self.ids = [i for i in range(n)]

    def root(self, p):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    def find(self, p, q):
        return self.root(p)== self.root(q)

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)
        self.ids[root_p] = root_q                


class QuickWeightedUF:
    """
        Add size of component to modify the root of smaller component to point
        to larger component
    """

    def __init__(self, n) -> None:
       self.ids = [i for i in range(n)]
       self.size = [1 for i in range(n)]

    def root(self, p):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    def find(self, p, q):
        return self.root(p)== self.root(q)

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)

        if self.size[p] < self.size[q]:
            self.ids[root_p] = root_q
            self.size[root_q] += self.size[root_p]

        else:
            self.ids[root_q] = root_p
            self.size[root_p] += self.size[root_q]

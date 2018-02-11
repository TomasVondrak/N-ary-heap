"""N-ary heap implementation."""


class NHeap(object):
    """Represents a maximum n-ary heap."""

    def __init__(self, n = 2, hl=None):
        """
        Build heap from list. O(n).
        Items must be iterable, n must be positive integer.    
        """
        if n < 1 or not isinstance(n, int):
            raise ValueError("n must be integer >= 1")
        self._n = n
        self._hl = hl

    def get_parent(self, index):
        """Returns the parent index of a member, which index was given"""
        return (index - 1) // self._n

    def get_children(self, index):
        """Returns all child of a given index"""
        first_child = index * self._n + 1
        return range(first_child, min(first_child + self._n, len(self._hl)))

    def increase_key(self, index):
        """In O(log n)"""
        current = self._hl[index]
        while index >= 0: #stop when index is 0 (index is the root)
            parent_index = self.get_parent(index)
            parent = self._hl[parent_index]
            if parent > current:
                return
            self._hl[parent_index], self._hl[index], index = current, parent, parent_index

    def _heapify(self, index):
        current = self._hl[index]
        while True:
            children = tuple((self._hl[x], x) for x in self.get_children(index))
            if not children:
                return #This is the end, we are done
            candidate, candidate_index = max(children)
            if current > candidate:
                return
            self._hl[candidate_index], self._hl[index], index = current, candidate, candidate_index
        
    def get_max(self):
        """Get maximum item, do not remove it. O(1)."""
        return self._hl[0]

    def extract_max(self):
        """Get maximum item and remove it. O(n)."""
        result, self._hl[0] = self._hl[0], self._hl[-1]
        if self._hl:
            self._heapify(0)
        return result

    def insert(self, value):
        """Insert new item into heap. O(log n)."""
        self._hl.append(value)
        self.increase_key(len(self._hl) - 1)
        pass

    def size(self):
        """Get size of heap. O(1)."""
        return len(self._hl)

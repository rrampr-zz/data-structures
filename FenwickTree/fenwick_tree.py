from typing import Iterable, TypeVar, Callable

T = TypeVar('T')

"""
Traditionally Fenwick Trees operate on arrays of integers. They were concieved for the purposes of supporting two operations
efficiently:
1) Sum up the first k elements in the array
2) Add a value x to the kth element in the array

In a traditional array A, 1) would take O(n) time and 2) would take O(1) time.
If you were to transform the array  A into a cumulative sum array B, 1) would take O(1) time
but 2) would take O(n) time as you need to update all cumulative sums containing the updated element.

The Fenwick tree meets halfway between both approaches and supports 1) and 2) in O(log n) time. It is should ideally be used when you envision
a sequence of elements and you have a lot sum queries and a lot of update queries.

While traditionally Fenwick Trees operate on arrays of integers and sums, the data structure below
is abstract enough to be used for any iterable of any type T (other than integer) w/ an associative binary operation  (that represents +)
"""
class FenwickTree:
    def __init__(self, a: Iterable[T], op: Callable[[T, T], T], identity: T) -> None:
        """
            Args:
            param1: a is an iterable of any type.
            param2: op is an associative binary operator with identity on T.
            param3: identity is the identity of T under the operation op

            To be concise (T, op) form a monoid

            Returns:
            None. This is a constructor for a fenwick tree

            Raises: Does not throw an exception

            Time complexity: O(nlogn) for constructing this data structure
        """
        self.a = list(a)
        self.op = op
        self.identity = identity
        self.f_tree = [identity] * (len(a) + 1)
        for i, elem in enumerate(a):
            self.update(i, elem)


    def reduce(self, i : int) -> T:
        """
            Args:
            param1: i is an index of the sequence 'a' used to construct the fenwick tree.
            Returns:
            result represents reducing the subsequence a[:i] under the binary operator op

            Raises: Throws a ValueError exception if an invalid index is passed

            Time Complexity : O(log n) where n is the number of elements in a
        """
        if i >= len(self.a) or i < 0:
            raise ValueError("Invalid index operation")
        index = i + 1
        result = self.identity
        while index > 0:
            ## Get rid of the least significant bit
            result = self.op(result, self.f_tree[index])
            index = index - (index & -index)
        return result

    def update(self, i: int, val: T) -> None:
        """
            Args:
            param1: i is an index of the sequence 'a' used to construct the fenwick tree.

            Returns: None

            Effects:
            Effectively equivalent to doing a[i] = op(a[i], val)

            Time Complexity : O(log n) where n is the number of elements in a

            Raises: Throws a ValueError exception if an invalid index is passed
        """
        if i >= len(self.a) or i < 0:
            raise ValueError("Invalid index operation")
        index = i + 1
        while index <= len(self.f_tree):
            self.f_tree[index] = self.op(self.f_tree[index], val)
            index += (index & -index)
        return

if __name__ == '__main__':
    a = FenwickTree([1,2,3,4,5,6], lambda x, y: x + y, 0)
    print(a.reduce(2))
    print(a.reduce(0))
    a.update(3, 100)
    print(a.reduce(3))

from typing import Any, Iterator

from .errors import PopError
from .node import Node


class List:
    '''Linked list.'''

    def __init__(self, *args) -> None:
        '''
        init.

        :param args: list of object to initialize list.
        '''
        self._iterator_index = -1
        self._length = 0
        self.root = None
        self.tail = None
        for arg in args:
            self.push_back(arg)

    def push_back(self, data: Any) -> None:
        '''
        Add element at the end of the list

        :param data: data to insert
        :return: None
        '''
        if self.root:
            last_item = self.tail
            last_item.next = Node(data)
            self.tail = last_item.next
        else:
            self._init(data)
        self._length += 1

    def push_front(self, data: Any) -> None:
        '''
        Add element at the beginning of the list.

        :param data: data to insert
        :return: None
        '''
        if not self.root:
            self._init(data)
        else:
            new_item = Node(data, self.root)
            self.root = new_item
        self._length += 1

    def pop_back(self) -> None:
        '''
        Delete last element.

        :return: None
        :raises PopError: if list is empty
        '''
        if self._length == 0:
            raise PopError('Pop from empty list')
        del self[self._length - 1]

    def pop_front(self) -> None:
        '''
        Delete first element.

        :return: None
        :raises PopError: if list is empty
        '''
        if self._length == 0:
            raise PopError('Pop from empty list')
        del self[0]

    def insert(self, data: Any, index=None) -> None:
        '''
        Insert new element at ``index``.

        :param data: data to insert
        :param index: index at which position to insert
        :return: None
        '''
        if index is None:
            return self.push_back(data)
        if index == 0:
            return self.push_front(data)

        self._check_index(index)

        next_item = self._get_node(index)
        prev_item = self._get_node(index - 1)
        prev_item.next = Node(data, next_item)
        self._length += 1

    def at(self, index: int) -> Any:
        '''
        Get element at ``index``.

        :param index: index of an element to get
        :return: data at given index
        '''
        return self[index]

    def remove(self, index: int) -> None:
        '''
        Delete element at ``index``

        :param index: index of an element to delete
        :return: None
        '''
        del self[index]

    def get_size(self) -> int:
        '''
        Get size of the list.

        :return: size of the list.
        '''
        return len(self)

    def clear(self) -> None:
        '''
        Clear the list

        :return: None
        '''
        self.root = None
        self.tail = None
        self._length = 0

    def set(self, data: Any, index: int) -> None:
        '''
        Set value of an element at ``index`` to ``data``.

        :param index: index of an element to change
        :param data: data to replace element with
        :return: None
        '''
        self._check_index(index)
        self._get_node(index).data = data

    def is_empty(self) -> bool:
        '''
        Get if list is empty.

        :return: bool: weather list empty or not
        '''
        return self._length == 0

    def push_front_list(self, other: 'List') -> None:
        '''
        Add data from ``other`` in the beginning of the list.

        If called like so::

            x = List(5, 6, 7).push_front_list(List(1, 2, 3, 4))

        Should act like this::

            x = List(1, 2, 3, 4, 5, 6, 7)

        :param other: other list from which to take data to insert
        :return: None
        '''
        for item in tuple(other)[::-1]:
            self.push_front(item)

    def __delitem__(self, index) -> None:
        '''delitem implementation.'''
        self._check_index(index)
        if self._length == 1:  # one element
            to_del = self.root
            self.root = None
            self.tail = None
        elif index == self._length - 1:  # last element
            to_del = self.tail
            self.tail = self._get_node(self._length - 2)
            self.tail.next = None
        elif index == 0:  # first element
            to_del = self.root
            new_root = self.root.next
            self.root = new_root
        else:  # middle element
            to_del = self._get_node(index)
            prev_item = self._get_node(index - 1)
            next_item = self._get_node(index + 1)
            prev_item.next = next_item
        self._length -= 1
        to_del.next = None
        return to_del.data

    def __len__(self) -> int:
        '''len implementation.'''
        return self._length

    def __getitem__(self, index: int) -> Any:
        '''getitem implementation.'''
        return self._get_node(index).data

    def __str__(self) -> str:
        '''str implementation.'''
        result = f'List({", ".join(str(item) for item in self)})'
        return result

    def __iter__(self) -> Iterator:
        '''iter implementation.'''
        return self

    def __next__(self) -> Any:
        '''next implementation.'''
        self._iterator_index += 1
        if self._iterator_index >= len(self):
            self._iterator_index = -1
            raise StopIteration
        else:
            return self[self._iterator_index]

    def _init(self, data: Any) -> None:
        '''
        Initialize empty list with given ``data``.

        :param data: data with which initialize list
        :return: None
        '''
        self.root = Node(data)
        self.tail = self.root

    def _check_index(self, index: int) -> None:
        '''
        Check if given ``index`` is valid.

        Checks if index is within the (0; len(self) -1) boundaries
        and type of index is int.

        :param index: index to check
        :return: None
        :raises TypeError: if index is not an int
        :raises IndexError: if index is out of range
        '''
        if not isinstance(index, int):
            raise TypeError('List index must be an integer')
        if index >= len(self) or index < 0:
            raise IndexError('List index out of range')

    def _get_node(self, index: int) -> Node:
        '''
        Get a list node at ``index``.

        :param index: index of node to get
        :return: Node at index within the list
        '''
        self._check_index(index)
        item = self.root
        for i in range(0, index):
            item = item.next
        return item

    def __manual_len(self) -> int:
        size = 0
        node = self.root
        while node:
            node = node.next
            size += 1
        return size

from typing import Any


class Node:
    '''Node of the liked list.'''

    def __init__(self, data: Any, next_: 'Node' = None) -> None:
        '''
        init.

        :param data: data of the node
        :param next_: reference to the next node
        '''
        self.data = data
        self.next = next_

    def __str__(self) -> str:
        '''str.'''
        return str(self.data)

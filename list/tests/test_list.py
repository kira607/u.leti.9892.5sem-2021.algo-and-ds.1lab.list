import pytest

from list import List, PopError


@pytest.mark.parametrize(
    'test_data',
    (
        (1, 2, 3),
        ('a', 'b', 'c'),
        (List(List(), List(1, 3)), (1, [9, 2]), ['hello', {1: '404'}]),
        (),
    )
)
def test_list_init(test_data: tuple):
    '''Test if init handles argument properly.'''
    list_ = List(*test_data)
    assert len(list_) == len(test_data)
    assert tuple(list_) == test_data


@pytest.mark.parametrize(
    'initial_list,insert_item,expected_list',
    (
        ((1, 2, 3), 4, (1, 2, 3, 4)),
        (('a', 'b', 'c'), 'd', ('a', 'b', 'c', 'd')),
        (
            (0, (1, [9, 2]), ['hello', {1: '404'}]),
            {'xyz': 't'},
            (0, (1, [9, 2]), ['hello', {1: '404'}], {'xyz': 't'}),
        ),
        ((), 'new', ('new',)),
    ),
)
def test_list_push_back(initial_list, insert_item, expected_list):
    list_ = List(*initial_list)
    list_.push_back(insert_item)
    assert tuple(list_) == expected_list


@pytest.mark.parametrize(
    'initial_list,insert_item,expected_list',
    (
        ((1, 2, 3), 0, (0, 1, 2, 3)),
        (('a', 'b', 'c'), 'z', ('z', 'a', 'b', 'c')),
        (
            (0, (1, [9, 2]), ['hello', {1: '404'}]),
            {'xyz': 't'},
            ({'xyz': 't'}, 0, (1, [9, 2]), ['hello', {1: '404'}]),
        ),
        ((), 'new', ('new',)),
    ),
)
def test_list_push_front(initial_list, insert_item, expected_list):
    list_ = List(*initial_list)
    list_.push_front(insert_item)
    assert tuple(list_) == expected_list


@pytest.mark.parametrize(
    'initial_list,expected_list',
    (
        ((1, 2, 3), (1, 2)),
        (('a', 'b', 'c'), ('a', 'b')),
        ((0, (1, [9, 2]), ['hello', {1: '404'}]), (0, (1, [9, 2]))),
        (('new',), ()),
    ),
)
def test_list_pop_back(initial_list, expected_list):
    list_ = List(*initial_list)
    list_.pop_back()
    assert tuple(list_) == expected_list


def test_list_pop_back_with_exception():
    with pytest.raises(PopError):
        List().pop_back()


@pytest.mark.parametrize(
    'initial_list,expected_list',
    (
        ((1, 2, 3), (2, 3)),
        (('a', 'b', 'c'), ('b', 'c')),
        ((0, (1, [9, 2]), ['hello', {1: '404'}]), ((1, [9, 2]), ['hello', {1: '404'}])),
        (('new',), ()),
    ),
)
def test_list_pop_front(initial_list, expected_list):
    list_ = List(*initial_list)
    list_.pop_front()
    assert tuple(list_) == expected_list


def test_list_pop_front_with_exception():
    with pytest.raises(PopError):
        List().pop_front()


@pytest.mark.parametrize(
    'initial_list,insert_item,insert_pos,expected_list',
    (
        ((1, 2, 3), 0, 0, (0, 1, 2, 3)),
        (('a', 'b', 'c'), 'z', 2, ('a', 'b', 'z', 'c')),
        (
            (0, (1, [9, 2]), ['hello', {1: '404'}]),
            {'xyz': 't'},
            1,
            (0, {'xyz': 't'}, (1, [9, 2]), ['hello', {1: '404'}]),
        ),
        ((), 'new', 0, ('new',)),
    ),
)
def test_list_insert(initial_list, insert_item, insert_pos, expected_list):
    list_ = List(*initial_list)
    list_.insert(insert_item, insert_pos)
    assert tuple(list_) == expected_list


@pytest.mark.parametrize(
    'initial_list,insert_item,insert_pos,exception',
    (
        ((1, 2, 3), 0, 3, IndexError),
        (('a', 'b', 'c'), 'z', -1, IndexError),
        ((0, (1, [9, 2]), ['hello', {1: '404'}]), {'xyz': 't'}, '1', TypeError),
        ((), 'new', 1, IndexError),
    ),
)
def test_list_insert_with_exception(
    initial_list,
    insert_item,
    insert_pos,
    exception,
) -> None:
    with pytest.raises(exception):
        List(*initial_list).insert(insert_item, insert_pos)


@pytest.mark.parametrize(
    'list_, index, expected_value',
    (
        (List(1, 2, 3), 0, 1),
        (List('a', 'b', 'c'), 2, 'c'),
        (List(0, (1, [9, 2]), ['hello', {1: '404'}]), 1, (1, [9, 2])),
    ),
)
def test_list_at(list_, index, expected_value):
    assert list_.at(index) == expected_value


@pytest.mark.parametrize(
    'list_, index, exception',
    (
        (List(1, 2, 3), [0], TypeError),
        (List('a', 'b', 'c'), 200, IndexError),
        (List(0, (1, [9, 2]), ['hello', {1: '404'}]), -1, IndexError),
        (List(), 0, IndexError),
    ),
)
def test_list_at_with_exception(list_, index, exception):
    with pytest.raises(exception):
        list_.at(index)


@pytest.mark.parametrize(
    'list_, index, expected_list',
    (
        (List(1, 2, 3), 0, (2, 3)),
        (List('a', 'b', 'c'), 2, ('a', 'b')),
        (
            List(0, (1, [9, 2]), ['hello', {1: '404'}]),
            1,
            (0, ['hello', {1: '404'}]),
        ),
    ),
)
def test_list_remove(list_, index, expected_list):
    list_.remove(index)
    assert tuple(list_) == expected_list


@pytest.mark.parametrize(
    'list_, index, exception',
    (
        (List(1, 2, 3), [0], TypeError),
        (List('a', 'b', 'c'), 200, IndexError),
        (List(0, (1, [9, 2]), ['hello', {1: '404'}]), -1, IndexError),
        (List(), 0, IndexError),
    ),
)
def test_list_remove_with_exception(list_, index, exception):
    with pytest.raises(exception):
        list_.remove(index)


@pytest.mark.parametrize(
    'list_, expected_len',
    (
        (List(1, 2, 3), 3),
        (List('a', 'b', 'c'), 3),
        (List(0, (1, [9, 2]), ['hello', {1: '404'}], -1, IndexError), 5),
        (List(), 0),
        (List(*(i for i in range(1000))), 1000),
    ),
)
def test_list_get_size(list_, expected_len):
    assert len(list_) == list_.get_size() == list_._length == expected_len


@pytest.mark.parametrize(
    'list_',
    (
        (List(1, 2, 3)),
        (List('a', 'b', 'c')),
        (List(0, (1, [9, 2]), ['hello', {1: '404'}], -1, IndexError)),
        (List()),
        (List(*(i for i in range(1000)))),
    ),
)
def test_list_clear(list_):
    list_.clear()
    assert list_.root is None
    assert list_.tail is None
    assert list_.get_size() == 0


@pytest.mark.parametrize(
    'list_, index, data',
    (
        (List(1, 2, 3), 0, 'hello'),
        (List('a', 'b', 'c'), 2, 'world'),
        (List(0, (1, [9, 2]), ['hello', {1: '404'}], -1, IndexError), 2, 0),
    ),
)
def test_list_set(list_, index, data):
    list_.set(data, index)
    assert list_.at(index) == data


@pytest.mark.parametrize(
    'list_, index, exception',
    (
        (List(1, 2, 3), [0], TypeError),
        (List('a', 'b', 'c'), 200, IndexError),
        (List(0, (1, [9, 2]), ['hello', {1: '404'}]), -1, IndexError),
        (List(), 0, IndexError),
    ),
)
def test_list_set_with_exception(list_, index, exception):
    mock_data = ''
    with pytest.raises(exception):
        list_.set(mock_data, index)


@pytest.mark.parametrize(
    'list_, is_empty',
    (
        (List(1, 2, 3), False),
        (List('a', 'b', 'c'), False),
        (List(0, (1, [9, 2]), ['hello', {1: '404'}], -1, IndexError), False),
        (List(), True),
        (List(*(i for i in range(1000))), False),
    ),
)
def test_list_is_empty(list_, is_empty):
    assert list_.is_empty() == is_empty


@pytest.mark.parametrize(
    'list_, other, result',
    (
        (List(1, 2, 3), List(4, 5, 6), (4, 5, 6, 1, 2, 3)),
        (List('a', 'b', 'c'), List('d'), ('d', 'a', 'b', 'c')),
        (List(), List(), ()),
        (List(3, 4, 5), List(), (3, 4, 5)),
        (List(), List(3, 4, 5), (3, 4, 5)),
    ),
)
def test_list_push_front_list(list_, other, result):
    list_.push_front_list(other)
    assert tuple(list_) == result
from list import List


def main():
    list1 = List(1, 2, 3, 4, {5: 6}, [7, 8], (9,), '10')
    list2 = List()
    print(list1)
    print(list2)
    print(f'{list1.at(0)=}')

    try:
        print(list2.at(0))
    except IndexError:
        print('print(list.at(0)) raised IndexError')

    for index, elem in enumerate(list1):
        print(f'[{index}]: {elem}')


if __name__ == '__main__':
    main()
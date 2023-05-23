class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: следующий обьект стека
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f'{self.__class__.__name__}{self.data,self.next_node}'


class Stack():
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.stack = []
        self.top = object

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    def __str__(self):
        return f'Стак данных'


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """
        try:
            object = Node(data, self.stack[-1])
        except IndexError:
            object = Node(data, None)
        self.stack.append(object)
        self.top = object

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """

        if len(self.stack) == 1:
            self.top = None
        else:
            self.top = self.stack[-2]
        return self.stack.pop(-1).data

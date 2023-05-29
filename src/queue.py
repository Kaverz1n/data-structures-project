class Node:
    """Класс для узла очереди"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f'{self.__class__.__name__}{self.data, self.next_node}'


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.queue = []
        self.head = None
        self.tail = None

    def __str__(self):
        if len(self.queue) > 0:
            elements = [i.data for i in self.queue]
            return '\n'.join(elements)
        else:
            return ''

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if len(self.queue) >= 1:
            obj = Node(data)
            self.tail = obj
            self.queue[-1].next_node = obj
            self.queue.append(obj)
        else:
            obj = Node(data)
            self.tail = obj
            self.head = obj
            self.queue.append(obj)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента или None
        """
        if len(self.queue) > 1:
            self.head = self.head.next_node
        elif len(self.queue) == 1:
            self.head = None
            self.tail = None
        else:
            return None

        return self.queue.pop(0).data

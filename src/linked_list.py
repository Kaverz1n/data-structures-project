class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"

    def __str__(self):
        return 'Узел односвязного списка'


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.linked_list = []
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        object_ = Node(data)
        if len(self.linked_list) == 0:
            self.head = object_
            self.tail = object_
        else:
            self.head = object_
            object_.next_node = self.linked_list[0]

        self.linked_list.insert(0, object_)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        object_ = Node(data)
        if len(self.linked_list) == 0:
            self.head = object_
            self.tail = object_
        else:
            self.tail = object_
            self.linked_list[-1].next_node = object_

        self.linked_list.append(object_)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

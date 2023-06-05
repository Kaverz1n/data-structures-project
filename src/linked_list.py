class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict):
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

    def to_list(self) -> list:
        '''
        Вовзаращает все данные, которые содержатся
        в односвязном списке
        '''
        data_list = []
        for node in self.linked_list:
            data_list.append(node.data)
        return data_list

    def get_data_by_id(self, value) -> dict:
        '''
        Возвращает словарь с данными, значения ключа "id"
        которого равно переданному значению в фукнкцию
        '''
        data_list = self.to_list()
        for data in data_list:
            try:
                if data['id'] == value:
                    return data
            except:
                print('Данные не являются словарем или в словаре нет id.')

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

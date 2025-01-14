import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'Файл item.csv поврежден'

class CSVNotFoundError(InstantiateCSVError):
    def __init__(self):
        self.message = 'Файл отсутствует'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return int(self.quantity) + int(other.quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise Exception('Наименование товара превышает 10 символов.')
        self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_csv(cls, filename) -> None:
        """Вызываем классы из файла"""

        try:
            cls.all.clear()

            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])

                    if not row['name']:
                        raise InstantiateCSVError
                    if not row['price']:
                        raise InstantiateCSVError
                    if not row['quantity']:
                        raise InstantiateCSVError
        # Обработка ошибки файл не найден
        except FileNotFoundError:
            raise CSVNotFoundError
        # Обработка ошибки файл поврежден
        except KeyError:
            raise InstantiateCSVError

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Инициализирует экземпляр класса ITEM"""

        address_file = '../src/items.csv'
        try:
            cls.instantiate_csv(address_file)
        except CSVNotFoundError as ex:
            print(ex.message)
        except InstantiateCSVError as ex:
            print(ex.message)

    @staticmethod
    def string_to_number(num):
        numb = float(num)
        return int(numb)

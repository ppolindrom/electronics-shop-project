"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_item():
    # пример товаров для тестирования
    item1 = Item('Молоко', 50.0, 3)
    item2 = Item('Хлеб', 30.0, 5)

    # Тест метода calculate_total_price()
    assert item1.calculate_total_price() == 150.0
    assert item2.calculate_total_price() == 150.0

    # Тест метода apply_discount()
    item1.pay_rate = 10.0
    item1.apply_discount()
    assert item1.price == 45.0

    item2.pay_rate = 20.0
    item2.apply_discount()
    assert item2.price == 24.0

    # Тест переменной all
    assert Item.all == [item1, item2]

def test_instantiate_from_csv():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

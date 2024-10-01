import random


# Задание списка продуктов
products = [
    "Яблоко", "Банан", "Апельсин", "Виноград", "Клубника", "Черника", "Манго", "Ананас", "Персик", "Арбуз",
    "Огурец", "Помидор", "Морковь", "Брокколи", "Картофель", "Лук", "Чеснок", "Болгарский перец", "Шпинат", "Салат",
    "Молоко", "Яйца", "Сыр", "Йогурт", "Масло", "Сливки", "Творог", "Сметана", "Мороженое", "Взбитые сливки",
    "Хлеб", "Рис", "Паста", "Овсянка", "Каша", "Мука", "Сахар", "Соль", "Перец", "Оливковое масло",
    "Курица", "Говядина", "Свинина", "Рыба", "Креветки", "Индейка", "Бекон", "Ветчина", "Колбаса", "Стейк",
    "Арахисовое масло", "Миндальное масло", "Джем", "Мёд", "Кленовый сироп", "Кетчуп", "Горчица", "Майонез", "Соевый соус", "Уксус",
    "Печенье", "Чипсы", "Сухари", "Попкорн", "Пряники", "Шоколад", "Конфеты", "Орехи", "Сухофрукты", "Мюсли батончики",
    "Яблочный сок", "Апельсиновый сок", "Виноградный сок", "Лимонад", "Газировка", "Вода", "Чай", "Кофе", "Энергетический напиток", "Спортивный напиток",
    "Консервированная фасоль", "Консервированная кукуруза", "Консервированный горошек", "Консервированные помидоры", "Консервированный ананас", "Консервированный тунец", "Консервированный лосось", "Консервированная курица", "Консервированный суп", "Консервированный бульон",
    "Замороженная пицца", "Замороженные овощи", "Замороженные фрукты", "Замороженные блюда", "Замороженные вафли", "Замороженный картофель фри", "Замороженные котлеты", "Замороженные рыбные палочки", "Замороженные куриные наггетсы", "Замороженный йогурт",
    "Спагетти", "Макароны", "Лазанья", "Рамен", "Лапша", "Киноа", "Кускус", "Ячмень", "Полента", "Тортильи",
    "Пищевая сода", "Разрыхлитель", "Дрожжи", "Корица", "Мускатный орех", "Паприка", "Перец чили", "Тмин", "Орегано", "Базилик",
    "Шампунь", "Кондиционер", "Мыло", "Зубная паста", "Туалетная бумага", "Бумажные полотенца", "Алюминиевая фольга", "Пищевая плёнка", "Стиральный порошок", "Средство для мытья посуды",
    "Губки", "Мешки для мусора", "Пакеты на застёжке", "Лампочки"
]; products = sorted(products)


# Функция генерации случайных цен
def generate_random_prices():
    return [random.randint(50, 500) for _ in range(len(products))]


# Создание списков для магазинов с ценами
magnit_pl = generate_random_prices(); magnit_pl = list(zip(products, magnit_pl))
monetka_pl = generate_random_prices(); monetka_pl = list(zip(products, monetka_pl))
vkusvill_pl = generate_random_prices(); vkusvill_pl = list(zip(products, vkusvill_pl))


# Ввод товаров от пользователя
products_from_user = input('Введите товары ==> ').split(", ")
products_from_user = [product.strip() for product in products_from_user]  


def calculate_cost(store_prices, products_from_user):
    total_cost = 0
    for user_product in products_from_user:
        for item in store_prices:
            if item[0].lower() == user_product.lower():  
                total_cost += item[1]
                break
    return total_cost


magnit_total = calculate_cost(magnit_pl, products_from_user)
monetka_total = calculate_cost(monetka_pl, products_from_user)
vkusvill_total = calculate_cost(vkusvill_pl, products_from_user)


print(f"Магнит: {magnit_total} рублей")
print(f"Монетка: {monetka_total} рублей")
print(f"Вкусвилл: {vkusvill_total} рублей")


def find_best_store(store_totals):
    best_store = store_totals[0] 
    for store in store_totals:
        if store[1] < best_store[1]: 
            best_store = store
    return best_store


store_totals = [("Магнит", magnit_total), ("Монетка", monetka_total), ("Вкусвилл", vkusvill_total)]


best_store = find_best_store(store_totals)
print(f"\nЛучшее предложение в {best_store[0]}, итоговая цена {best_store[1]} рублей.")
from collections import deque


def is_palindrome(s):
    """
    Перевіряє, чи є рядок паліндромом, ігноруючи регістр та пробіли.
    """
    string_deque = deque()

    # Видаляємо пробіли та змінюємо регістр
    formatted_string = "".join(ch.lower() for ch in s if ch.isalnum())

    # Додаємо символи до двосторонньої черги
    for char in formatted_string:
        string_deque.append(char)

    # Порівнюємо символи з обох кінців
    while len(string_deque) > 1:
        if string_deque.popleft() != string_deque.pop():
            return False
    return True


# Тестуємо функцію
test_strings = ["А роза упала на лапу Азора", "Не паліндром", "Madam, I'm Adam"]
for s in test_strings:
    print(f"'{s}' є паліндромом? {is_palindrome(s)}")

import queue
import random
import time

# Створюємо чергу заявок
requests_queue = queue.Queue()


def generate_request(request_id):
    """
    Генерує нову заявку з унікальним ідентифікатором та додає її до черги.
    """
    print(f"Генеруємо заявку з ID: {request_id}")
    requests_queue.put(request_id)


def process_request():
    """
    Обробляє заявку з черги.
    """
    if not requests_queue.empty():
        request_id = requests_queue.get()
        print(f"Обробляємо заявку з ID: {request_id}")
    else:
        print("Черга пуста.")


# Головний цикл (для демонстрації, обмежимо кількість ітерацій)
for _ in range(5):
    request_id = random.randint(1, 100)  # Генеруємо унікальний ID для заявки
    generate_request(request_id)
    time.sleep(1)  # Імітація часу на генерацію заявки
    process_request()
    time.sleep(1)  # Імітація часу на обробку заявки

import asyncio
import time
import threading
import multiprocessing


def calculate_threaded(operation, num1, num2):
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Ошибка: деление на ноль"
            return num1 / num2
        else:
            return "Неизвестная операция"
    except Exception as e:
        return f"Ошибка: {e}"


def calculate_multiprocessing(operation, num1, num2):
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Ошибка: деление на ноль"
            return num1 / num2
        else:
            return "Неизвестная операция"
    except Exception as e:
        return f"Ошибка: {e}"



async def calculate_async(operation, num1, num2):
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Ошибка: деление на ноль"
            return num1 / num2
        else:
            return "Неизвестная операция"
    except Exception as e:
        return f"Ошибка: {e}"

async def main_async(operations):
    tasks = [calculate_async(operation, num1, num2) for operation, num1, num2 in operations]
    results = await asyncio.gather(*tasks)
    start_time = time.time()
    for i, result in enumerate(results):
        print(f"Результат {operations[i][0]}({operations[i][1]}, {operations[i][2]}): {result}")
    end_time = time.time()
    print(f"Время выполнения asyncio: {end_time - start_time:.2f} секунд")



def main_threaded(operations):
    results = []
    threads = []
    start_time = time.time()
    for operation, num1, num2 in operations:
        thread = threading.Thread(target=calculate_threaded, args=(operation, num1, num2), daemon=True)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


    for operation, num1, num2 in operations:
        for i, result in enumerate(results):
          if operation == operations[i][0] and num1 == operations[i][1] and num2 == operations[i][2]:
              print(f"Результат {operation}({num1}, {num2}): {result}")
              break
    end_time = time.time()
    print(f"Время выполнения threading: {end_time - start_time:.2f} секунд")

def main_multiprocessing(operations):
    with multiprocessing.Pool() as pool:
        start_time = time.time()
        results = pool.starmap(calculate_multiprocessing, operations)
        for i, result in enumerate(results):
            print(f"Результат {operations[i][0]}({operations[i][1]}, {operations[i][2]}): {result}")
        end_time = time.time()
        print(f"Время выполнения multiprocessing: {end_time - start_time:.2f} секунд")




if __name__ == "__main__":
    operations = [
        ("add", 10, 5),
        ("subtract", 20, 8),
        ("multiply", 4, 6),
        ("divide", 15, 3),
        ("divide", 10, 0),
        ("add", 100, 200),
        ("multiply", 1000, 10),
        ("subtract", 100, 20),
        ("divide", 100, 25),
        ("multiply", 50, 2)
    ]

    asyncio.run(main_async(operations))
    main_threaded(operations)
    main_multiprocessing(operations)
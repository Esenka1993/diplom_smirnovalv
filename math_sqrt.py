import multiprocessing
import threading
import asyncio
import time
import math

def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += math.sqrt(i)
    return result

def run_threaded(tasks):
    threads = []
    #results = []
    for task in tasks:
        thread = threading.Thread(target=cpu_bound_task, args=(task,), daemon=True)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def run_multiprocessing(tasks):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(cpu_bound_task, tasks)
    return results

async def run_async(tasks):
    async def async_cpu_bound_task(n):
      return cpu_bound_task(n)
    tasks_async = [async_cpu_bound_task(task) for task in tasks]
    results = await asyncio.gather(*tasks_async)
    return results

if __name__ == "__main__":
    num_tasks = 20 #число задач
    tasks = [1000000] * num_tasks #число итераций в цикле


    # Многопоточное выполнение
    start_time = time.time()
    run_threaded(tasks)
    end_time = time.time()
    print(f"Время выполнения многопоточным способом: {end_time - start_time:.2f} секунд")

    # Многопроцессное выполнение
    start_time = time.time()
    run_multiprocessing(tasks)
    end_time = time.time()
    print(f"Время выполнения многопроцессным способом: {end_time - start_time:.2f} секунд")

    # Асинхронное выполнение (asyncio)
    start_time = time.time()
    asyncio.run(run_async(tasks))
    end_time = time.time()
    print(f"Время выполнения асинхронным способом: {end_time - start_time:.2f} секунд")
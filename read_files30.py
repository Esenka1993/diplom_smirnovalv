import asyncio
import aiofiles
import time
import threading
import multiprocessing


async def read_file_async(file):
    try:
        async with aiofiles.open(file, "r", encoding="utf-8") as f:
            info = await f.read()
            return info
    except FileNotFoundError:
        return f"Файл {file} не найден"
    except Exception as e:
        return f"Ошибка чтения файла {file}: {e}"



def read_file_threaded(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            info = f.read()
            return info
    except FileNotFoundError:
        return f"Файл {file} не найден"
    except Exception as e:
        return f"Ошибка чтения файла {file}: {e}"




def read_file_multiprocessing(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            info = f.read()
            return info
    except FileNotFoundError:
        return f"Файл {file} не найден"
    except Exception as e:
        return f"Ошибка чтения файла {file}: {e}"




async def main_async(files):
    tasks = [read_file_async(file) for file in files]
    results = await asyncio.gather(*tasks)
    start_time = time.time()
    for i, result in enumerate(results):
        print(f"Результат файла {files[i]}: {result[:50]}...")
    end_time = time.time()
    print(f"Время выполнения asyncio: {end_time - start_time:.2f} секунд")


def main_threaded(files):
    results = []
    threads = []
    start_time = time.time()
    for file in files:
        thread = threading.Thread(target=read_file_threaded, args=(file,), daemon=True)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    for i, result in enumerate(results):
        print(f"Результат файла {files[i]}: {result[:50]}...")
    end_time = time.time()
    print(f"Время выполнения threading: {end_time - start_time:.2f} секунд")


def main_multiprocessing(files):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        start_time = time.time()
        results = pool.map(read_file_multiprocessing, files)
        for i, result in enumerate(results):
            print(f"Результат файла {files[i]}: {result[:50]}...")
        end_time = time.time()
        print(f"Время выполнения multiprocessing: {end_time - start_time:.2f} секунд")


if __name__ == "__main__":
    files = ["files_for_read/file1.txt", "files_for_read/file2.txt", "files_for_read/file3.txt",
             "files_for_read/file4.txt", 'files_for_read/file5.txt', "files_for_read/file6.txt",
             "files_for_read/file7.txt", "files_for_read/file8.txt", "files_for_read/file9.txt",
             'files_for_read/file10.txt', "files_for_read/file11.txt", "files_for_read/file12.txt",
             'files_for_read/file13.txt', "files_for_read/file14.txt", "files_for_read/file15.txt",
             'files_for_read/file16.txt', "files_for_read/file17.txt", "files_for_read/file18.txt",
             'files_for_read/file19.txt', "files_for_read/file20.txt", "files_for_read/file21.txt",
             'files_for_read/file22.txt', "files_for_read/file23.txt", "files_for_read/file24.txt",
             'files_for_read/file25.txt', "files_for_read/file26.txt", "files_for_read/file27.txt",
             'files_for_read/file28.txt', "files_for_read/file29.txt", "files_for_read/file30.txt"]

    asyncio.run(main_async(files))
    main_threaded(files)
    main_multiprocessing(files)
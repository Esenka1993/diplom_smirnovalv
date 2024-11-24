import asyncio
import time
import threading
import multiprocessing
import requests
import aiohttp


async def fetch_content_async(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return f"Ошибка загрузки {url}: {response.status}", response.status
        except aiohttp.ClientError as e:
            return f"Ошибка загрузки {url}: {e}", 500
        except asyncio.TimeoutError:
            return f"Ошибка: таймаут при загрузке {url}", 504



def fetch_content_threaded(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return f"Ошибка загрузки {url}: {response.status_code}", response.status_code
    except requests.exceptions.RequestException as e:
        return f"Ошибка загрузки {url}: {e}", 500


def fetch_content_multiprocessing(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return url, response.text
        else:
            return url, f"Ошибка загрузки {url}: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return url, f"Ошибка загрузки {url}: {e}"




async def main_async(urls):
    tasks = [fetch_content_async(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for i, (content, status) in enumerate(results):
        if status == 200:
            print(f"Загрузка {urls[i]} успешна: первые 50 символов: {content[:50]}...")
        else:
            print(f"Ошибка загрузки {urls[i]}: {content}")



def main_threaded(urls):
    results = []
    threads = []
    start_time = time.time()
    for url in urls:
        thread = threading.Thread(target=fetch_content_threaded, args=(url,), daemon=True)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    for thread in threads:
        try:
            result = thread.get_result()
            results.append(result)
        except Exception as e:
            print(f"Ошибка при получении результата потока: {e}")

    for i, url in enumerate(urls):
      try:
        result = fetch_content_threaded(url)
        if isinstance(result, tuple):
            status = result[1]
            if status == 200:
                print(f"Загрузка {url} успешна: первые 50 символов: {result[0][:50]}...")
            else:
                print(f"Ошибка загрузки {url}: {result[0]}")
      except Exception as e:
        print(f"Ошибка: {e}")

    end_time = time.time()
    print(f"Время выполнения threading: {end_time - start_time:.2f} секунд")


def main_multiprocessing(urls):
    with multiprocessing.Pool(processes=min(multiprocessing.cpu_count(), len(urls))) as pool: # ограничить число процессов
        start_time = time.time()
        results = pool.starmap(fetch_content_multiprocessing, [(url,) for url in urls])

        for url, content in results:
            if isinstance(content, str):
                print(f"Загрузка {url} успешна: первые 50 символов: {content[:50]}...")
            else:
                print(f"Ошибка загрузки {url}: {content}")

        end_time = time.time()
        print(f"Время выполнения multiprocessing: {end_time - start_time:.2f} секунд")




if __name__ == "__main__":
    urls = ['https://ria.ru/20241121/solntse-1984926002.html', 'https://ria.ru/20241120/nauka-1984588483.html',
            'https://ria.ru/20241120/starship-1984727616.html',
            'https://ria.ru/20241122/nauka-1985061956.html', 'https://ria.ru/20241122/bolid-1985169486.html'
            "https://www.google.com",
            "https://www.python.org",
            "https://www.wikipedia.org",
            "https://www.bbc.com",
            "https://stackoverflow.com"
            ]
    asyncio.run(main_async(urls))
    main_threaded(urls)
    main_multiprocessing(urls)
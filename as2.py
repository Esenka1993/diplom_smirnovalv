import asyncio
import aiohttp
import time
import threading
import multiprocessing
import requests

async def fetch_content(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return f"Ошибка загрузки {url}: {response.status}", response.status
        except aiohttp.ClientError as e:
            return f"Ошибка загрузки {url}: {e}", 500


async def main(urls):
    """Загружает контент с нескольких URL одновременно."""
    tasks = [fetch_content(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for i, (content, status) in enumerate(results):
        if status == 200:
            print(f"Загрузка {urls[i]} успешна:\n{content[:10]}...")
        else:
            print(f"Ошибка при загрузке {urls[i]}: {content}")

def fetch_content_threaded(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Ошибка загрузки {url}: {response.status_code}", response.status_code
    except requests.exceptions.RequestException as e:
        return f"Ошибка загрузки {url}: {e}", 500



def main_threaded(urls):
    results = []
    threads = []
    start_time = time.time()
    for url in urls:
        thread = threading.Thread(target=fetch_content_threaded, args=(url,),
                                  daemon=True)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    for i, url in enumerate(urls):
        for j, result in enumerate(results):
          if i == j[0]:
             if isinstance(result, tuple):
                status = result[1]
                if status == 200:
                    print(f"Загрузка {url} успешна:\n{result[0][:10]}...")
                else:
                    print(f"Ошибка при загрузке {url}: {result[0]}")

    end_time = time.time()
    print(f"Время выполнения threading: {end_time - start_time:.2f} секунд")



def fetch_content_multiprocessing(url):
  try:
      response = requests.get(url)
      if response.status_code == 200:
          return url, response.text, response.status_code
      else:
          return url, f"Ошибка загрузки {url}: {response.status_code}", response.status_code
  except requests.exceptions.RequestException as e:
      return url, f"Ошибка загрузки {url}: {e}", 500


def main_multiprocessing(urls):
    with multiprocessing.Pool() as pool:
        start_time = time.time()
        results = pool.starmap(fetch_content_multiprocessing, [(url,) for url in urls])

        for url, content, status in results:
            if status == 200:
                print(f"Загрузка {url} успешна:\n{content[:10]}...")
            else:
                print(f"Ошибка при загрузке {url}: {content}")

        end_time = time.time()
        print(f"Время выполнения multiprocessing: {end_time - start_time:.2f} секунд")



if __name__ == "__main__":
    urls = ['https://ria.ru/20241121/solntse-1984926002.html', 'https://ria.ru/20241120/nauka-1984588483.html',
            'https://ria.ru/20241120/starship-1984727616.html',
            'https://ria.ru/20241122/nauka-1985061956.html', 'https://ria.ru/20241122/bolid-1985169486.html']

    start_time = time.time()
    asyncio.run(main(urls))
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")
    main_threaded(urls)
    main_multiprocessing(urls)


from PIL import Image, ImageFilter
import threading
import multiprocessing
import time


def process_image_threaded(image_path, output_path):
    try:
        image_1 = Image.open(image_path)
        image_1_1 = image_1.convert('L')
        ch_im_1 = image_1_1.resize((900, 540))
        ch_2 = ch_im_1.filter(ImageFilter.DETAIL)
        ch_2.save(output_path)
    except Exception as e:
        print(f"Ошибка при обработке изображения в потоке: {e}")


def process_image_multiprocessing(image_path, output_path):
    try:
        image_1 = Image.open(image_path)
        image_1_1 = image_1.convert('L')
        ch_im_1 = image_1_1.resize((900, 540))
        ch_2 = ch_im_1.filter(ImageFilter.DETAIL)
        ch_2.save(output_path)
    except Exception as e:
        print(f"Ошибка при обработке изображения в процессе: {e}")


if __name__ == "__main__":
    image_path = '774757691.jpg'
    output_path_threaded = 'кот_threaded.png'
    output_path_multiprocessing = 'кот_multiprocessing.png'

    # Обычное выполнение
    start_time = time.time()
    image_1 = Image.open(image_path)
    image_1_1 = image_1.convert('L')
    ch_im_1 = image_1_1.resize((900, 540))
    ch_2 = ch_im_1.filter(ImageFilter.DETAIL)
    ch_2.save('кот_обычное_изобр.png')
    end_time = time.time()
    print(f"Время выполнения обычным способом: {end_time - start_time:.2f} секунд")


    # Многопоточное выполнение
    start_time = time.time()
    thread = threading.Thread(target=process_image_threaded, args=(image_path, output_path_threaded), daemon=True)
    thread.start()
    thread.join()
    end_time = time.time()
    print(f"Время выполнения многопоточным способом: {end_time - start_time:.2f} секунд")

    # Многопроцессное выполнение
    start_time = time.time()
    process = multiprocessing.Process(target=process_image_multiprocessing, args=(image_path, output_path_multiprocessing))
    process.start()
    process.join()
    end_time = time.time()
    print(f"Время выполнения многопроцессным способом: {end_time - start_time:.2f} секунд")
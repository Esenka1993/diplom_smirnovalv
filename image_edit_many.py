from PIL import Image, ImageFilter
import threading
import multiprocessing
import time
import os
def process_single_image(filepath, outpath):
    try:
        image_1 = Image.open(filepath)
        image_1_1 = image_1.convert('L')
        ch_im_1 = image_1.resize((900, 540))
        ch_2 = ch_im_1.filter(ImageFilter.DETAIL)
        ch_2.save(outpath)
    except Exception as e:
        print(f"Ошибка обработки изображения {filepath}: {e}")


def process_images_threaded(image_paths, output_paths):
    threads = []
    for i in range(len(image_paths)):
        thread = threading.Thread(target=process_single_image, args=(image_paths[i], output_paths[i]), daemon=True)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def process_images_multiprocessing(image_paths, output_paths):
    with multiprocessing.Pool() as pool:
        pool.starmap(process_single_image, zip(image_paths, output_paths))


if __name__ == "__main__":
    image_dir = "images_for_edit"
    output_dir = "ready_images"

    image_paths = [os.path.join(image_dir, f"image_{i}.jpg") for i in range(1, 11)]
    output_paths = [os.path.join(output_dir, f"output_{i}.png") for i in range(1, 11)]


    for path in image_paths:
        img = Image.new('RGB', (500, 500), color = 'grey')
        img.save(path)


    # Базовое выполнение
    start_time = time.time()
    for i in range(len(image_paths)):
        process_single_image(image_paths[i], output_paths[i])
    end_time = time.time()
    print(f"Время базового выполнения: {end_time - start_time:.2f} секунд")


    # Многопоточное выполнение
    start_time = time.time()
    process_images_threaded(image_paths, output_paths)
    end_time = time.time()
    print(f"Время выполнения многопоточным способом: {end_time - start_time:.2f} секунд")


    # Многопроцессное выполнение
    start_time = time.time()
    process_images_multiprocessing(image_paths, output_paths)
    end_time = time.time()
    print(f"Время выполнения многопроцессным способом: {end_time - start_time:.2f} секунд")
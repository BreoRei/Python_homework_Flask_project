import random
import time
import asyncio
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

MIN_NUMBER = 1
MAX_NUMBER = 100
NUMBER_OF_INTEGERS = 1_000_000


def generate_random_array(size):
    return [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(size)]


def calculate_sum(array):
    return sum(array)


async def calculate_sum_async(array):
    return sum(array)


def main():
    array = generate_random_array(NUMBER_OF_INTEGERS)

    # Многопоточность
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        result = executor.submit(calculate_sum, array).result()
    end_time = time.time()
    print(f"Многопоточность: Сумма элементов массива: {result}. Время выполнения: {end_time - start_time} секунд.")

    # Многопроцессорность
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map(calculate_sum, [array])[0]
    end_time = time.time()
    print(f"Многопроцессорность: Сумма элементов массива: {result}. Время выполнения: {end_time - start_time} секунд.")

    # Асинхронность
    async def main_async():
        start_time = time.time()
        result = await calculate_sum_async(array)
        end_time = time.time()
        print(f"Асинхронность: Сумма элементов массива: {result}. Время выполнения: {end_time - start_time} секунд.")

    # loop = asyncio.new_event_loop()
    # loop.run_until_complete(main_async())
    asyncio.run(main_async())


if __name__ == "__main__":
    main()

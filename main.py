import asyncio
import SyncFibonacciNumber


async def main():
    while True:
        try:
            n = int(input("Enter a non-negative number: "))
            if n < 0:
                print("Please enter a non-negative number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    task1 = asyncio.create_task(SyncFibonacciNumber.fib_with_delay(n))
    task2 = asyncio.create_task(SyncFibonacciNumber.fib_with_delay(n))

    await asyncio.gather(task1,
                         task2)

    result1 = None
    result2 = None
    try:
        result1 = task1.result()
        result2 = task2.result()
    except Exception as e:
        print(f"An error occurred: {e}")

    if result1 is not None and result2 is not None:
        print(f"Fib({n}): {result1 if result1 < result2 else result2}")
        print(f"First task finished: {'task1' if result1 < result2 else 'task2'}")


if __name__ == "__main__":
    asyncio.run(main())
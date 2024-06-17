# import asyncio

# async def delay_two_seconds():
#     print("delay_two_seconds: start")
#     await asyncio.sleep(2)
#     print("delay_two_seconds: end")

# async def delay_five_seconds():
#     print("delay_five_seconds: start")
#     await asyncio.sleep(5)
#     print("delay_five_seconds: end")

# async def main():
#     task1 = asyncio.create_task(delay_two_seconds())
#     task2 = asyncio.create_task(delay_five_seconds())
    
#     await task1
#     await task2


# asyncio.run(main())



import asyncio
import random

async def random_intervals():
    initial_delay = random.uniform(1.0, 5.0) 
    print(f"Starting with an initial delay of {initial_delay:.2f} seconds")
    await asyncio.sleep(initial_delay)
    
    for i in range(1, 11):
        print(i)
        if i <= 10:  
            interval_delay = random.uniform(1,2) 
            print(f"Waiting for {interval_delay:.2f} seconds before printing the next number")
            await asyncio.sleep(interval_delay)

async def main():
    await random_intervals()


asyncio.run(main())
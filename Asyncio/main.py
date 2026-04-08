import asyncio


# Coroutine function 
# async def main():
#     print("Start async main function ")
# # main() #coroutine object


# Part-1
# async def fetch_data(delay, id):
#     print("Fetching data... id:", id)
#     await asyncio.sleep(delay)
#     print("Data fetched, id:", id)
#     return {
#         "data": "Some Data",
#         "id" : id
#     }
# async def main():
#     task_1 = fetch_data(3, 1)
#     task_2 = fetch_data(5, 2)

#     result_1 = await task_1
#     print(f"Received Results: {result_1}")

#     result_2 = await task_2
#     print(f"Received Results: {result_2}")





# Part-2
async def fetch_data(delay, id):
    print(f"Fetching data....id: {id}")
    await asyncio.sleep(delay)
    print(f"Fetched data Successfully of id:{id}")
    return{
        "id": id,
        "data": f"Sample data from routin {id}"
    }

async def main():
    task_1 = asyncio.create_task(fetch_data(1, 2))
    task_2 = asyncio.create_task(fetch_data(2, 3))
    task_3 = asyncio.create_task(fetch_data(3, 1))

    # results =  await asyncio.gather(fetch_data(1, 2),fetch_data(2, 3), fetch_data(3, 1))
    # for result in results:
    #     print(result)



    # TaskGroup
    result_1 = await task_1
    result_2 = await task_2
    result_3 = await task_3


    print(result_1,result_2, result_3)
asyncio.run(main())
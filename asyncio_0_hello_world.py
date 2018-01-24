import asyncio


def hello_world1():
    print("Hello World1!")
    return True


async def hello_world2():
    print("Hello World2!")
    return True


async def hello_world3():
    await asyncio.sleep(1)
    return "Hello World3!"


def got_result(future):
    print(future.result())


helloworld3 = hello_world3()
helloworld2 = hello_world2()
helloworld1 = hello_world1()

print("Get loop")
loop = asyncio.get_event_loop()
# Blocking call which returns when the hello_world() coroutine is done
print("Run loop...")
loop.run_until_complete(helloworld2)
loop.run_until_complete(helloworld3)
loop.close()
print("Close loop...")

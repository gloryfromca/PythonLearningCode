import asyncio
import time
async def A_IO():
	print("A_IO sleep...")
	await asyncio.sleep(3)
	print("A_IO get up!")
	return "A"
async def B_IO():
	print("B_IO sleep...")
	await asyncio.sleep(1)
	print("B_IO get up!")
	return "B"
async def C_IO(name):
	a_result = await A_IO()
	print(name + "_a:" + a_result)
	b_result = await B_IO()
	print(name + "_b:" + b_result)

begin_time = time.time()
c1 = C_IO("c1")
c2 = C_IO("c2")

loop = asyncio.get_event_loop()
server = loop.run_until_complete(asyncio.wait([c1, c2]))
print(server)
print("time:", time.time()-begin_time)
	
	




	
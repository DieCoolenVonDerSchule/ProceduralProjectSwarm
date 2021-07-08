#!/usr/bin/env python

# HIVE (websocket server)

import sys
import random
import asyncio
import websockets
from datetime import date


async def createGalaxy(websocket, path):
	transit = await websocket.recv()
	print("TRANSIT: ", transit)
	t = transit.split(",")
	systemCount = t[0]
	planetCountMin = t[1]
	planetCountMax = t[2]
	
	if systemCount==0:
		systemCount = random.randrange(10,20)
		
		
	if planetCountMin==0 and planetCountMax==0:
		planetCountMin = 0
		planetCountMax = 8
	
	generatemsg = f"GENERATED {systemCount} SYSTEMS"
	
	await websocket.send(generatemsg)
	print(f"> {generatemsg}")
	setGalaxy(int(systemCount),int(planetCountMin),int(planetCountMax))
	

def setSystem(planetCount) :
	file_object = open('/var/lib/hive/hivelog.txt', 'a')
	file_object.write('\n')
	file_object.write(str(date.today()))
	file_object.write(' ')
	file_object.write('planetCount: ')
	file_object.write(str(planetCount))
	file_object.write('\n')
	print("planetCount: "+str(planetCount))
	for i in range(0,planetCount) :
		file_object.write('planet generated')
		file_object.write('\n')
		print("-> planet generated")
	file_object.write('-------------------------------')
	file_object.write('\n')
	file_object.close()
	print("-------------------------------")
	


def setGalaxy(systemCount, planetCountMin, planetCountMax) :

	print("---------NEW-GALAXY------------")
	for i in range(0,systemCount) :
		print("SYSTEM GENERATED")
		setSystem(random.randrange(planetCountMin,planetCountMax))


print("START HIVE")
print("----------")		
	

start_server = websockets.serve(createGalaxy, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

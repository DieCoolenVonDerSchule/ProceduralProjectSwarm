#!/usr/bin/env python

# QUEEN (websocket client) 

import sys
import asyncio
import websockets
from datetime import date

async def createGalaxy(transit) :
	uri = "ws://c_hive:8765"
	async with websockets.connect(uri) as websocket:
				
		await websocket.send(transit)
		print(f"> {transit}")
		
		generatemsg = await websocket.recv()
		print(f"< {generatemsg}")

print("START QUEEN")
print("-----------")

if len(sys.argv) == 1:
	print("CREATE GALAXY WITHOUT ARGUMENTS")
	print("")
	systemCount = 0
	planetCountMin = 0
	planetCountMax = 0
	
if len(sys.argv) == 2:
	print("CREATE GALAXY WITH SYSTEM COUNT: ", str(sys.argv[1]))
	print("")
	systemCount = sys.argv[1]
	planetCountMin = 0
	planetCountMax = 0

if len(sys.argv) > 2:
	print("                      systems  planetMin planetMax")
	print("Argument List: ", str(sys.argv))
	systemCount = sys.argv[1]
	planetCountMin = sys.argv[2]
	planetCountMax = sys.argv[3]
	
	
transferStr = str(systemCount)+","+str(planetCountMin)+","+str(planetCountMax)
file_object = open('/var/lib/queen/queenlog.txt', 'a')
file_object.write('\n')
file_object.write(str(date.today()))
file_object.write('\n')
file_object.write('systemCount: ')
file_object.write(str(systemCount))
file_object.write('\n')
file_object.write('planetCountMin: ')
file_object.write(str(planetCountMin))
file_object.write('\n')
file_object.write('planetCountMax: ')
file_object.write(str(planetCountMax))
file_object.write('\n')
file_object.write('-------------------------------')
file_object.write('\n')
file_object.close()
	
asyncio.get_event_loop().run_until_complete(createGalaxy(transferStr))

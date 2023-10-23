from evdev import InputDevice, ecodes
from pygame import mixer

dev = InputDevice('/dev/input/event4')

print(dev)
mixer.init()
bumbo = mixer.Sound('Sounds/BUMBO_COM_EQ.wav')
caixa = mixer.Sound('Sounds/caixa_com_EQ.wav')
tom = mixer.Sound('Sounds/TOM_1_COM_EQ.wav')
tom2 = mixer.Sound('Sounds/TOM_2_COM_EQ.wav')

try:
	for event in dev.read_loop():

		if event.type == ecodes.EV_KEY:
			if event.type == ecodes.EV_KEY:
				if(event.value == 1):
					# switch case for event.code
					if(event.code == 304):
						bumbo.play()
					elif(event.code == 305):
						caixa.play()
					elif(event.code == 306):
						tom.play()
					elif(event.code == 307):
						tom2.play()

except KeyboardInterrupt:
	print("Exiting program...")
	mixer.quit()
	exit()

# async def helper(dev):
# 	async for event in dev.async_read_loop():
		# if event.type == ecodes.EV_KEY:
		# 	if(event.value == 1):
		# 		# switch case for event.code
		# 		if(event.code == 304):
		# 			print("Azul")
		# 			bumbo.play()
		# 		elif(event.code == 305):
		# 			print("Verde")
		# 			caixa.play()
		# 		elif(event.code == 306):
		# 			print("Vermelho")
		# 			tom.play()
		# 		elif(event.code == 307):
		# 			print("Amarelo")
		# 			tom2.play()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(helper(dev))
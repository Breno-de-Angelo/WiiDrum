import threading
import sys
from evdev import InputDevice, ecodes
from pygame import mixer
from pygame import key

devBattery = InputDevice('/dev/input/event4')

print(devBattery)
mixer.init()
bumbo = mixer.Sound('Sounds/BUMBO_COM_EQ.wav')
caixa = mixer.Sound('Sounds/caixa_com_EQ.wav')
tom = mixer.Sound('Sounds/TOM_1_COM_EQ.wav')
tom2 = mixer.Sound('Sounds/TOM_2_COM_EQ.wav')


def battery(devBattery):
	for event in devBattery.async_read_loop():
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

def stop():
	while True:
		# if "q" key is pressed
		input("Pressione ENTER para sair...")
		return True
	
def main():
	# Create new threads
	batteryThread = threading.Thread(target=battery, args=(devBattery, ))

	# Start new Threads
	batteryThread.start()

	if(stop()):
		print("Exiting program...")
		batteryThread.join()
		mixer.quit()

main()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(helper(dev))

# try:
# 	for event in dev.read_loop():
# 		if event.type == ecodes.EV_KEY:
# 			if event.type == ecodes.EV_KEY:
# 				if(event.value == 1):
# 					# switch case for event.code
# 					if(event.code == 304):
# 						bumbo.play()
# 					elif(event.code == 305):
# 						caixa.play()
# 					elif(event.code == 306):
# 						tom.play()
# 					elif(event.code == 307):
# 						tom2.play()

# except KeyboardInterrupt:
# 	print("Exiting program...")
# 	mixer.quit()
# 	exit()

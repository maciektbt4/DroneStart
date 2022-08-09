from tello import Tello
from datetime import datetime
import time



tello = Tello()


tello.send_command("command")
time.sleep(3)
tello.send_command("takeoff")
time.sleep(2)
tello.send_command("land")

print("Thank you for a pleasent fly")
import threading
# import os
# import signal as sig
import time

class lightBulb():
    consumption_rate: int
    light_bulb_power_state: bool = True
    thread_power_consumption_id = None
    def __init__(self):
        print("Hello from lightBulb.")
        self.consumption_rate = 0.0

    def get_consumption(self):
        return round(self.consumption_rate, 2)
    
    def power_light_bulb(self, signal):
        if signal:
            self.light_bulb_power_state = True
            self.thread_power_consumption = self.generate_power_comsumption()
        else:
            self.light_bulb_power_state = False
            if self.thread_power_consumption_id != None:
                # print(f"show me thread_power_comsumption_id {self.thread_power_consumption_id}")
                # os.kill(self.thread_power_consumption_id, sig.SIGTERM)
                self.thread_power_consumption_id.join()
                

    def generate_power_comsumption(self):
        self.consumption_rate = 0.48
        # power consumption of 4 unit LED light bulbs might be varied from 0.08 kWh to 0.1 kWh.
        thr = threading.Thread(target=self.thread_callback, args=["Light-bulb", 5])
        thr.start()
        return thr

    def thread_callback(self, name, loop):

        while self.light_bulb_power_state:
            while self.consumption_rate < 0.5 and self.light_bulb_power_state:
                self.consumption_rate += 0.02
                time.sleep(0.2)
                print(f"{name}: ", self.consumption_rate)
            while self.consumption_rate > 0.08 and self.light_bulb_power_state:
                self.consumption_rate -= 0.02
                time.sleep(0.2)
                print(f"{name}: ", self.consumption_rate)
        self.consumption_rate = 0.0
import threading
# import os
# import signal as sig
import time

class airCon():
    consumption_rate: int
    air_con_power_state: bool = True
    thread_power_consumption_id = None
    def __init__(self):
        print("Hello from airCon.")
        self.consumption_rate = 0.0

    def get_consumption(self):
        return round(self.consumption_rate, 2)
    
    def power_air_con(self, signal):
        if signal:
            self.air_con_power_state = True
            self.thread_power_consumption = self.generate_power_comsumption()
        else:
            self.air_con_power_state = False
            if self.thread_power_consumption_id != None:
                # print(f"show me thread_power_comsumption_id {self.thread_power_consumption_id}")
                # os.kill(self.thread_power_consumption_id, sig.SIGTERM)
                self.thread_power_consumption_id.join()
                

    def generate_power_comsumption(self):
        self.consumption_rate = 0.48
        # power consumption of 1 unit air con might be varied from 0.48 kWh to 5.14 kWh.
        thr = threading.Thread(target=self.thread_callback, args=["Air-con", 5])
        thr.start()
        return thr

    def thread_callback(self, name, loop):
        while self.air_con_power_state:
            while self.consumption_rate < 5.14 and self.air_con_power_state:
                self.consumption_rate += 0.8
                time.sleep(0.2)
                print(f"{name}: ", self.consumption_rate)
            while self.consumption_rate > 0.48 and self.air_con_power_state:
                self.consumption_rate -= 0.8
                time.sleep(0.2)
                print(f"{name}: ", self.consumption_rate)
        self.consumption_rate = 0.0


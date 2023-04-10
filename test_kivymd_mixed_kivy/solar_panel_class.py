import threading
# import os
# import signal as sig
import time

class SolarPanel():
    produce_rate: int
    solar_panel_power_state: bool = True
    thread_produce_id = None
    def __init__(self):
        print("Hello from SolarPanel.")
        self.produce_rate = 0.0

    def get_produce_rate(self):
        return round(self.produce_rate, 2)
    
    def power_solar_panel(self, signal):
        if signal:
            self.solar_panel_power_state = True
            self.thread_produce_id = self.generate_produce_voltage()
        else:
            self.solar_panel_power_state = False
            if self.thread_produce_id != None:
                self.thread_produce_id.join()
                

    def generate_produce_voltage(self):
        self.produce_rate = 1.52
        # charging rate should be between 24.8 - 25.2
        thr = threading.Thread(target=self.thread_callback, args=["Solar-Panel", 5])
        thr.start()
        return thr

    def thread_callback(self, name, loop):

        while self.solar_panel_power_state:
            while self.produce_rate < 2.85 and self.solar_panel_power_state:
                self.produce_rate += 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.produce_rate)
            while self.produce_rate > 1.49 and self.solar_panel_power_state:
                self.produce_rate -= 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.produce_rate)
        self.produce_rate = 0.0
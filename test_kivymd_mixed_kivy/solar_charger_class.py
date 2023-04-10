import threading
# import os
# import signal as sig
import time

class SolarCharger():
    charging_rate: int
    solar_charger_power_state: bool = True
    thread_charging_voltage_id = None
    def __init__(self):
        print("Hello from SolarCharger.")
        self.charging_rate = 0.0

    def get_charging_rate(self):
        return round(self.charging_rate, 2)
    
    def power_solar_charger(self, signal):
        if signal:
            self.solar_charger_power_state = True
            self.thread_charging_voltage_id = self.generate_charging_voltage()
        else:
            self.solar_charger_power_state = False
            if self.thread_charging_voltage_id != None:
                self.thread_charging_voltage_id.join()
                

    def generate_charging_voltage(self):
        self.charging_rate = 22.0
        # charging rate should be between 24.8 - 25.2
        thr = threading.Thread(target=self.thread_callback, args=["Solar-Charger", 5])
        thr.start()
        return thr

    def thread_callback(self, name, loop):

        while self.solar_charger_power_state:
            while self.charging_rate < 25.2 and self.solar_charger_power_state:
                self.charging_rate += 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.charging_rate)
            while self.charging_rate > 23.0 and self.solar_charger_power_state:
                self.charging_rate -= 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.charging_rate)
        self.charging_rate = 0.0
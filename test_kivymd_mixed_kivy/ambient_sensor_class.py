import threading
import time

class AmbientSensor():
    consumption_rate: int
    ambient_sensor_power_state: bool
    ambient_sensor_temp: float
    ambient_sensor_humid: float
    ambient_sensor_pressure: float
    thread_power_consumption_id = None
    thread_temp_id = None
    thread_humid_id = None
    thread_pressure_id = None

    def __init__(self):
        print("Hello from AmbientSensor.")
        self.consumption_rate = 0.0
        self.ambient_sensor_temp = 31.0
        self.ambient_sensor_humid = 5.0
        self.ambient_sensor_pressure = 3.0

    def get_consumption(self):
        return round(self.consumption_rate, 2)
    
    def get_ambient_sensor_temp(self):
        return round(self.ambient_sensor_temp, 2)
    
    def get_ambient_sensor_humid(self):
        return round(self.ambient_sensor_humid, 2)

    def get_ambient_sensor_pressure(self):
        return round(self.ambient_sensor_pressure, 2)
    

    def power_ambitent_sensor(self, signal):
        if signal:
            self.ambient_sensor_power_state = True
            self.thread_power_consumption_id = self.generate_power_comsumption()
            self.thread_temp_id = self.generate_temp()
            self.thread_humid_id = self.generate_humid()
            self.thread_pressure_id = self.generate_pressure()
        else:
            self.ambient_sensor_power_state = False
            if self.thread_power_consumption_id != None:
                # print(f"show me thread_power_comsumption_id {self.thread_power_consumption_id}")
                # os.kill(self.thread_power_consumption_id, sig.SIGTERM)
                self.thread_power_consumption_id.join()
                self.thread_temp_id.join()
                self.thread_humid_id.join()
                self.thread_pressure_id.join()
    

    def generate_power_comsumption(self):
        self.consumption_rate = 0.48
        # power consumption of 1 unit ambient sensor might be varied from 0.48 kWh to 5.14 kWh.
        thr = threading.Thread(target=self.thread_callback, args=["Ambient-sensor", 5])
        thr.start()
        return thr

    def thread_callback(self, name, loop):
        while self.ambient_sensor_power_state:
            while self.consumption_rate < 0.67 and self.ambient_sensor_power_state:
                self.consumption_rate += 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.consumption_rate)
            while self.consumption_rate > 0.48 and self.ambient_sensor_power_state:
                self.consumption_rate -= 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.consumption_rate)
        self.consumption_rate = 0.0

    
    def generate_temp(self):
        self.ambient_sensor_temp = 25
        # room temperature range is 20 - 25 degree celsius.
        thr = threading.Thread(target=self.thread_temp_callback, args=["Ambient-temp", 5])
        thr.start()
        return thr

    def thread_temp_callback(self, name, loop):
        while self.ambient_sensor_power_state:
            while self.ambient_sensor_temp < 23 and self.ambient_sensor_power_state:
                self.ambient_sensor_temp += 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.ambient_sensor_temp)
            while self.ambient_sensor_temp > 20 and self.ambient_sensor_power_state:
                self.ambient_sensor_temp -= 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.ambient_sensor_temp)
        self.ambient_sensor_temp = 0.0
    

    def generate_humid(self):
        self.ambient_sensor_humid = 42
        # average humidity is 40 - 60 percentage.
        thr = threading.Thread(target=self.thread_humid_callback, args=["Ambient-humid", 5])
        thr.start()
        return thr

    def thread_humid_callback(self, name, loop):
        while self.ambient_sensor_power_state:
            while self.ambient_sensor_humid < 60 and self.ambient_sensor_power_state:
                self.ambient_sensor_humid += 0.2
                time.sleep(0.2)
                print(f"{name}: ", self.ambient_sensor_humid)
            while self.ambient_sensor_humid > 40 and self.ambient_sensor_power_state:
                self.ambient_sensor_humid -= 0.2
                time.sleep(0.2)
                print(f"{name}: ", self.ambient_sensor_humid)
        self.ambient_sensor_humid = 0.0

    def generate_pressure(self):
        self.ambient_sensor_pressure = 14
        # atmospheric pressure range is around 14.696 psi.
        thr = threading.Thread(target=self.thread_pressure_callback, args=["Ambient-pressure", 5])
        thr.start()
        return thr

    def thread_pressure_callback(self, name, loop):
        while self.ambient_sensor_power_state:
            while self.ambient_sensor_pressure < 15.9 and self.ambient_sensor_power_state:
                self.ambient_sensor_pressure += 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.ambient_sensor_pressure)
            while self.ambient_sensor_pressure > 12.1 and self.ambient_sensor_power_state:
                self.ambient_sensor_pressure -= 0.01
                time.sleep(0.2)
                print(f"{name}: ", self.ambient_sensor_pressure)
        self.ambient_sensor_pressure = 0.0
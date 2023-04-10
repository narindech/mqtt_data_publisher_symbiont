from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.app import MDApp

from kivy.clock import Clock
from functools import partial

import air_con_class as air
import light_bulb_class as light
import ambient_sensor_class as ambient
import solar_charger_class as charger
import solar_panel_class as panel

class LivingRoomScreen(Screen):
    light_bulb_1_toggle = True
    air_con_toggle = True
    solar_panel_toggle = True
    ambient_sensor_toggle = True
    solar_charger_toggle = True

    air = air.airCon()
    light = light.lightBulb()
    ambient = ambient.AmbientSensor()
    charger = charger.SolarCharger()
    panel = panel.SolarPanel()

    def enter(self):
        print("enter is called.")
        event = Clock.schedule_interval(partial(self.my_callback), 1 / 30.)
        self.turn_off()
        
    def turn_off(self):
        self.turn_off_light_bulb()
        self.turn_off_air_con()
        self.turn_off_solar_panel()
        self.turn_off_ambient_sensor()
        self.turn_off_solar_charger()


    def turn_off_light_bulb(self):
        self.light_bulb_1_toggle = False
        status_text = "Status: OFF"
        self.ids.image_light_bulb.source = "assets/light_bulb_off_cropped.jpg"
        self.ids.card_light_bulb.md_bg_color = "#404042"

        self.ids.label_light_bulb.color = "white"
        self.ids.label_light_bulb_status.color = "white"
        self.ids.label_light_bulb_power_consumption.color = "white"
        self.ids.label_light_bulb_status.text = status_text
        self.light.power_light_bulb(False)

    def turn_off_air_con(self):
        self.air_con_toggle = False
        status_text = "Status: OFF"
        self.ids.image_air_con.source = "assets/air_con_modified_off.jpg"
        self.ids.label_air_con_status.text = status_text
        self.air.power_air_con(False)

    def turn_off_solar_panel(self):
        self.solar_panel_toggle = False
        self.ids.image_solar_panel.source = "assets/solar_panel_off.jpg"
        self.ids.card_solar_panel.md_bg_color = "#b1ab9d"
        self.panel.power_solar_panel(False)
        # not producing electricity

    def turn_off_ambient_sensor(self):
        self.ambient_sensor_on_off()

    def turn_off_solar_charger(self):
        self.ids.label_charging_controller.color = "grey"
        self.ids.label_charging_controller_voltage.color = "grey"

    def my_callback(self, dt):
        # print('My callback is called', dt)
        
        air_con_value = self.air.get_consumption()
        light_con_value = self.light.get_consumption()

        ambient_con_value = self.ambient.get_consumption()
        ambient_temp_value = self.ambient.get_ambient_sensor_temp()
        ambient_humid_value = self.ambient.get_ambient_sensor_humid()
        ambient_pressure_value = self.ambient.get_ambient_sensor_pressure()

        solar_produce_rate = self.panel.get_produce_rate()

        solar_charging_rate = self.charger.get_charging_rate()

        print("show me air consumption --> ", air_con_value)
        print("get light bulb consumption: ", light_con_value)
        print("show me solar produce voltage --> ", solar_produce_rate)
        print("show me charging voltage --> ", solar_charging_rate)


        self.ids.label_air_con_power_consumption.text = f"Power consumption (kWh): {str(air_con_value)}"
        self.ids.label_light_bulb_power_consumption.text = f"Power consumption (kWh): {str(light_con_value)}"

        self.ids.label_ambient_sensor_temp.text = f"Temperature (°C) : {str(ambient_temp_value)}"
        self.ids.label_ambient_sensor_humid.text = f"Humidity (%): {str(ambient_humid_value)}"
        self.ids.label_ambient_sensor_pressure.text = f"Pressure (Psi): {str(ambient_pressure_value)}"
        self.ids.label_ambient_sensor_power_consumption.text = f"Power consumption (kWh): {str(ambient_con_value)}"
        
        self.ids.label_solar_panel_watt.text = f"Produced kilowatt per hour (kWh): {str(solar_produce_rate)}"
    
        self.ids.label_charging_controller_voltage.text = f"Charging voltage (V): {str(solar_charging_rate)}"

    def light_bulb_1_on_off(self):
        print("light_bulb_1_on_off is called.")
        status_text = "Status: "
        if self.light_bulb_1_toggle:
            status_text += "OFF"
            self.ids.image_light_bulb.source = "assets/light_bulb_off_cropped.jpg"
            self.ids.card_light_bulb.md_bg_color = "#404042"

            self.ids.label_light_bulb.color = "white"
            self.ids.label_light_bulb_status.color = "white"
            self.ids.label_light_bulb_power_consumption.color = "white"
            self.ids.label_light_bulb_status.text = status_text
            self.light.power_light_bulb(False)
            
        else:
            status_text += "ON"
            self.ids.image_light_bulb.source = "assets/light_bulb_on_cropped.jpg"  
            self.ids.card_light_bulb.md_bg_color = "#ffffff"

            self.ids.label_light_bulb.color = "black"
            self.ids.label_light_bulb_status.color = "black"
            self.ids.label_light_bulb_power_consumption.color = "black"
            self.ids.label_light_bulb_status.text = status_text
            self.light.power_light_bulb(True)

        self.light_bulb_1_toggle = not self.light_bulb_1_toggle  

    def air_con_on_off(self):
        print("air_con_on_off is called.")
        status_text = "Status: "
        if self.air_con_toggle:
            status_text += "OFF"
            self.ids.image_air_con.source = "assets/air_con_modified_off.jpg"
            self.ids.label_air_con_status.text = status_text
            self.air.power_air_con(False)
        else:
            status_text += "ON"
            self.ids.image_air_con.source = "assets/air_con_modified_on.jpg"
            self.ids.label_air_con_status.text = status_text
            self.air.power_air_con(True)
        self.air_con_toggle = not self.air_con_toggle

    def solar_panel_on_off(self):
        print("solar_panel_on_off is called.")
        if self.solar_panel_toggle:
            self.ids.card_solar_panel.md_bg_color = "#b1ab9d"
            self.ids.image_solar_panel.source = "assets/solar_panel_off.jpg"
            self.panel.power_solar_panel(False)
        else:
            self.ids.card_solar_panel.md_bg_color = "#fecf04"
            self.ids.image_solar_panel.source = "assets/solar_panel_on.jpg"
            self.panel.power_solar_panel(True)
        self.solar_panel_toggle = not self.solar_panel_toggle

    def ambient_sensor_on_off(self):
        print("ambient_sensor_on_off is called.")
        if self.ambient_sensor_toggle:
            self.ambient.power_ambitent_sensor(False)
            # self.ids.card_solar_panel.md_bg_color = "#b1ab9d"
            # self.ids.image_solar_panel.source = "assets/solar_panel_off.jpg"
        else:
            self.ambient.power_ambitent_sensor(True)
            # self.ids.card_solar_panel.md_bg_color = "#fecf04"
            # self.ids.image_solar_panel.source = "assets/solar_panel_on.jpg"
        self.ambient_sensor_toggle = not self.ambient_sensor_toggle

    def solar_charger_on_off(self):
        print("solar_charger_on_off is called.")
        if self.solar_charger_toggle:
            self.charger.power_solar_charger(False)
            self.ids.label_charging_controller.color = "grey"
            self.ids.label_charging_controller_voltage.color = "grey"
        else:
            self.charger.power_solar_charger(True)
            self.ids.label_charging_controller.color = "black"
            self.ids.label_charging_controller_voltage.color = "black"
        self.solar_charger_toggle = not self.solar_charger_toggle
    
    

class WindowManager(ScreenManager):
    pass
    
######## Follow this link to use kivyMD with original Kivy
###### https://www.youtube.com/watch?v=gW4byuP97K4
########
class KivyMD_KVApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        # self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_palette = "Teal"

        sm = ScreenManager()
        sm.add_widget(LivingRoomScreen(name="livingroom"))
        return sm
    # def on_stop(self):
    #     print('show me before kill --> ', thread_name)
    #     os.kill(self.thread_name.getpid(), signal.SIGKILL)


if __name__ == "__main__":
    app = KivyMD_KVApp()
    app.run()
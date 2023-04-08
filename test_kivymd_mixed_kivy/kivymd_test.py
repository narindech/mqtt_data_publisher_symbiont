from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.app import MDApp

from kivy.clock import Clock
from functools import partial

import air_con_class as air
import light_bulb_class as light
import ambient_sensor_class as ambient

class LivingRoomScreen(Screen):
    light_bulb_1_toggle = True
    air_con_toggle = True
    solar_panel_toggle = True
    air = air.airCon()
    light = light.lightBulb()
    ambient = ambient.AmbientSensor()

    def enter(self):
        print("enter is called.")
        event = Clock.schedule_interval(partial(self.my_callback), 1 / 30.)
        

    def my_callback(self, dt):
        # print('My callback is called', dt)
        
        air_con_value = self.air.get_consumption()
        light_con_value = self.light.get_consumption()

        ambient_con_value = self.ambient.get_consumption()
        ambient_temp_value = self.ambient.get_ambient_sensor_temp()
        ambient_humid_value = self.ambient.get_ambient_sensor_humid()
        ambient_pressure_value = self.ambient.get_ambient_sensor_pressure()

        print("show me air consumption --> ", air_con_value)
        print("get light bulb consumption: ", light_con_value)


        self.ids.label_air_con_power_consumption.text = f"Power consumption (kW): {str(air_con_value)}"
        self.ids.label_light_bulb_power_consumption.text = f"Power consumption (kW): {str(light_con_value)}"

        self.ids.label_ambient_sensor_temp.text = f"Temperature (°C) : {str(ambient_temp_value)}"
        self.ids.label_ambient_sensor_humid.text = f"Humidity (%): {str(ambient_humid_value)}"
        self.ids.label_ambient_sensor_pressure.text = f"Pressure (Bar): {str(ambient_pressure_value)}"
        self.ids.label_ambient_sensor_power_consumption.text = f"Power consumption (kW): {str(ambient_con_value)}"
        
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
        else:
            self.ids.card_solar_panel.md_bg_color = "#fecf04"
            self.ids.image_solar_panel.source = "assets/solar_panel_on.jpg"
        self.solar_panel_toggle = not self.solar_panel_toggle
    

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
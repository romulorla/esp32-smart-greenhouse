# ESP32 Smart Greenhouse UI

This project's goal was to develop an user interface for an indoor greenhouse, as part of a friend's school final year project. 
An overall view of the project can be seen in the picture bellow.

<p align="center">
<img src="https://i.ibb.co/nnQYBfR/8fc39adb-09e7-4af6-a542-473c9d740b73.jpg" alt="drawing" width="400"/>
</p>

## Hardware and working principle

On the hardware side, there's a microcontroller reading all the environment's variables such as: **temperature, humidity, pH, luminosity, water level**. The sensors utilized in this project was:
* DHT22 for reading the temperature and humidity.
* LDR for reading the luminosity.
* PH-4502C for reading the soil's pH.
* Generic water level switches to read the tank's water level.

The microcontroller sends, every second, a JSON containing all the sensors data to the ESP32 over the Serial port. The protocol used was UART due to its simplicity and ease of implementation.

On the ESP32 side, it was decided to program it with [MicroPython](https://micropython.org/) due to its fast development time. The ESP32 is responsible for reading the Serial data it is receiveing and also to host the web page containing all the greenhouse's environment data. The framework utilized to host the web page and manage the web server was [Picoweb](https://github.com/pfalcon/picoweb) due to its simplicity and familiarity with [Flask](https://flask.palletsprojects.com/en/2.1.x/).

![This is a alt text.](https://i.ibb.co/jHc82Bg/ESP32-Smart-greenhouse.png)


## User interface

The web app was developed using simple HTML and CSS. To add a little bit of interactivity for the user, it was also used [VueJS](https://vuejs.org/) as the Javascript framework together with [Vuetify](https://vuetifyjs.com/en/) for the UI components. The main goal while developing the web page was to keep it as simple and as lightweight as possible because of the limited memory available on the ESP32. Every 3 seconds, the web page sends a fetch request to a specific route on the ESP32, that sends back a JSON response containing all the measurement's data. The updated data is then binded to the HTML content on the page. 


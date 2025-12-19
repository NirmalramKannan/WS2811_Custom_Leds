# WS2811_Custom_Leds
Small Script to control 50 WS2811 digitally adressable LEDs via Raspberry PI

# Setup:

1. Wire the WS2811's dedicated power and ground wires to a seperate 5V power source uisng an adapter (Should not be from Raspberry PI)
2. Connect the siganl and ground wires of the female end of the WS2811 to the Raspberry PI. Use GPIO 18 (PCM Clk) for signal pin and any Ground pin for ground.
3. Run app.py with arguments 1, 2, 3 or 4 for different LED patterns

Python Library Dependicies (Install with pip):
1. rpi_ws281x
2. adafruit-circuitpython-neopixel


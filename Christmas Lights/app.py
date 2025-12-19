import board
import neopixel
from time import sleep
import colorsys
import random
import sys

def color_wheel_50():
    colors = []
    for i in range(50):
        h = i / 50.0
        r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        colors.append((
            int(r * 255),
            int(g * 255),
            int(b * 255)
        ))
    return colors

pixels = neopixel.NeoPixel(board.D18, 50, brightness = 1, pixel_order = neopixel.GRB)
pattern = 1

if len(sys.argv) > 1:
    try:
        pattern = int(sys.argv[1])
        if pattern not in [1, 2, 3, 4]:
            raise ValueError
    except ValueError:
        print("Usage: ./run <pattern_number>")
        print("pattern_number must be 1, 2, or 3")
        sys.exit(1)

print(f"Running pattern {pattern}")

match pattern:
#=======================================================================
	case 1:
		colors = color_wheel_50()        
		offset = 0

		while True:
			for i in range(50):
				pixels[i] = colors[(i + offset) % 50]

			pixels.show()
			offset = (offset - 1) % 50
   
#=======================================================================
	case 2:
		hue = 0.0
		HUE_STEP = 0.001
		FPS_DELAY = 0.02

		while True:
			r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
			color = (int(r * 255), int(g * 255), int(b * 255))

			pixels.fill(color)
			pixels.show()

			hue += HUE_STEP
			if hue >= 1.0:
				hue -= 1.0

			sleep(FPS_DELAY)
    
#=======================================================================
	case 3:
		NUM_PIXELS = 50
		WHITE = (0, 0, 0)
		SNAKE_LENGTH = 5
		FPS_DELAY = 0.05

		position = 0

		h = random.random()
		r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
		snake_color = (int(r * 255), int(g * 255), int(b * 255))

		while True:
			pixels.fill(WHITE)

			for i in range(SNAKE_LENGTH):
				idx = (position + i) % NUM_PIXELS
				pixels[idx] = snake_color

			pixels.show()

			position += 1

			if position >= NUM_PIXELS:
				position = 0
				h = random.random()
				r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
				snake_color = (int(r * 255), int(g * 255), int(b * 255))

			sleep(FPS_DELAY)
#=======================================================================
	case 4:
		offset = 0
		RED   = (255, 0, 0)
		GREEN = (0, 255, 0)
		BLUE  = (0, 0, 255)
		ORANGE = (255,165,0)
		YELLOW = (255,255,0)
		PURPLE = (128,0,128)
		colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
		
		while True:
			for i in range(50):
				pixels[i] = colors[(i + offset) % 6]

			offset = (offset + 1) % 6
			sleep(0.1)
				

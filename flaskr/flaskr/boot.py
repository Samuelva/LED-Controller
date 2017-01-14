# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *

# LED strip configuration:
LED_COUNT      = 180      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW

# Define functions which animate LEDs in various ways.
def boot(strip, color, wait_ms=400):
        wait_ms = 0.02
        """Wipe color across display a pixel at a time."""
        for i in range(91):
                strip.setPixelColor(i, color)
                strip.setPixelColor(181-i, color)
                strip.show()
                time.sleep(wait_ms)
        for x in range(100, -1, -5):
                strip.setBrightness(x)
                strip.show()
                time.sleep(0.020)
        time.sleep(0.1)
        for x in range(0, 255, 5):
                strip.setBrightness(x)
                strip.show()
                time.sleep(0.025)




# Main program logic follows:
if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        print ('Press Ctrl-C to quit.')
        #while True:
        # boot(strip, Color(0, 0, 0, 255), 0)  # Composite White wipe

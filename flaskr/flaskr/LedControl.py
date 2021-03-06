# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import sys
from neopixel import *

class LedControl:
    def __init__(self):   
        # LED strip configuration:
        self.LED_COUNT      = 180      # Number of LED pixels.
        LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
        LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 0
        LED_STRIP      = ws.SK6812_STRIP_RGBW

        self.status = "Off"
        
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        self.strip.begin()

    def boot(self, colour):
##        for i in range(180):
##            self.strip.setBrightness(100)
##            self.strip.setPixelColor(i, Color(0, 0, 0, 0))
##        self.strip.show()
##        for i in range(180):
##            self.strip.setPixelColor(i, Color(0, 0, 0, 0))
##            self.strip.show()
##            time.sleep(0.02)
        for i in range(self.LED_COUNT+1):
            self.strip.setBrightness(100)
            self.strip.setPixelColor(i, Color(0, 0, 0, 0))
        self.strip.show()
        for i in range(self.LED_COUNT+1):
            self.strip.setPixelColor(i, colour)
##            self.strip.setPixelColor(165-i, colour)
            self.strip.show()
            time.sleep(0.02)
##        for x in range(100, -1, -5):
##            self.strip.setBrightness(x)
##            self.strip.show()
##            time.sleep(0.020)
##        time.sleep(0.1)
##        for x in range(0, 255, 5):
##            self.strip.setBrightness(x)
##            self.strip.show()
##            time.sleep(0.025)

    def changeColour(self, colour):
        for i in range(self.LED_COUNT+1):
            self.strip.setPixelColor(i, colour)
            self.strip.show()
            time.sleep(0.01)

    def shutdown(self):
##        j = 1
##        for i in range(83, 166):
##            self.strip.setPixelColor(i, Color(0, 0, 0, 0))
##            self.strip.setPixelColor(i-j, Color(0, 0, 0, 0))
##            self.strip.show()
##            j += 2
##            time.sleep(0.02)
        for i in range(self.LED_COUNT+1, -1, -1):
            self.strip.setPixelColor(i, Color(0, 0, 0, 0))
            self.strip.show()
            time.sleep(0.02)

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status


# Main program logic follows:
#if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
        # Intialize the library (must be called once before other functions).

        # print ('Press Ctrl-C to quit.')
        #while True:
        #boot(strip, Color(0, 0, 0, 255), 0)  # Composite White wipe

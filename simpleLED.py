import RPi.GPIO as GPIO
LED = 21

# NeoPixels must be connected to D10, D12, D18 or D21 to work.
#pixel_pin = board.D21
# The number of NeoPixels
#num_pixels = 24
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
#ORDER = neopixel.GRB

#pixels = neopixel.NeoPixel(
#    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
#)


GPIO.setmode(GPIO.BCM)

for i in range(5):
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(20, GPIO.LOW)
    time.sleep(0.5)
#!/usr/bin/python

from Tkinter import *

root = Tk()
root.title("Elentirmo Observatory Controller v0.1")
dust_cover_text = StringVar()
dust_cover_text.set('Cover Closed')

flat_box_text = StringVar()
flat_box_text.set('Flat Box Off')

dslr_text = StringVar()
dslr_text.set('DSLR Off')

roof_text = StringVar()
roof_text.set('Roof closed')

# Tweeting Setup
global tweet_text
import sys
from twython import Twython
CONSUMER_KEY = 'oQsRvuBMJaCfbvXHjgjQ'
CONSUMER_SECRET = 'Im2K2iATjFWyZE07ApNBQy0vXhAMmyLFZ2AFynq6UY'
ACCESS_KEY = '2341986678-ZGuDmP9NcswzKDHlMl1d7fT7tZJEclqCZrGDGpc'
ACCESS_SECRET = 'cb42X2lgMMGhbQZYdVdI1PuHFkESO6ZnWoZP5Ipd0c30N'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
import time
print (time.strftime("%Y.%m.%d-%H:%M:%S"))

def tweet():
    #print "Tweeting now..."
    import os
    api.update_status(status=time.strftime("%Y.%m.%d-%H:%M:%S") + " - " + tweet_text)
    return;

def dust_cover_open():
    #print "Opening dust cover"
    global tweet_text
    ## Open a serial connection with Arduino.
    import time
    import serial
    ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using
    time.sleep(3)                       # Wait 3 seconds for Arduino to reset
    print ser                           # Print serial config
    print "Sending serial command to OPEN the dust cover."
    ser.write("O")
    print "Opening serial connection."
    ser.close()
    # Reminder to close the connection when finished
    if(ser.isOpen()):
     print "Serial connection is still open."
    dust_cover_label.config(bg="Green")
    dust_cover_text.set('Cover is Open')
    tweet_text = "Dust cover is open."
    tweet()

def dust_cover_close():
    print "Closing"
    ## Open a serial connection with Arduino.
    import time
    import serial
    ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using
    time.sleep(3)                       # Wait 3 seconds for Arduino to reset
    print ser                           # Print serial config
    print "Sending serial command to CLOSE the dust cover."
    ser.write("C")
    print "Closing serial connection."
    ser.close()
    # Reminder to close the connection when finished
    if(ser.isOpen()):
     print "Serial connection is still open."
    dust_cover_label.config(bg="red")
    dust_cover_text.set('Cover is closed')
    tweet_text = "Dust cover is closed."
    tweet()
    
def flat_on():
    print "Activating flat box"
    ## Open a serial connection with Arduino.
    import time
    import serial
    ##ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using
    time.sleep(3)                       # Wait 3 seconds for Arduino to reset
    print ser                           # Print serial config
    print "Sending serial command to turn on the flat box via relay."
    ser.write("Q")
    print "Opening serial connection."
    ser.close()
    # Reminder to close the connection when finished
    if(ser.isOpen()):
     print "Serial connection is still open."
    flat_box_label.config(bg="Green")
    flat_box_text.set('Flat Box on')
    tweet_text = "Lightbox is on."
    tweet()

def flat_off():
    print "Dectivating flat box"
    ## Open a serial connection with Arduino.
    import time
    import serial
    ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using
    time.sleep(3)                       # Wait 3 seconds for Arduino to reset
    print ser                           # Print serial config
    print "Sending serial command to turn off the flat box via relay."
    ser.write("F")
    print "Opening serial connection."
    ser.close()
    # Reminder to close the connection when finished
    if(ser.isOpen()):
     print "Serial connection is still open."
    flat_box_label.config(bg="red")
    flat_box_text.set('Flat Box Off')
    tweet_text = "Lightbox is off."
    tweet()

def dslr_on():
    print "Activating DSLR"
    ## Open a serial connection with Arduino.
    import time
    import serial
    ##ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using
    time.sleep(3)                       # Wait 3 seconds for Arduino to reset
    print ser                           # Print serial config
    print "Sending serial command to turn on the dslr relay."
    ser.write("D")
    print "Opening serial connection."
    ser.close()
    # Reminder to close the connection when finished
    if(ser.isOpen()):
     print "Serial connection is still open."
    dslr_label.config(bg="Green")
    dslr_text.set('DSLR on')
    tweet_text = "DSLR is on."
    tweet()

def dslr_off():
    print "Dectivating DSLR"
    ## Open a serial connection with Arduino.
    import time
    import serial
    ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using
    time.sleep(3)                       # Wait 3 seconds for Arduino to reset
    print ser                           # Print serial config
    print "Sending serial command to turn off the dslr via relay."
    ser.write("M")
    print "Opening serial connection."
    ser.close()
    # Reminder to close the connection when finished
    if(ser.isOpen()):
     print "Serial connection is still open."
    dslr_label.config(bg="red")
    dslr_text.set('DSLR Off')
    tweet_text = "DSLR is off."
    tweet()

def roof_open():
    print "Opening roof"
    ## Open a serial connection with Arduino.
    import time
    import serial
    ##ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using
    time.sleep(3)                       # Wait 3 seconds for Arduino to reset
    print ser                           # Print serial config
    print "Sending serial command to open the roof."
    ser.write("1")
    print "Opening roof."
    ser.close()
    # Reminder to close the connection when finished
    if(ser.isOpen()):
     print "Serial connection is still open."
    roof_label.config(bg="Green")
    roof_text.set('Roof open')
    tweet_text = "Roof open."
    tweet()

def roof_close():
    print "Opening roof"
    ## Open a serial connection with Arduino.
    import time
    import serial
    ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using
    time.sleep(3)                       # Wait 3 seconds for Arduino to reset
    print ser                           # Print serial config
    print "Sending serial command to open the roof."
    ser.write("M")
    print "Opening serial connection."
    ser.close()
    # Reminder to close the connection when finished
    if(ser.isOpen()):
     print "Serial connection is still open."
    roof_label.config(bg="red")
    roof_text.set('Roof closed')
    tweet_text = "Roof is closed."
    tweet()

#Buttons
open_dust_cover_btn = Button(text=" Open Dust Cover ", width=15, command=dust_cover_open)
open_dust_cover_btn.grid(row=1, column=1)

close_dust_cover_btn = Button(text=" Close Dust Cover ", width=15, command=dust_cover_close)
close_dust_cover_btn.grid(row=1, column=2)

flat_box_on_btn = Button(text="Turn On Lightbox", width=15, command=flat_on)
flat_box_on_btn.grid(row=2, column=1)

flat_box_off_btn = Button(text="Turn Off Lightbox", width=15, command=flat_off)
flat_box_off_btn.grid(row=2, column=2)

dslr_on_btn = Button(text="Turn On DSLR", width=15, command=flat_on)
dslr_on_btn.grid(row=3, column=1)

dslr_off_btn = Button(text="Turn Off DSLR", width=15, command=flat_off)
dslr_off_btn.grid(row=3, column=2)

roof_open_btn = Button(text="Open roof", width=15, command=flat_on)
roof_open_btn.grid(row=4, column=1)

roof_close_btn = Button(text="Close roof", width=15, command=flat_off)
roof_close_btn.grid(row=4, column=2)

#Labels

dust_cover_label = Label(root, textvariable=dust_cover_text, width=15, fg="Black", bg="Red")
dust_cover_label.grid(row=1, column=0)

flat_box_label = Label(root, textvariable=flat_box_text, width=15, fg="Black", bg="Red")
flat_box_label.grid(row=2, column=0)

dslr_label = Label(root, textvariable=dslr_text, width=15, fg="Black", bg="Red")
dslr_label.grid(row=3, column=0)

roof_label = Label(root, textvariable=roof_text, width=15, fg="Black", bg="Red")
roof_label.grid(row=4, column=0)

root.mainloop()

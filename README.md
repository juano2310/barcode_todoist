# Barcode Scanner, Semantics3 and Todoist
Using a USB barcode scanner you can scan an item, get the product name from Semantics3 and add it to a list on Todoist.

Every time I run out of something I just scan it and it adds it to my "Shopping" list that I also share with my wife. 

For this project I used a Raspberry Pi and Adafruit Barcode Reader/Scanner Module - CCD Camera - USB Interface (https://www.adafruit.com/products/1203)


#### Boot on start up:

The challenge here is that it needs to listen for keyboard events so it has to run in the foreground. 

- First we need to add two lines to /etc/profile 

<code>sudo nano /etc/profile</code>

sleep 10  
python /home/pi/barcode.py

- Press ctrl X to exit and Y to save
- Restart the Pi

<code>sudo reboot</code>

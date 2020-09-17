## Diagram
![Untitled_Diagram](uploads/73d5b09daf8569e592f4586a9afb3a2f/Untitled_Diagram.png)

## LED Startup
When the table first starts via startup.sh the led_startup.py script runs. Which will fade the LEDs to the strip's primary color and then fade to off afterwards. This runs pretty independently of the rest of the lights module and only runs when the startup.sh script is run when the table first starts up.

## LED Main
led_main.py gets spawned as a child process of the main sisbot express server if the table is configured to use LEDs. The sisbot server will then connect to a socket that gets created in led_main.py using the Link Control Protocol LCP. To change different parameters related to the LEDs the sisbot server will write data to /tmp/sisyphus_sockets on the Raspberry PI and led_main.py will read data from /tmp/sisyphus_sockets and change the LEDs accordingly. The parameters to set the LED offset from theta, set the LED pattern, and the LED color are controlled by the main sisbot object in sisbot.js. Also, the current rho and theta are also written to the LCP socket in the plotter module (plotter.js) and is read by led_main.py.

Also, before the socket data gets read in led_main.py. A startup sequence similar to led_startup.py gets run where the LEDs will fade the LEDs to the primary color and then to off unless the -q (Quick) command line arg is given. The LED strip gets instantiated as a Adafruit_NeoPixel object. Finally, after the socket data is read the LED brightness is updated if needed and the current LED pattern is updated.

## Patterns
LED patterns get passed and read by led_main given a specific name of a pattern without the .py extension. led_main.py will dynamically import and call the pattern's init and update method which are required on each of the patterns. The init method will initialize the pattern and the ball's current theta and rho position get passed to the method if the pattern relies on information the ball. The update method will then advance through one transition of the current pattern which will happen on each run through of the main program loop. Arguments passed to the update method then include the new theta and rho of the ball if the pattern uses data from the ball, the current brightness, the primary and secondary color for the LEDs, the number of balls, and the current LED strip object.

## Color Functions
The color functions module contains common methods related to changing the color of the LEDs. The current available color functions allow 2 colors to be blended together, allows for pixels to be filled with just one color, allows for pixels to be whiped, and allows for the strip to be set using rainbow colors.

## Easing
The easing module contains common methods related to easing the colors of the LED lights.
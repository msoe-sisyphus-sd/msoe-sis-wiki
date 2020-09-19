## Development Setup
The sisyphus table requires both network visibility and internet access. This is impossible to achieve by attaching the sisyphus table to the MSOE wifi network, but this can be achieved by connecting an MSOE laptop to MSOE wifi, and then using the hotspot feature on the laptop. Note that this is an interim solution until we can solidify plans with IT or Dr. Schilling to move the table to Cybersecurity lab and enable a form of remote access.

## Turn Windows 10 MSOE Laptop into a Hotspot

1) Go to Settings > Left Menu > Mobile hotspot
2) Toggle the hotspot to "On"
3) Share the internet connection from the Wi-Fi adapter.
4) Set up a more recognizable network name, not the MSOE-XYZ123 default.
5) Set a secure Network password.
6) Make sure the Network band is set to 2.4Ghz. The table does not have a 5Ghz band and will not see the network if you select anything except 2.4Ghz.
![image](uploads/d34c63fb4cfa92a49bfd3bde8cffb6e7/image.png)

^^example setup (with simple, insecure password--please make yours more secure :) )

## Connect the Sisyphus table to the Hotspot
1) The sisyphus table will come up in AP mode when it can't find a wifi network it has on file. This is called "SeniorDesignTable."
2) Connect the team phone to the SeniorDesignTable wifi. 
![image](uploads/3d7995d42abc3957bc1675a7741d5f3d/image.png)
3) Go to the Sisyphus app, and connect to the table. It'll look something like this:
![image](uploads/0d516dafbc20d9d402773101c31b5a4c/image.png)

4) Hit "Connect to Wifi"
5) Type in the credentials you created for your MSOE laptop hotspot.
6) The table will say "attempting to connect to router." In this case the "router" the table is connecting to is the router your MSOE laptop is creating :)
7) Switch the phone's wifi over to the hotspot's network.
8) Open back up the Sisyphus app and see if you can connect to the table. In some cases, I found I had to reboot the table in order for the table to fully sign onto the laptop's hotspot.

## SSH Into the Sisyphus Table
1) First, find the IP of the Sisyphus table (Windows 10 hotspots do not handle local DNS resolution very well, or if they do I don't know how to set it up)

![image](uploads/97b0a3762f60260c24f7bc974249adf9/image.png)

^^ I did this using nmap. If you don't have nmap installed on your PC, there might be other ways to do this, but I'm not sure. For me the sisyphus table didn't show up in the Windows 10 "devices list."

** Note that windows laptop hotspots use a netmask of 255.255.255.0 by default. I don't think this is changeable, so when you do your nmap be sure to use a netmask of /24, otherwise it won't work :)

Image of SSH Working, using the IP from the previous screenshot:

![image](uploads/d18832a75a80e3b9f13f176d448117dc/image.png)

## Oh no! It's Not Working!
* if the steps above didn't work for you, double-check the device list on your hotspot.
![image](uploads/d84b2ae5b2c779ae7ebb9bb45bf82166/image.png)

Verify that something (your personal phone or the team phone) can connect to your MSOE Laptop.
  * if no devices can connect to your MSOE laptop's hotspot, you may need to double-check your adapter settings.
![image](uploads/1b636cc303660e10fbfd2289e2a14479/image.png)

  * double check that the properties of your wifi adapter are set to the following under the "sharing" tab:
![image](uploads/5b486f9b5f33f6d09acdaed01104a653/image.png)

  * For sanity purposes, uncheck everything, recheck everything, then hit "OK"
  * Now try connecting an external device to your laptop's hotspot. If this works, then go ahead and try from "Connect the Sisyphus Table to the Hotspot." If this doesn't work, you most likely have a problem with your Wifi adapter. In some cases, a driver update can help. In other cases, restarting your computer might refresh this wireless interface. 




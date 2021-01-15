Connecting to the table via SSH:

  1. connect using ssh to `pi@seniordesigntable.msoe.edu`
  2. use the password `sisyphusrpi`
  

Controlling the table via Webapp API:

  1. install Postman (on desktop, website doesn't work)
  2. downlload json setup: {todo}
  3. change URL to: `http://seniordesigntable.msoe.edu:3002/` + the URI
  4. if still having issues, contact a team member
  
Changing light pattern

  1. use `ps aux | grep python | grep -v grep` to locate previously running light pattern
  2. use `sudo kill -9` to kill the previous process
  3. from `sisbot/content/lights` run `sudo python led_main.py -q -n 167 -p $p &` where $p is the pattern name (without the .py file extension)
  
  
Changing track

  1. Find the track id associated with the track (the filename of the track in `sisbot/content/tracks`)
  2. Use Postman to issue a `set_track` request where the body's data's id is the track id
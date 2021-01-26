<!-- Okay really SAQ: Stuart Asked Questions -->

As you are following the steps in the readme, you may hit a few roadbumps. Here are some common ones

# PyAudio not installing
If you run into an issue with pip not being able to find portaudio.h, you have to manually install it via:
`sudo apt install portaudio19-dev python-pyaudio` then re-run `pip intall pyaudio`

# HOST and PORT
The HOST and PORT variables on the server.py should point to the address of main.py and vise versa. Main.py is the client, and so should be run on whatever machine is doing the recording. Server and server-ml are  
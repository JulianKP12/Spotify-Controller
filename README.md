# Spotify-Controller
An Arduino + Python based Spotify Controller


## About

This is mostly a personal project with which i can control my spotify 
through an arduino. Since some friends have brought up the idea I
might just make a library for the spotify API as a fun project.

This project does not have pretty code though as it was 3AM and
it was being mean and besides that, this is a personal project
that I don't plan on adding new features to

## Schematic
![Image of the schematic](/schematic.png)
###### I'm not an electrical engineer don't bully me

## How to use

First of all poor you, second of all you need Python 3 and the following libraries:
```
pip install flask==1.1.2
pip install serial
```

Run the app.py script and go to http://localhost:5000/, from there
just follow the provided steps. Once logged in, you should be ready to go

The button functionalities, ranging from left to right, are:
Previous song, Pause, Next song

# Team ILLUMINATI - Myntra HackerRamp
## Component 1 - Crowd Detection and People Counter
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

For our complete submission, headover to - https://github.com/swatig23/myntra_ILLUMINATI
This is the first component of our project - *Crowd Detection and People Counter (CDPC)*

Before going further please see the demo - [Demo](https://photos.app.goo.gl/MZWZxMSfPf9UQooGA)

# Features!

  - Easy 5 step setup on your local PC.
  - Interactive Command Line API for fast usage.
  - Advanced Centroid Tracking Algorithm to identify people and track them.
  - 34 FPS. Can run at 60 FPS if RAM allows.

You can also:
  - Use this as an API!
  - Use your webcam and/or an external camera for mask detection using our Command Line Arguements.


# Tech

Our CDPC uses a number of open source projects and libraries to work properly:

* Tensorflow - For training our DL Model.
* Keras - For helping us evaluate our DL Model
* Open CV - For Face Recognition and all our computer vision needs.
* Caffe - A deep learning framework made with expression, speed, and modularity in mind. Used for Detecting and tracking people.
* Mobile Net SSD - Pretrained DL Model

# Installation

We have tried to keep the installation process as simple as possible. Please keep note of the following points:

* Please follow the exact steps.The App is tested and verified only if each step is followed.
* First time deployment of app might take 1 -2 minutes.
* Note that all commands are to be entered with Admin Permissions in the command line.

Step 1 - Clone the Repository.
```sh
$ git clone https://github.com/Prabhav55221/ILLUIMINATI-Crowd-Detection.git
$ cd ILLUMINATI-Crowd-Detection
```

Step 2 - Create Virtual Env and Download Reqs.
```sh
$ mkvirtualenv tester
$ pip3 install -r requirements.txt
OR
$ mkvirtualenv tester
$ pip install -r requirements.txt
```

And that's it! You are done. Let's now get this working.

# Working

##### API Mode - For all you devs out there

Step 1: CD into the folder
Step 2: Now you can use both __VIDEO__ and __WEBCAM MODE__ by entering the following code.

> __Video Mode__ (Pass any video path as input)
> Once you run the below code, the APP will ask for a choice. Choose 1 for video
> Incase you face any issues passing local path, add the video to /videos folder and pass in videos/name.mp4
```sh
$ python3 app.py
OR
$ python app.py
```

> __Webcam Mode__
> Once you run the below code, the APP will ask for a choice. Choose 2 for webacam.
```sh
$ python3 app.py
OR
$ python3 app.py
```

# That's it !

Team Illuminati
NSUT, Delhi

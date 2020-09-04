# license plate recognition

# VEHICLE RECOGNITION , LICENSE PLATE , Brand , YEAR AND MORE! 
This  project focuses on "Vechicle recognition , using opencv , skit image  using  openalpr API  
 The entire video with demonstation of each and every part (in realtime) is available in my YouTube Channel <a href="https://www.youtube.com/watch?v=79MWFko1hUA&t=52s&ab_channel=LeonBogod"> Leo Bogod Youtube Channel </a>

# OpenALPR API and OpenCV   is used as a base for object recogntion on this project, more info can be found on this [repo](https://github.com/ahmetozlu/tensorflow_object_counting_api).***

---
<p align="center">
  <img src="https://github.com/LeoBogod22/License_Plate_Recognition/blob/master/Screenshot_18.png">
</p>
<br></br>

  <img src="https://github.com/LeoBogod22/License_Plate_Recognition/blob/master/Screenshot_15.png"><br></br>
  
  <img src="https://github.com/LeoBogod22/License_Plate_Recognition/blob/master/Screenshot_20.png">

This project has more features than just licenes plate detection, here are some additional feautres 

- Recognition of approximate vehicle color
- Recognition of approximate vehicle brand 
- Recognition of approximate vehicle year 
 - Import all images from folder making it easy to analyze multiple images at once
 Prediction of approximate vehicle size height and length 
 
 
 ToDos:

- More powerful detection models will be shared.
- Make the algorithm work with video  instead of picture only 
- Code cleanup will be performed.


## Theory

### System Architecture

- Vehicle color prediction has been developed using OpenCV via K-Nearest Neighbors Machine Learning Classification Algorithm is Trained Color Histogram Features, [see](https://github.com/ahmetozlu/vehicle_counting_tensorflow/tree/master/utils/color_recognition_module) for more info.

- License plate extraction was created with openCV and East Text recogntion Library + pyteseract for converting image to string.  




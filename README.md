# BiolaFacialRecognition
Searches the Biola directory for matches.

createEncodings.py creates the encodings for all of the photos in the directory and saves them so that searches are faster.

biolaFacialRecognition.py contains the script to import photos to compare against the directory. Checks against encodings, gradually increasing similarity strictness until only one result remains.

![Screenshot of output](https://i.imgur.com/qtjXmDq.png)

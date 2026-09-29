Badminton Court Movement Heatmap

Problem

In badminton, players move around different parts of the court during a rally. It can be useful for players and coaches to know which areas of the court a player visits the most. However, checking a video frame by frame and noting the player's position manually takes a lot of time.

Proposed Solution

The idea of this project is to use computer vision to track a badminton player from a video. The system detects the player and records their position as they move around the court. The position from each frame is converted into coordinates and stored for further analysis.

Using this data, the project creates a movement heatmap. The heatmap makes it easier to see which areas of the badminton court the player spends more time or moves through more often.

Target Users

This project can be useful for:

- Badminton players who want to understand their movement
- Coaches who want to analyse a player's court coverage
- Sports students working on sports analysis
- Beginners who are interested in using technology for sports

Main Features

1. Taking a badminton video as input
2. Detecting and tracking one player in the video
3. Extracting the player's position frame by frame
4. Saving the movement coordinates in a CSV file
5. Generating a movement heatmap
6. Displaying the movement on a badminton court

Scope

For the current version, the project focuses on tracking only one player and showing their movement on a badminton court. The main goal is to make it easier to understand the player's movement without having to manually check the entire video.

In the future, the project can be extended with features such as shot detection, tracking both players, calculating movement statistics, and adding a graphical user interface to make the system easier to use.
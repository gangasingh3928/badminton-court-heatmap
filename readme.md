Badminton Court Movement Heatmap

Problem

In badminton, players constantly move between different areas of the court during a rally. Knowing which parts of the court a player uses most can be helpful for both players and coaches. However, watching a video frame by frame and recording the player's position manually can take a lot of time.

Proposed Solution

This project uses computer vision to track a badminton player from a video. The system detects the player and follows their movement throughout the video. It records the player's position in each frame, converts it into coordinates, and saves the data for analysis.

The collected data is then used to create a movement heatmap. This makes it easier to see which areas of the court the player visits most often and where they spend more time during the game.

Target Users

This project can be useful for:

- Badminton players who want to understand their movement patterns
- Coaches who want to analyse a player's court coverage
- Sports students working on video-based sports analysis
- Beginners interested in applying technology to sports

Main Features

1. Taking a badminton video as input
2. Detecting and tracking one player in the video
3. Extracting the player's position frame by frame
4. Saving the movement coordinates in a CSV file
5. Generating a movement heatmap
6. Displaying the movement on a badminton court

Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib
- YOLO
- CSV

Project Workflow

Video
→ Player Detection
→ Player Tracking
→ Coordinate Extraction
→ CSV Storage
→ Court Mapping
→ Heatmap

Installation

Install the required packages using:

pip install -r requirements.txt

Running the Project

Place the badminton video inside the "videos" folder.

Run the tracking program:

python track_player.py

After that, generate the court heatmap by running:

python court_map.py

Output

The project generates the following files:

- "player_positions.csv"
- "player_heatmap.png"
- "badminton_heatmap.png"

The CSV file contains the player's recorded positions, while the image files show the player's movement on the court.

Scope

The current version of the project focuses on tracking one player and displaying their movement on a badminton court. The main aim is to make it easier to understand a player's movement without manually checking the entire video.

Future Enhancements

In the future, the project could be improved by adding:

- Automatic court detection
- Shot detection
- Smash and drop analysis
- Tracking of multiple players
- Movement statistics
- A graphical user interface
- Support for multiple videos

Conclusion

This project shows how computer vision can be used for badminton video analysis. By detecting and tracking a player, recording their coordinates, and displaying the results as a heatmap, it provides a simple way to study court movement and understand how a player uses different areas during a game.

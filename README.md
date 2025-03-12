# Video Editing Helper

## Overview
Video Editing Helper is a Python script that renames video files based on the default names assigned by a phone. It extracts the date from the filename and renames the files in a structured format, making it easier to organize video clips for editing.

## Features
 - Automatically detects video files in a specified directory
 - Extracts the recording date from the filename (if available)
 - Renames files in the format:
```
FolderName Day X (Y).ext
```
 - Day X represents the number of days since a defined START_DATE
 - (Y) is a sequential number for multiple videos from the same day

# Usage
1. Configure the Script
 - Set the START_DATE variable to match the first recording date.
 - Update the video_dir variable with the path to your video folder.
 - Add any additional video file extensions to the VIDEO_EXTENSIONS list if needed.
2. Run the Script
 - Execute the script using Python:

```
python video_editing_helper.py
```
The script will rename files in the specified directory according to the naming convention.

## Example
Before:
```
VID_20250201_123456.mp4  
VID_20250202_141234.mp4  
VID_20250202_151234.mp4  
```
After:
```
Lifting Day 2 (1).mp4  
Lifting Day 3 (1).mp4  
Lifting Day 3 (2).mp4
```
## Notes
 - Ensure the script has permission to rename files in the target directory.
 - If no date is found in a filename, the script will skip that file.
 - Adjust the regex pattern in extract_date_from_filename() if your phone uses a different filename format.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


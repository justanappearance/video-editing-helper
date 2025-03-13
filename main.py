import datetime
import glob
import os
import re

# Configuration
START_DATE = datetime.date(2025, 1, 30)  # Adjust to match your first recording
# TARGET_LENGTH = 60  # Clip length in seconds
VIDEO_EXTENSIONS = ["mp4", "mov", "avi"]


def get_video_files(directory):
    """Get all video files in the directory."""
    files = []
    for ext in VIDEO_EXTENSIONS:
        files.extend(glob.glob(os.path.join(directory, f"*.{ext}")))
    return sorted(files)


def extract_date_from_filename(filename):
    # Regular expression to match the date part (YYYYMMDD) in the filename
    match = re.search(r"\d{8}", filename)  # Looks for an 8-digit number (YYYYMMDD)

    if match:
        # Extract the date string (e.g., '20250131')
        date_str = match.group(0)

        # Convert the date string to a datetime object
        extracted_date = datetime.datetime.strptime(date_str, "%Y%m%d").date()
        return extracted_date
    else:
        print(f"No date found in {filename}")
        return None


def rename_videos(directory):
    """Rename videos in the format 'FolderName Day X (Y).ext'."""
    video_files = get_video_files(directory)
    renamed_files = []

    # Use os.path to extract the folder name from the directory path
    folder_name = os.path.basename(os.path.normpath(directory))

    for file in video_files:
        # Extract date from filename or manually set it
        file_date = extract_date_from_filename(
            file
        )  # Adjust based on naming convention

        if not file_date:
            continue
        day_number = (file_date - START_DATE).days + 1  # Calculate "Day X"

        # Use os.path to split the file name and extension
        base_name, ext = os.path.splitext(os.path.basename(file))
        new_name = f"{folder_name} Day {day_number} ({len(renamed_files) + 1}){ext}"
        new_path = os.path.join(directory, new_name)

        os.rename(file, new_path)
        renamed_files.append(new_path)

    return renamed_files


if __name__ == "__main__":
    video_dir = "/mnt/e/Video Editing/Footage/Sax Practice"  # Change this
    renamed_files = rename_videos(video_dir)
    print("Processing complete!")

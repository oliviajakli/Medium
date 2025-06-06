# Author: Olivia Jákli
# Example #2
# Rename image files based on their PLU (Price Look-Up) codes and optional count numbers.
import re
from pathlib import Path


images = [
    Path("images/12345_image.jpg"),
    Path("images/67890_image.png"),
    Path("images/12345_2_image.jpg"),
    Path("images/invalid_image.txt"),
    Path("images/12345_invalid.jpg")
]

for image_path in images:
    try:
        # Extract PLU and potential count from filename (without extension)
        original_name = image_path.stem

        # Use regex to extract PLU and optional count numbers.
        # This pattern looks for digits at the start of the filename (PLU),
        # followed by optional non-digit characters, then optional digits (count).
        match = re.match(r'^(\d+)([^\d]*)(\d*)$', original_name)

        if not match:
            print(f"Could not parse PLU from filename: {original_name}")
            
    except Exception as e:
        print(f"Failed to rename {image_path}: {str(e)}")
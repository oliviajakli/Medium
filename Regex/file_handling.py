import re
from pathlib import Path
import logging
import sys

# Set up logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

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

        # Use regex to extract PLU and any count numbers after it
        # This pattern looks for digits at the start of the filename (PLU)
        # followed by optional non-digit characters and then optional digits (count)
        match = re.match(r'^(\d+)([^\d]*)(\d*)$', original_name)

        if not match:
            logger.warning(f"Could not parse PLU from filename: {original_name}")
            
    except Exception as e:
        logger.error(f"Failed to rename {image_path}: {str(e)}")
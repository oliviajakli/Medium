# Author: Olivia Jákli
# Example #2
# Rename image files based on their SKU and optional count numbers.
import re
from pathlib import Path


images = [
    Path("images/12345.jpg"),
    Path("images/67890-1.png"),
    Path("images/67890-2.png"),
    Path("images/12121-1.webp"),
    Path("images/12121-2.webp"),
    Path("images/12121-3.webp")
]

product_names_dict = {
    "12345": "Red Sweater",
    "67890": "Blue Jeans",
    "12121": "Black Tank Top"
}


for image_path in images:
    
    original_name = image_path.stem
    # Use regex to extract PLU and optional count numbers.
    # This pattern looks for digits at the start of the filename (SKU),
    # followed by optional non-digit characters, then optional digits (count).
    match = re.fullmatch(r'(\d{5})(-\d)?', original_name)

    if not match:
        print(f"Could not parse SKU from filename: {original_name}")
        continue

    sku, count = match.groups()

    if sku in product_names_dict:
        product_name = product_names_dict[sku].replace(" ", "-") 
    else:
        product_name = "Unknown-Product"
    if count:
        new_name = f"{sku}-{product_name}{count}{image_path.suffix}"
    else:
        new_name = f"{sku}-{product_name}{image_path.suffix}"
    # Create new path with the updated name.
    new_path = image_path.parent / new_name
    print(f"Renaming {image_path} to {new_path}")
    image_path.rename(new_path)
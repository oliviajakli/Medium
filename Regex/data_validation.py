# Author: Olivia Jákli
# Example #1
# User inputs a Coordinate Reference System (CRS) in the format "EPSG:XXXX", 
# where XXXX is a 4-digit number.
import re

usr_in = input("Enter CRS: ").strip()

# Regular expression to match the CRS format
crs_pattern = r"^EPSG:\d{4}$"
if re.match(crs_pattern, usr_in):
    print("Valid CRS format.")
else:
    print("Invalid CRS format. Please enter in the format 'EPSG:XXXX' " \
    "where XXXX is a 4-digit number.")

# Author: Olivia Jákli
# Example #3
# Parse a log file for specific error messages using regex.
import re

log = """
2025-01-01 10:30:45 ERROR: Database connection failed
2025-01-01 10:31:00 INFO: User logged in successfully
2025-01-01 10:32:15 WARNING: Low disk space
2025-01-01 10:33:20 ERROR: File not found
2025-01-01 10:34:05 INFO: Data backup completed
2025-01-01 10:35:30 ERROR: Connection timeout after 30 seconds
2025-01-01 10:36:00 INFO: System rebooted
"""

if re.search(r'ERROR.*connection', log, re.IGNORECASE):
    print("An error related to connection was found in the log.")
else:
    print("No connection-related errors found in the log.")
'''
==============================================
Project name: Project November
Author name: Aradoxis
Date: 2025-01-13
Description: Updates the user's discord status with the percentage completed of the given 
time period OR with seconds until the given end time. 
Only works when current time is within the given time period.
==============================================
'''

# -----------Imports-----------
import time, requests

# ----------Constants----------

# This string must be taken from the user's authorization field
AUTHORIZATION_CODE = ""

# Starting time in seconds since the epoch
THE_BEGINNING = 1730433600

# Ending time in seconds since the epoch
THE_END = 1733029200

# Time between status updates in seconds
FREQUENCY = 3

# Type of message status will update to
# PDONE - Percentage of the time period: (THE_BEGINNING - THE_END) completed so far
# SLEFT - Seconds left until THE_END, THE_BEGINNING is ignored
# TEST  - Prints the date and time represented by THE_BEGINNING and THE_END to the console once
VALUE = "TEST"

url = "https://discord.com/api/v8/users/@me/settings"

def ChangeStatus(message):
    """
    ------------------------------------------
    Description:
    Sets the user's status to the given value.
    ------------------------------------------
    Args:
        message (string): new status
    ------------------------------------------
    """
    
    header = {
        "authorization" : AUTHORIZATION_CODE
    }
    
    jsonData = {
        "status": "online",
        "custom_status": {
            "text": message
        }
    }
    
    requests.patch(url, headers=header, json = jsonData)
    
    return

while VALUE == "PDONE":
    pdone = (time.time() - THE_BEGINNING) / (THE_END - THE_BEGINNING) * 100
    ChangeStatus(f"Percent done: {pdone:.6f}%")
    time.sleep(FREQUENCY)
    
while VALUE == "SLEFT":
    left = THE_END - time.time()
    ChangeStatus(f"Seconds left: {left:.0f}")
    time.sleep(FREQUENCY)
    
if VALUE == "TEST":
    print(f"THE_BEGINNING: {time.ctime(THE_BEGINNING)}")
    print(f"THE_END: {time.ctime(THE_END)}")
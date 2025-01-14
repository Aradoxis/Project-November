# Project_November
 A python program that updates the user's discord status every x seconds to either percent done through a time period or seconds left until the end of it.

## How to setup:

1. Ensure that your computer has python installed including the requests library.
    - Download the latest version of python [here](https://www.python.org/downloads/).
    - To install the requests library, paste this into command prompt: `python -m pip install requests`
2. Extract the zip and open the `project_november.py` file in any IDE or text editor.
3. On line 18, enter your discord account's authorization code inside the quotation marks. Instructions on how to find your account's authorization code are as follows:

    - Open discord through your web browser and press the hotkey to open inspect element (`ctrl+shift+i` on Google Chrome).
    - Navigate to the "Network" tab at the top.
    - Switch servers and open direct messages to let some requests populate.
    - Look in the inspect menu for the panel titled "Name" and click on a request with a "?" in it (usually those requests contain your auth code).
    - In the panel to the right of the Name panel, make sure the tab "Headers" is selected.
    - Look down the left side of the headers panel for "Authorization:". The value to the left of it is your auth code. If you don't see it, try a different request.

    #### DO NOT SHARE YOUR AUTH CODE WITH ANYONE!!!

    Anyone with access to your auth code can access your account data.
4. Change `THE_BEGINNING` and/or `THE_END` to the time(s) you want as the number of seconds since the epoch. You can use the converter at [epochconverter](https://www.epochconverter.com/) or trial and error using the "TEST" setting.
5. Change FREQUENCY to the amount of seconds you want between each time the status is updated.
6. Change VALUE to the setting you want:
    - PDONE - Percentage of the time period completed so far.

        ![Screenshot of pdone status](/images/screenshot_pdone.png)

    - SLEFT - Seconds left until THE_END, THE_BEGINNING is ignored.

        ![Screenshot of sleft status](/images/screenshot_sleft.png)

    - TEST  - Prints the date and time represented by THE_BEGINNING and THE_END to the console once.

        ![Screenshot of test console output](/images/screenshot_test.png)

7. With that all completed, run the program. If you are using the test setting, you can run it again after changing the value to fix any errors you might have done. If you are using any other setting, congrats! You now have a status that updates automatically! Feel free to edit the `project_november.py` file however you want.

The program can be interrupted by either entering `ctrl+c` into the console or turning off your computer.
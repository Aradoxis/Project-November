# Project_November
 A Python program that updates the user's discord status every x seconds to either percent done through a time period or seconds left until the end of it.

 ![Screenshot of pdone status](/images/screenshot_pdone.png)
 ![Screenshot of sleft status](/images/screenshot_sleft.png)

## How to setup:

1. Ensure that your computer has Python installed including the requests library.
    - Download the latest version of Python [here](https://www.python.org/downloads/).
    - To install the requests library, paste this into the command prompt: `python -m pip install requests`
---
2. Extract the zip and open the `project_november.py` file in any IDE or text editor.
---
3. On line 18, enter your discord account's authorization code inside the quotation marks. Instructions on how to find your account's authorization code are as follows:

    - Open Discord through your web browser and press the hotkey to open the inspect element menu (`ctrl+shift+i` on Google Chrome).
    - Navigate to the "Network" tab at the top.
    - Switch servers and/or open direct messages to let some requests populate.
    - Look in the inspect menu for the panel titled "Name" and click on a request with a "?" in it (usually those requests contain your auth code).
    - In the panel to the right of the Name panel, make sure the tab "Headers" is selected.
    - Look down the left side of the headers panel for "Authorization:". The value to the left of it is your auth code. If you don't see it, try a different request.

    #### DO NOT SHARE YOUR AUTH CODE WITH ANYONE!!!

    Anyone with access to your auth code can access your account data.
---
4. Change `THE_BEGINNING` and/or `THE_END` to the time(s) you want as the number of seconds since the epoch. You can use the converter at [epochconverter](https://www.epochconverter.com/) or trial and error using the "TEST" setting.
---
5. Change FREQUENCY to the amount of seconds you want between each time the status is updated.
---
6. Change VALUE to the setting you want:
    - PDONE - Percentage of the time period completed so far.

        ![Screenshot of pdone status](/images/screenshot_pdone.png)

    - SLEFT - Seconds left until THE_END, THE_BEGINNING is ignored.

        ![Screenshot of sleft status](/images/screenshot_sleft.png)

    - TEST  - Prints the date and time represented by THE_BEGINNING and THE_END to the console/terminal.

        ![Screenshot of test console/terminal output](/images/screenshot_test.png)
---
7. With that all completed, run the program. Instructions on how to run a Python program are as follows:
    - Open the command prompt and paste `cd C:\Downloads\November` assuming the project is still in your downloads folder, if you moved it, change the file path accordingly. Press enter.
    - Paste `python project_november.py` and enter.
---
If you are using the test setting, you can run it again after changing the value to try and get the right date. If you are using any other setting, congrats! You now have a status that updates automatically! Feel free to edit the `project_november.py` file however you want.

The program can be interrupted by either entering `ctrl+c` into the console/terminal or turning off your computer. This means the program will not run when your device is off so you will have to run it each time you turn it back on.

---
This is a very "works on my device" kind of project so take my instructions with a grain of salt and seek out online guides if needed.

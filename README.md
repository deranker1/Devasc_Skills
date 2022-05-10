# Devasc_Skills

### Task 1: Python expirements practica

* Start by setting up your DEVASC-LABVM and get it up and running
* Install [VirtualBox](https://www.virtualbox.org/) 
* Download the [OVA](https://www.netacad.com/portal/content/devnet-associate-virtual-machines-vms) file from cisco's website 
* Open Oracle Virtual Box and import the OVA file
* Use the username **devasc** and password **Cisco123!** to login
* Running Python in VS Code
  * First Install [Visual Studio Code](https://code.visualstudio.com/)
  * Open VS Code and open the python script located in the task 1 folder
  * Use the terminal to install the necessary libraries using pip3
  * Run the python script by typing the filepath  
* Running Python in Jupyter notebook
  * First Install Jupyter via terminal by using the pip3 command
  * Run the program by typing **jupyter notebook** in the terminal
  * A new browser window should open, or you could click the http link displayed in the terminal output
  * To run a python script, first click on New -> Python3
  * Paste in your python code and click on Run
  * You can now save this script or add a new one using the toolbar
* Running Python in IDLE environment
  * First install Python IDLE via terminal using **sudo apt-get install idle3**
  * Verify that Python version is the same as Python IDLE version and update if needed, 
  you can check the version with command python3 --version
  * type **idle** in your terminal to start Python IDLE
  * Paste in Python code in the IDLE script environment and click on run
  * The code output should display on the terminal screen

Possible issues:
* If you can't access jupyter via chromium based browser, try firefox
* If Python IDLE gets errors when trying to run code, check the python versions and make sure they match

### Task 2: Explore Python development tools and REST APIs

* Start by setting up your DEVASC-LABVM and get it up and running.
* If not yet completed, see task 1
* Explore REST APIs with School Library API
  * Go to the School Library Documentation page by opening the chromium browser
  * 

### Task 3: Github Skills

* Start by setting up your DEVASC-LABVM and get it up and running. 
* If not yet completed, see task 1.


### Task 4: Webex teams API

* Start by setting up your DEVASC-LABVM and get it up and running. 
* If not yet completed, see task 1.
* 

### Task 5: Data Format Conversion

* Start by setting up your DEVASC-LABVM and get it up and running. 
* If not yet completed, see task 1.
* Parsing JSON data in different formats using [jsonconvert.py](https://github.com/deranker1/Devasc_Skills/blob/main/Task%205:%20Data%20Format%20Conversion/json_convert.py)
* Parsing JSON to YAML
 * First import the YAML library
 * Use the print("---") to create three dashes which is required for YAML formatting
 * Use print together with the YAML method .dump() and pass in the variable which encapsulates the JSON string
 * You should now see the JSON string displayed in YAML format
* Parsing JSON to Python Dict
 * First make sure you have imported the json library
 * Use print with the json method .loads() and pass in the valid JSON variable
 * You should now see the JSON string displayed in dictionary format
 * Parsing Python Dict to JSON
  * First make sure you have imported the json library
  * Use print with the json method .dumps() and pass in the valid Dict variable 
  * Optionally you could also pass in the **indent** parameter with an assigned number to create a cleaner display
  * The dict should now display in JSON format
  * 

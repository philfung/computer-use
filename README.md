# Computer Use Demo for Mac

This is a fork of Anthropic's computer use demo modified to run on Mac.

## Caution
Computer use is a beta feature from Anthropic that has direct access to the internet and sends screenshots of your desktop to Anthropic. 

## Setup
1. Ensure you have the latest Python 3 and Chrome installed.
2. You need to enable extra permissions so that this application can control your mouse and keyboard.  
  * Open the 'Settings' app->click on 'Privacy and Security'->click on 'Accessibility'. 
  * Click the little '+' on the lower-left and add the 'Terminal' application.  
  * Click the toggle next to the 'Terminal' app so it turns blue.
3. Open 'Terminal', clone this repo, set up a Python virtual environment and install all requirements.
```bash
git clone <this repository>
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r dev-requirements.txt
```
3. Run the Streamlit application.
```bash
python -m streamlit run computer_use_demo/streamlit.py
```
The Computer Use Demo should automatically open in Chrome.

4. Enter your Anthropic API Key in the left panel of the application.

5. Try computer use by entering commands!
For example:
```bash
"Open cnn.com and click on the latest article"


"Open the Settings app and lower the screen brightness"
```


 



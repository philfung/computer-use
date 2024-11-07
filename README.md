# Computer Use Demo for MacOS 💻

This is a fork of [Anthropic's computer use demo](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) modified to run on macOS. It allows you to experience the power and limitations of computer use firsthand.

<img height="300" alt="Screenshot 2024-11-06 at 3 52 59 PM" src="https://github.com/user-attachments/assets/d22cf7d3-3b72-41fb-a492-4d6404cea98d">

## Caution
Computer use is a [beta feature from Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) that has direct access to the internet and sends screenshots of your desktop to Anthropic. 

## Setup
1. Ensure you have the latest [Python 3](https://www.python.org/downloads/) and [Chrome](https://www.google.com/chrome/dr/download/) installed.
2. You need to enable extra permissions so that this application can control your mouse and keyboard.  
  * Open the 'Settings' app->click on 'Privacy and Security'->click on 'Accessibility'.
<img width="75" alt="Screenshot 2024-11-06 at 3 48 30 PM" src="https://github.com/user-attachments/assets/67de19cc-cf7b-448c-a02c-52304e8d43f3">

<img height="100" alt="Screenshot 2024-11-06 at 3 44 47 PM" src="https://github.com/user-attachments/assets/59c325d7-4e43-4272-8ac0-76323cd9dba7">
    <img height="100" alt="Screenshot 2024-11-06 at 3 45 02 PM" src="https://github.com/user-attachments/assets/eb497da7-e8c2-45a2-82c5-c6ceb49dee54">

  * Click the little '+' on the lower-left and add the 'Terminal' application.
<img width="66" alt="Screenshot 2024-11-06 at 3 46 28 PM" src="https://github.com/user-attachments/assets/87a10818-7f7d-4130-8e21-688815a21124">

  * Click the toggle next to the 'Terminal' app so it turns blue.
<img width="476" alt="Screenshot 2024-11-06 at 3 47 23 PM" src="https://github.com/user-attachments/assets/67e1a154-38bb-4c1b-9692-ccd382f4d470">


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

<img height="100" alt="Screenshot 2024-11-06 at 3 55 11 PM" src="https://github.com/user-attachments/assets/9fb5ebbb-577e-4c1d-ab85-8fd876cfb2b8">

5. Try computer use by entering commands!
For example:
```bash
"Open cnn.com and click on the latest article"


"Open the Settings app and lower the screen brightness"
```


 



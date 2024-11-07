# Computer Use for MacOS 💻
This macOS version of [Anthropic's computer use demo](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) lets you experience its capabilities and limitations firsthand.

<img height="450" alt="Frame 1" src="https://github.com/user-attachments/assets/d1a4e615-ef1c-4045-a3d3-a4b38b636994">

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


3. Open the 'Terminal' app and install and run the application.
```bash
chmod u+x install_and_run.sh
./install_and_run.sh
```
The Computer Use Demo should automatically open in the Chrome browser.

4. Enter your Anthropic API Key in the left panel of the application.

<img height="200" alt="Screenshot 2024-11-06 at 3 55 11 PM" src="https://github.com/user-attachments/assets/9fb5ebbb-577e-4c1d-ab85-8fd876cfb2b8">

5. Try computer use by entering commands!
For example:
```bash
"Open cnn.com and click on the latest article"


"Open the Settings app and lower the screen brightness"
```


 



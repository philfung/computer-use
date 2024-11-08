# Computer Use for MacOS 💻
A macOS app (forked from [Anthropic's computer use demo](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)) for LLM-based computer use on your laptop.

<img height="450" alt="Frame 1" src="https://github.com/user-attachments/assets/d1a4e615-ef1c-4045-a3d3-a4b38b636994">

## Caution ⚠️
Computer use is a [beta feature from Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) that has direct access to the internet and sends screenshots of your desktop to Anthropic. 

## Setup
1. Ensure you have the latest [Python 3](https://www.python.org/downloads/) (>= 3.11) and [Chrome](https://www.google.com/chrome/dr/download/) installed, and an [Anthropic API key](https://console.anthropic.com/settings/keys).
2. Enable Accesibility permissions so that this application can control your mouse and keyboard.  
* Open the *Settings* app->click on *Privacy and Security*->click on *Accessibility*.</br></br>
&nbsp;&nbsp;<img width="75" alt="Screenshot 2024-11-06 at 3 48 30 PM" src="https://github.com/user-attachments/assets/67de19cc-cf7b-448c-a02c-52304e8d43f3">&nbsp;<img height="100" alt="Screenshot 2024-11-06 at 3 44 47 PM" src="https://github.com/user-attachments/assets/59c325d7-4e43-4272-8ac0-76323cd9dba7">&nbsp;<img width="286" alt="Screenshot 2024-11-07 at 6 29 40 PM" src="https://github.com/user-attachments/assets/52f471ae-b16c-4d2d-bcaf-dfe225e6987e">


* Click the little *+* on the lower-left and add the *Terminal* application, and click on the toggle next to the app so it turns blue.</br></br>
&nbsp;&nbsp;<img width="66" alt="Screenshot 2024-11-06 at 3 46 28 PM" src="https://github.com/user-attachments/assets/87a10818-7f7d-4130-8e21-688815a21124">
&nbsp;&nbsp;<img width="476" alt="Screenshot 2024-11-06 at 3 47 23 PM" src="https://github.com/user-attachments/assets/67e1a154-38bb-4c1b-9692-ccd382f4d470">

3. Enable Screen Recording permissions so that this application can take screenshots of the desktop.
* Open the *Settings* app->click on *Privacy and Security*->click on *Screen and System Recording*.</br></br>
&nbsp;&nbsp;<img width="75" alt="Screenshot 2024-11-06 at 3 48 30 PM" src="https://github.com/user-attachments/assets/67de19cc-cf7b-448c-a02c-52304e8d43f3">&nbsp;<img height="100" alt="Screenshot 2024-11-06 at 3 44 47 PM" src="https://github.com/user-attachments/assets/59c325d7-4e43-4272-8ac0-76323cd9dba7">&nbsp;<img height="100" alt="Screenshot 2024-11-07 at 6 28 23 PM" src="https://github.com/user-attachments/assets/1ff6c92d-3399-446a-bdb4-13236971b620">

* Click the little *+* on the lower-left and add the *Terminal* application, and click on the toggle next to the app so it turns blue.</br></br>
&nbsp;&nbsp;<img width="66" alt="Screenshot 2024-11-06 at 3 46 28 PM" src="https://github.com/user-attachments/assets/87a10818-7f7d-4130-8e21-688815a21124">
&nbsp;&nbsp;<img width="476" alt="Screenshot 2024-11-06 at 3 47 23 PM" src="https://github.com/user-attachments/assets/67e1a154-38bb-4c1b-9692-ccd382f4d470">


4. Open the *Terminal* app and run the install script.
<img width="32" alt="Screenshot 2024-11-07 at 1 52 18 PM" src="https://github.com/user-attachments/assets/4fa5a963-9f26-4d22-9bac-6d5f81957000">

```bash
git clone https://github.com/philfung/open-computer-use.git
cd open-computer-use
chmod u+x install_and_run.sh
./install_and_run.sh
```
&nbsp;&nbsp;The Computer Use Demo should automatically open in the Chrome browser.

&nbsp;&nbsp;&nbsp;&nbsp;<img height="250" alt="Frame 1" src="https://github.com/user-attachments/assets/d1a4e615-ef1c-4045-a3d3-a4b38b636994">

5. Enter your [Anthropic API Key](https://console.anthropic.com/settings/keys) in the left panel of the application.

&nbsp;&nbsp;&nbsp;&nbsp;<img height="200" alt="Screenshot 2024-11-06 at 3 55 11 PM" src="https://github.com/user-attachments/assets/9fb5ebbb-577e-4c1d-ab85-8fd876cfb2b8">

6. Try computer use by entering commands!
For example:
```bash
"Open cnn.com and click on the latest article"


"Open the Settings app and lower the screen brightness"
```


 



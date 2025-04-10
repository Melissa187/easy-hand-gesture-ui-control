# easy-hand-gesture-ui-control-4SO22AI033
A part of our major project where in we use Mediapipe Library in order to use hand movements to perform basic ui actions(In this Code:Zooming In and out and Changing the volume up and down)

In this code, I have used Python 3.10 in order to allow the use of the MediaPipe library, which does not work well with updated versions of Python. This project is a part of our major project "Adaptive UI/UX for Users", where we aim to make the use of computers easier and more relaxing — especially for tech people and researchers. Inspired by how we use mobile phones, this code handles a part of it: enabling zoom in and zoom out functionality, and volume up and down control through hand gestures.

Many more actions can be performed using the MediaPipe library by changing the finger combinations. Here's a snippet of the code that handles it:[image](https://github.com/user-attachments/assets/9ab0deca-da6a-45d2-8610-af9660d5b130)
if fingers == [1, 0, 0, 0, 0]:
        return "volume_up", fingers
    elif fingers == [0, 1, 1, 0, 0]:
        return "volume_down", fingers
    elif fingers == [1, 1, 1, 0, 0]:
        return "zoom_out", fingers
    elif fingers == [0, 1, 0, 0, 0]:
        return "zoom_in", fingers
    else:
        return "none", fingers

PyAutoGUI lets Python control the keyboard and mouse — like a robotic hand operating your computer.

In this project, we used it for:

Gesture	PyAutoGUI Function	What It Does
Zoom In	                  pyautogui.hotkey('ctrl', '+')	                        Presses Ctrl and + to zoom in
Zoom Out	                pyautogui.hotkey('ctrl', '-')	                        Presses Ctrl and – to zoom out
Volume Up	                pyautogui.press('volumeup')	                          Increases system volume
Volume Down	              pyautogui.press('volumedown')	                        Decreases system volume
Why PyAutoGUI is useful:
No need to interact with specific app code — it works like a human pressing keys.
Easy to automate actions like typing, clicking, zooming, and volume control.
Works on most platforms (Windows, macOS, Linux).[image](https://github.com/user-attachments/assets/20532993-01a1-45d0-8e35-431c6480a7a7)
    if action == "volume_up":
        pyautogui.press("volumeup")
    elif action == "volume_down":
        pyautogui.press("volumedown")
    elif action == "zoom_in":
        pyautogui.hotkey("ctrl", "+")
    elif action == "zoom_out":
        pyautogui.hotkey("ctrl", "-")




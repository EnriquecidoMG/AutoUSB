# <p align="center"> ![AutoUSB Git](https://github.com/user-attachments/assets/fd4f3923-cb04-4c6e-82c2-534f1fbc9cd0) </p>
## What does?
The application we created is designed to facilitate the creation of an autorun.inf file on USB drives. Here’s a summary of its features and functionalities:

- **Main Functions:**
USB Drive Selection: Allows users to select a connected USB drive, ensuring that the main disk where the operating system is installed is not chosen.

* **Autorun Customization:**

  * Drive Name: Users can set a new name for the USB drive.
  * Custom Icon: Users can select a .ico file that will be copied to the drive and used as its icon.
  * Automatic Startup File: Users can select an executable file, an image, or a video that will run automatically when the USB drive is inserted.
  * Autorun File Generation: The application creates an autorun.inf file that contains the necessary configuration to personalize the user experience when inserting the USB drive.

- **File Copying:** Both the icon and the startup file are automatically copied to the USB drive, ensuring they are available on other computers.

- **Intuitive Interface:** The application features a simple and user-friendly graphical interface built with Tkinter, allowing users to perform all configurations with ease.

- **Help and Support:** It includes a help button that provides instructions on how to use the application, as well as a link to a GitHub repository for further information or support.

### Purpose:
The goal of the application is to simplify the process of configuring USB drives, enabling users to customize them and automate tasks. This is particularly useful in educational settings, presentations, or for sharing software and multimedia in a more engaging way.

## What is 'autorun'?
An autorun file (usually named autorun.inf) is a special configuration file used primarily in Microsoft Windows operating systems. It is placed in the root directory of a removable drive, such as a USB flash drive or a CD/DVD, to automate certain actions when the drive is inserted into a computer.

## Tips
- **Ensure Drive is Connected:** Before launching the app, make sure your USB drive is plugged into your computer and is recognized by the operating system.
  
- **Backup Important Data:** If your USB drive contains important files, consider backing it up before making any changes. This way, you can avoid accidental loss of data.
  
- **Safely Eject the Drive:** After the autorun file is created and the necessary files are copied, safely eject the USB drive from your computer.
  
- **Test the Autorun:** Insert the USB drive into another computer (preferably one that allows autorun functionality) to test if the autorun works as expected.
  
- **Check Autorun Settings:** If the autorun feature doesn’t work as expected, check the autorun settings on the target computer, as many newer versions of Windows have disabled this feature for security reasons.
  
- **Compatible executable Files:**
  - .exe
  - Images:
    - jpg
    - jpeg
    - png
    - gif
  * Videos:
    * mp4
    * avi
    * mov
    * mkv
          

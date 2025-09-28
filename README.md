# firefox-random-wallpapers
A python script to change your wallpaper to something random.


You must have "toolkit.legacyUserProfileCustomizations.stylesheets" in "about:config" set to true. 
You must have a "userContent.css" file in your "chrome" folder. An example "userContent.css" is available.
Your wallpaper folder must be in your chrome folder.
Only images can be in the wallpaper folder.


It will work with multiple profiles, but the wallpaper folder must be named the same thing in all the chrome folders.
It is recommended that you include this script in your startup applications and backup your files.


There are two arguments: "-wi" and an integer to manually select the wallpaper, or "-wn" and a name to manually select the wallpaper. 
Please note that if you are using "-wn", you have to have the same wallpaper in all profiles.

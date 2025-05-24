This is a python script which takes in a list of bandcamp queue files from the command line and converts them into the new format used by the app.

After the playlist update, I noticed that opening the queue caused the app to close immediately. This caused an issue as I have a habit of saving my queue file and restoring it later so I can keep listening to the same music.

After doing some digging, I found that the cause was some missing fields in the json data. This script simply adds some values to those fields. I don't know if adding incorrect values to the fields also causes the app to crash, but it wasn't an issue in my case.

In order to use this, first copy the PlayerState.json file from the internal bandcamp files on your phone to your computer. It should be located in (wherever app files are located)/(bandcamp folder)/files/PlayerState.json. Then, run `python bandcamp_queue_updater.py PlayerState.json` in the terminal and copy the file back to the bandcamp files. Make sure to delete the old file first. This will probably fix the issue.


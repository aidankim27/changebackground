#!/bin/csh
cd /usr/local/bin/changebackground
rm /Users/aidankim/Documents/backgrounds/background.jpg
python run.py $argv[1]
while(! -e /Users/aidankim/Documents/backgrounds/background.jpg) 
    sleep 3
    python run.py $argv[1]
end
osascript -e 'tell app "Finder" to set desktop picture to POSIX file "/Users/aidankim/Documents/backgrounds/background.jpg"'


# Images_in_telegram

It's connects to NASA and Spacex API's, fetch images and public it (or any other images) in telegram channel.

How to install
------

Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

    pip install -r requirements.txt
    
For using you need your TOKEN from [NASA](https://api.nasa.gov/#apod)

Also you need TOKEN for your [Bot in telegram](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)

You should use environment variables. Create file name **.env** and variables NASA_TOKEN and BOT_TOKEN in the root directory.
In file **.env** only two line:

    NASA_TOKEN = 'here is your own TOKEN'
    BOT_TOKEN = 'here is your own TOKEN'

Example for command line:

    $ python '\Images_in_telegram\main.py' 3600

Where 3600 - time in seconds between publications. The default time is 4 hours. 

Project Goals
------
This code was written for educational purposes as part of an online course for web developers at dvmn.org.
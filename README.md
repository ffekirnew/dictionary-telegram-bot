# Dictionary Telegram Bot
This is a telegram bot that can define English words in English, or get equivalent Words in Amharic.

## Usage
- change the telegram API in the main.py to your telegram bot's secret API.
- change the translation and definition databases you would like to use in the databases folder and the control them in the main.py file
- the database I am using is a JSON dictionary, that can easily interface with python and is flexible. As a matter of fact all the databases used in this project are JSON. The dictionaries are stored in the form {"word": ["definition1", "definition2"], ...} if you arrange your words database like that, the bot will work as expected just by changing the file paths to the files given in the main file. However, if you would like to change the format of your json dictionary or use any other database, you would likely need to do most of your modification to the <em>database_handler.py</em> file.

## Features
The features provided in the current version of the telegram bot are:
- translation from English to Amharic
- generation of random words for the user's education
- keeping track of users' learned words
- providing definitions for english words in english

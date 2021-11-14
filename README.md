# Cal-Hob-bot #

## Description ##
A discord bot that serves you [Calvin and Hobbes](https://en.wikipedia.org/wiki/Calvin_and_Hobbes) comic strip from [Go Comics](https://www.gocomics.com/) website.

## Purpose of the project ##
1. Get an understanding of how discord bot works using discord API.
2. Understanding web-scraping and parsing a response HTML web page using python libraries like requests and BeautifulSoup.

## Add the bot to your discord server ##
Use this [link](https://discord.com/api/oauth2/authorize?client_id=863124324100866069&permissions=182336&scope=bot) to add the bot to your server.

## Running the bot on your device as server ##
#### Step 1 ####
Clone the repository
```Python
git clone https://github.com/Aayush-2492/Cal-Hob-bot.git
```

#### Step 2 ####
Install the requirements
```Python
pip install -r requirements.txt
```
OR
```Python
pip3 install -r requirements.txt
```
depending upon the version of python you use.


#### Step 3 ####
Add a .env file which contains the token to your bot stored under TOKEN key.

Run the [main.py](https://github.com/Aayush-2492/Cal-Hob-bot/blob/main/main.py) file and the bot is now active :)

## Bot Commands ##
1. `$help` - Displays all the commands.
2. `$calhob` - Returns a strip from a random date.
3. `$calhob_on <day> <month> <year>` <day> <month> <year> - Returns strip on that date if it exists(18/11/1985 - 31/12/1995).

## LICENSE ##
The project is licensed under [MIT LICENSE](https://github.com/Aayush2492/Cal-Hob-bot/blob/main/LICENSE)

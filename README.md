```
 ____ _____           _       
|  _ \_   _|__  _ __ (_) __ _ 
| | | || |/ _ \| '_ \| |/ _` |
| |_| || | (_) | |_) | | (_| |
|____/ |_|\___/| .__/|_|\__,_|
               |_|            

```       


<h4 align="center">Discord Selfbot</h4>

<p align="center">
  <a href="https://discord.gg/SbucxwJSuA">
    <img src="https://discordapp.com/api/guilds/1065340995136389212/widget.png?style=shield" alt="Discord Server">
  </a></p>



## Features
- [x] Copy Server Channels/Roles
- [x] Spam Reactions
- [x] Send Message to All Dms
- [x] Get all Servers
- [x] Message Flood Servers



## Installing
Install Windows:
```python
pip install dtopia
```
**If it doesnt work you might be ratelimited**

## Example Selfbot Command
```python
import dtopia

bot = dtopia.Client(token="TOKEN",prefix='!')

@bot.command
def hey(data):
  channel = data['d']['channel_id']
  bot.sendMessage('Hey',channel)

bot.run()

```
## Example Selfbot Event
```python
import dtopia

bot = dtopia.Client(token="TOKEN",prefix='!')

@bot.event
def on_message(data):
 bot.printReceivedMsg(data)
 
bot.run()
```

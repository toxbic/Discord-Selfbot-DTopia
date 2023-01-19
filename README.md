```
 ____ _____           _       
|  _ \_   _|__  _ __ (_) __ _ 
| | | || |/ _ \| '_ \| |/ _` |
| |_| || | (_) | |_) | | (_| |
|____/ |_|\___/| .__/|_|\__,_|
               |_|            

```       
<a href="https://discord.com/invite/yourinvitelink">
  <img src="https://images-ext-2.discordapp.net/external/KXh3VWo6OpBvuYwrbqxlgjW4sQDMZ-rPD1Qcoa2unP4/https/media.tenor.com/W3hULqFhYs0AAAPo/goku.mp4" alt="Join My Discord">
</a>

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

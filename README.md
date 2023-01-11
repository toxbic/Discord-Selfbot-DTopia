```
 _____ _______          _       
|  __ \__   __|        (_)      
| |  | | | | ___  _ __  _  __ _ 
| |  | | | |/ _ \| '_ \| |/ _` |
| |__| | | | (_) | |_) | | (_| |
|_____/  |_|\___/| .__/|_|\__,_|
                 | |            
                 |_|         
```        
Discord Tools - SelfBot - Open Source - Free

**If it doesnt work you might be ratelimited**

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

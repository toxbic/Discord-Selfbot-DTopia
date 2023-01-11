```py
88888888ba, 888888888888                    88             
88      `"8b     88                         ""             
88        `8b    88                                        
88         88    88  ,adPPYba,  8b,dPPYba,  88 ,adPPYYba,  
88         88    88 a8"     "8a 88P'    "8a 88 ""     `Y8  
88         8P    88 8b       d8 88       d8 88 ,adPPPPP88  
88      .a8P     88 "8a,   ,a8" 88b,   ,a8" 88 88,    ,88  
88888888Y"'      88  `"YbbdP"'  88`YbbdP"'  88 `"8bbdP"Y8  
                                88                         
                                88                         
  
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

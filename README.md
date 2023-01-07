# DTopia - Discord-Tools
Discord Tools - SelfBot - Open Source - Free

**If it doesnt work you might be ratelimited**


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

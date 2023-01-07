# DTopia - Discord-Tools
Discord Tools - SelfBot - Open Source - Free




## Installing
Install Windows:
```python
pip install dtopia
```

## Example
```python
import dtopia

bot = dtopia.Client(token=TOKEN",prefix='!')

@bot.command
def help(data):
  channel = data['d']['channel_id']
  bot.sendMessage('How what',channel)

bot.run()

```


# DTopia - Discord-Tools
Discord Tools - SelfBot - Open Source - Free




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


```

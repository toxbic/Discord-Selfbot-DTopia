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

bot = dtopia.Client(token='Your token',prefix='!')

@bot.command
def help(data):
 print(data)
 
 bot.run()

```


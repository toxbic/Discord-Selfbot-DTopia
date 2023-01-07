import requests
import time
import colorama
import asyncio
import threading
import websockets
import json
import base64
import urllib.parse



fc = {}
cmd = {}



    
async def _f(self):
     url = f"wss://gateway.discord.gg/?v=6&encoding=json&token={self.token}"
     async with websockets.connect(url) as websocket:
        # Send the identify payload to connect to the server
        payload = {
            "op": 2,
            "d": {
                "token": self.token,
                "properties": {
                    "$os": "windows",
                    "$browser": "my_library",
                    "$device": "my_library"
                },
                "compress": False,
                "large_threshold": 250,
                "shard": [0, 1]
            }
        }
        await websocket.send(json.dumps(payload))

        # Wait for the hello event
        data = await websocket.recv()
        data = json.loads(data)
       

        # Start a loop to listen for events
        while True:
            
            data = await websocket.recv()
            data = json.loads(data)

            # Print messages from the server
            #if data["t"] == "MESSAGE_CREATE":
                #message = data["d"]
            #func(data)
            if data['t'] == 'MESSAGE_CREATE':
              if 'on_message' in fc:
                fu = fc['on_message']
                
                fu(data)
              if 'on_dm' in fc:
                  guild = data.get('d').get('guild_id')
  
                  if guild is None:
    
                    fu = fc['on_dm']
                    fu(data)
              if str(data['d']['content']) in cmd:
                 call = str(data['d']['content'])
                 #print(prf)
                
                 call = call.replace(self.prefix,'')
                 
                 x = cmd[data['d']['content']]
                 x(data)
               
              

def _lgerror(self,content):
  if self.logs == True:
   
    print(content)

     
class Client:
    def __init__(self, token,prefix: str,logs:'True or False' = None):
        self.token = token
        if logs == None:
          self.logs = True
        else:
         self.logs = logs
        self.prefix = prefix
        r = requests.head(url="https://discord.com/api/v1")


        try:
         print(f"{colorama.Fore.RED} You are ratelimited\n {int(r.headers['Retry-After']) / 60} minutes left{colorama.Fore.WHITE}")
  
         


        except:
          pass
    def sendMessage(self,content: str,channelID: str):

     url = 'https://discord.com/api/channels/' + channelID + '/messages'
     headers = {
        "Authorization": self.token
     }

     data = {
         "content": content}

     response = requests.post(url, headers=headers, json=data)
     if self.logs == True:

       val = response.json().get('message')
       if val == 'Cannot send messages to this user':
        return 'Cannot send messages to this user'
       print(f'{colorama.Fore.GREEN}SEND MSG TO {response.json()["channel_id"]}{colorama.Fore.WHITE}')
    
     return response

    def getGuilds(self):
           url = 'https://discord.com/api/users/@me/guilds'
           headers = {"Authorization": self.token}
           response = requests.get(url, headers=headers)
           if self.logs == True:
            print(f'{colorama.Fore.BLUE}FOUND {len(response.json())} SERVERS{colorama.Fore.WHITE}')
            for x in response.json():
             print(f'  {colorama.Fore.GREEN}FOUND: {x["name"]}{colorama.Fore.WHITE}')
           return response
    def getDms(self, logusername: 'True or False' = None):
           url = 'https://discord.com/api/v9/users/@me/channels'
           headers = {"Authorization": self.token}
           response = requests.get(url, headers=headers)
           if self.logs == True:
            print(f'{colorama.Fore.BLUE}FOUND {len(response.json())} DMS{colorama.Fore.WHITE}')
            for x in response.json():
             if logusername == True:
              print(f'  {colorama.Fore.GREEN}FOUND: {x["recipients"][0]["username"]}#{x["recipients"][0]["discriminator"]}{colorama.Fore.WHITE}')
             else:
                  print(f'  {colorama.Fore.GREEN}FOUND: {x["id"]}{colorama.Fore.WHITE}')         
           return response
           #return response    
              
             





  
    def copyServer(self, copiedID,pastedID):
           url = 'https://discord.com/api/guilds/' + copiedID + '/channels'
           headers = {"Authorization": self.token}
           response = requests.get(url, headers=headers)
           try:
            m = response.json().get('message')
            if m == 'Missing Access':
              if self.logs == True:
               print(f'{colorama.Fore.RED}DISCORD ERROR: Missing Access ( Check if your in that server )')
              return response.json()
           except:
            r = response.json()
            cat = {}
            d1 = {}
            for x in r:
             time.sleep(1)
             naam = x['name']
             pr = x['permission_overwrites']
             type = x['type']
             if type == 4:
               
                 r = requests.post(f'https://discord.com/api/v9/guilds/{pastedID}/channels',headers=headers,json={"type": type,"name": naam,"permission_overwrites": pr,'position':x['position']}) 
               #print(naam)
                 d1[x['id']] = r.json()['id']
                 if self.logs == True:
                   print(f'{colorama.Fore.BLUE} COPIED {naam}{colorama.Fore.WHITE}')
             else:
               cat[x['id']] = x
            
               
            for x in cat:
             time.sleep(1)
             if self.logs == True:
              print(f'{colorama.Fore.GREEN}     COPIED {cat[x]["name"]}{colorama.Fore.WHITE}')
             if cat[x]['parent_id'] == None:
                             r = requests.post(f'https://discord.com/api/v9/guilds/{pastedID}/channels',headers=headers,json={"type": cat[x]['type'],"name": cat[x]['name'],"permission_overwrites": cat[x]['permission_overwrites'],'position':cat[x]['position']})    
             else:
                             r = requests.post(f'https://discord.com/api/v9/guilds/{pastedID}/channels',headers=headers,json={"type": cat[x]['type'],"name": cat[x]['name'],"permission_overwrites": cat[x]['permission_overwrites'],'position':cat[x]['position'],'parent_id':d1[cat[x]['parent_id']]})                  
    def dmAll(self,content, logusername: 'True or False' = None):
           if content == '':
             lgerror(self,f'{colorama.Fore.RED}DISCORD ERROR: Empty Message')
             
             return
           m = 0
           response = requests.get('https://discord.com/api/v9/users/@me/channels', headers={"Authorization": self.token}).json()
           if self.logs == True:
            print(f'{colorama.Fore.BLUE}FOUND {len(response)} DMS{colorama.Fore.WHITE}')
           for user in response:
            
     

 
             time.sleep(1)
             response = requests.post('https://discord.com/api/channels/' + user['id'] + '/messages', headers={"Authorization": self.token}, json={"content": content})
             if response.status_code == 429:
               print('Rate limited')
               return
             if self.logs == True:
              val = response.json().get('message')
              if val == 'Cannot send messages to this user': 
                 if logusername == True:
                  print(f"{colorama.Fore.RED}   ERROR: {user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}{colorama.Fore.WHITE}")
                 else:
                         print(f"{colorama.Fore.RED}   ERROR: {user['recipients'][0]['id']}{colorama.Fore.WHITE}")          
                 continue
              m +=1
              if logusername == True:
               print(f"{colorama.Fore.GREEN}   SEND TO {user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}{colorama.Fore.WHITE}")
              else:
                print(f"{colorama.Fore.GREEN}   SEND TO {user['recipients'][0]['id']}{colorama.Fore.WHITE}")


              
    
               
           
           return f'CORRECTLY SEND TO {m}'
    def deleteMessage(self,messageID:str,channelID:str):
      r= requests.delete(f'https://discord.com/api/v9/channels/{channelID}/messages/{messageID}',headers={'authorization':self.token})
      if self.logs == True:
       try:
        r.json()
        print(f'{colorama.Fore.RED}DISCORD ERROR: {r.json()}')
        return r.json()
       except:
         print(f'{colorama.Fore.BLUE} DELETE MSG: {messageID}')
         return 'MESSAGE DELETED'
      return 'MESSAGE DELETED'
    def printReceivedMsg(self,data):
      if data['t'] == 'MESSAGE_CREATE':
       print(f"{colorama.Fore.GREEN} {data['d']['author']['username']}#{data['d']['author']['discriminator']} : {data['d']['content']}")
    def setStatus(self,content:str):



       response = requests.patch("https://discord.com/api/v6/users/@me/settings", headers={"Authorization":self.token}, json={"custom_status": {"text": content,"expires_at": None}})
       return response
    def userToken(self,userID: str):
        userid = userID

        encodedBytes = base64.b64encode(userid.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")[:-2]
        return encodedStr
    def addEmoji100Msg(self,emoji:'Emoji: 😁',channelID: str, interval: int = None):
  
       emoji_str = urllib.parse.quote(emoji)



       f = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages?limit=100',headers={'authorization':self.token}).json()
       xv = 0
       for x in f:
         if interval == None:
          time.sleep(1)
         else:
           time.sleep(interval)
           
         r= requests.put(f'https://discord.com/api/v9/channels/{channelID}/messages/{x["id"]}/reactions/{emoji_str}/%40me?location=Message&burst=false',json={'location':'Message','burst':'false'},headers={'authorization':self.token})
         xv += 1
         if self.logs == True:
           print(f'{colorama.Fore.GREEN}ADDED {emoji} TO {x["id"]} AMOUNT: {xv}')
    def addEmojisTo1Msg(self,channelID:str,msgID:str,emojis=list,interval: int = None,remove: 'True or False' = None):
      newl = []
      for x in emojis:
        emoji_str = urllib.parse.quote(x)
        newl.append(emoji_str)
      routes = 0
      i = 0
      while True:
       
       for x in newl:

        if interval == None:
          time.sleep(1)
        else:
          time.sleep(interval)
        r= requests.put(f'https://discord.com/api/v9/channels/{channelID}/messages/{msgID}/reactions/{x}/%40me?location=Message&burst=false',json={'location':'Message','burst':'false'},headers={'authorization':self.token})
        print(f'{colorama.Fore.GREEN} ADDED {emojis[i]} TO {msgID}')
        i += 1
       i = 0
       if remove == True:
        for x in newl:
      
         if interval == None:
           time.sleep(1)
         else:
           time.sleep(interval)
         r= requests.delete(f'https://discord.com/api/v9/channels/{channelID}/messages/{msgID}/reactions/{x}/%40me?location=Message&burst=false',json={'location':'Message','burst':'false'},headers={'authorization':self.token})
         print(f'{colorama.Fore.RED} REMOVED {emojis[i]} FROM {msgID}')
         i +=1
       else:
         break
       i = 0
       
    def event(self,func):
      for x in fc:
              
             
        if str(x) == f'{func.__name__}':
                print('NO 2 SAME FUNCTIONS AT A TIME')
                exit()
      fc[func.__name__] = func
    def command(self,func):
            
            for x in cmd:
              
             
              if str(x) == f'{self.prefix}{func.__name__}':
                print('NO 2 SAME FUNCTIONS AT A TIME')
                exit()
            cmd[f'{self.prefix}{func.__name__}'] = func

    def run(self):
         
         asyncio.run(_f(self)) 
                
    
       

     


      

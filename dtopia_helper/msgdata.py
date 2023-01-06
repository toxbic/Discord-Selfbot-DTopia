class msg:
  def __init__(self, data):
    self.user = f"{data['d']['author']['username']}{data['d']['author']['discriminator']}"
    self.user_id= data['d']['author']['id']

from pushbullet import Pushbullet
file="msg.txt"
with open (file, mode='r') as f:
  text=f.read()
pb=Pushbullet(API_KEY)
push=pb.push_note("please rember",text)

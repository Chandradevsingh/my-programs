from skpy import Skype
import os.path


slogin = Skype('chandradevbijnor@gmail.com', 'Latest$70')

# contact = slogin.contacts
# contact = slogin.contacts['live:.cid.7c9aedc050a9fb47']

# for _ in contact:
#     print(_)

# contact.chat.sendMsg('Hi...')

# group = slogin.chats.create(['', '', '', '', ''])

contact = slogin.contacts['live:.cid.7c9aedc050a9fb47']
with open('C:/Users/welcome/Pictures/Default Images/nature.jpg', 'rb') as f:
    contact.chat.sendFile(f, 'nature.jpg', image=True)
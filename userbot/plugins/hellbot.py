# this plugin made by Heaven Userbot

"""Plugin for HellBot Repo

\nCode by @ViLLAiN_V01

type '.hellbot' to get HellBot repo
"""

import random, re
from heavenbot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="hellbot ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Click [here](https://github.com/HellBoy-OP/HellBot) to open this 🔥**Lit AF!!**🔥 **Hêllẞø†** Repo.. Join channel :- @HellBot_Official Repo Uploaded By @HeavenBot_Official")
    
        
   

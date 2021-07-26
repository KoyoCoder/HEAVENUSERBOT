import re

from heavenbot import bot
from heavenbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from heavenbot.cmdhelp import CmdHelp
from heavenbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(h1m4n5hu0p):
    heaven = villain_v01.pattern_match.group(1)
    if not heaven:
        if villain_v01.is_reply:
            (await villain_v01.get_reply_message()).message
        else:
            await edit_or_reply(villain_v01, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(heaven))}")

    await troll[0].click(
        villain_v01.chat_id,
        reply_to=villain_v01.reply_to_msg_id,
        silent=bool(villain_v01.is_reply),
        hide_via=True,
    )

    await villain_v01.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()

from heavenbot.utils import *
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"shout", outgoing=True))
@bot.on(sudo_cmd(pattern=r"shout", allow_sudo=True))
async def shout(args):
    if args.fwd_from:
        return
    msg = "```"
    messagestr = args.text
    messagestr = messagestr[7:]
    text = " ".join(messagestr)
    result = [" ".join(text)]
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + " " + "  " * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "\n" + result
    await args.edit("`" + msg + "`")

CmdHelp("shout").add_command(
  "shout", "<text>", "Shouts your message in meme way.", ".shout Hello"
).add()
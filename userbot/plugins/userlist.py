"""Get Administrators of any Chat*
Syntax: .userlist"""
from telethon import events
from telethon.errors.rpcerrorlist import MessageTooLongError
from heavenbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern=r"userlist ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"userlist ?(.*)", allow_sudo=True))
async def get_users(show):
    """ For .userslist command, list all of the users of the chat. """
    if show.text[0].isalpha() or show.text[0] in ("/", "#", "@", "!"):
        return
    if not show.is_group:
        await edit_or_reply(show, "Are you sure this is a group?")
        return
    info = await show.client.get_entity(show.chat_id)
    title = info.title or "this chat"
    mentions = "Users in {}: \n".format(title)
    try:
        if not show.pattern_match.group(1):
            async for user in show.client.iter_participants(show.chat_id):
                if not user.deleted:
                    mentions += (
                        f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                    )
                else:
                    mentions += f"\nDeleted Account `{user.id}`"
        else:
            searchq = show.pattern_match.group(1)
            async for user in show.client.iter_participants(
                show.chat_id, search=f"{searchq}"
            ):
                if not user.deleted:
                    mentions += (
                        f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                    )
                else:
                    mentions += f"\nDeleted Account `{user.id}`"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await edit_or_reply(show, mentions)
    except MessageTooLongError:
        await edit_or_reply(show, 
            "Damn, this is a huge group. Uploading users lists as file."
        )
        with open("userslist.txt", "w+") as file:
            file.write(mentions)
        await show.client.send_file(
            show.chat_id,
            "userslist.txt",
            caption="Users in {}".format(title),
            reply_to=show.id,
        )
        remove("userslist.txt")

CmdHelp("userlist").add_command(
  "userlist", None, "Gets the list of all the users in the chat"
).add()
from SerenaRobot.events import register
from SerenaRobot import telethn as System
from PIL import Image, ImageDraw, ImageFont
import os

async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if useir.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return replied_user

@register(pattern=("/get_id"))
async def image_maker(event) -> None:
    replied_user = await event.get_reply_message()
    # open id photo
    id_template = Image.open("XMAS.jpg")
    # resize user photo to fit box in id template
    # postion on where to draw text
    draw = ImageDraw.Draw(id_template)
    color = "rgb(0, 0, 0)"  # black
    font = ImageFont.truetype("MerryChristmasStar.ttf", size=80)
    font2 = ImageFont.truetype("MerryChristmasStar.ttf", size=100)
    # put text in image
    draw.text(
        (1000, 460),
        replied_user.sender.first_name.replace("\u2060", ""),
        fill=color,
        font=font2,
    )
    draw.text((393, 50), str(replied_user.sender_id), fill=color, font=font)
    id_template.save("xmas.png")
    if "doc" in event.text:
        force_document = True
    else:
        force_document = False
    await System.send_message(
        event.chat_id,
        "Merry Christmas ☃️🌲",
        reply_to=event.message.id,
        file="xmas.png",
        force_document=force_document,
        silent=True,
    )
    os.remove("xmas.png")

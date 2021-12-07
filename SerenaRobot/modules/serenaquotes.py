import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import SerenaRobot.modules.serenaquotes_strings as animequotes_strings
from SerenaRobot import dispatcher
from SerenaRobot.modules.disable import DisableAbleCommandHandler
from SerenaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SerenaRobot.modules.helper_funcs.extraction import extract_user

@run_async
def serenaquotes(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(animequotes_strings.QUOTES_IMG))

__help__ = """
 ❦ `/serenaquotes`*:* get random cute and motivational Serena Quates
 
"""
ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("serenaquotes", serenaquotes)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)

__mod_name__ = "SERENA-SPECIAL🌹"
__command_list__ = [
    "serenaquotes"
]
__handlers__ = [
    ANIMEQUOTES_HANDLER
]

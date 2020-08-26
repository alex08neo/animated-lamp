from pyrogram import filters as  Filters

from ..utils import screenshot_fn
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_callback_query(Filters.create(lambda _, __, query: query.data.startswith('scht')))
async def _(c, m):
    c.loop.create_task(screenshot_fn(c, m))

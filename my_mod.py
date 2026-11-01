from .. import loader, utils

class MyMod(loader.Module):
    strings = {"name": "MyCoolMod"}

    @loader.command()
    async def mycmd(self, message, args):
        """Описание команды."""
        await utils.answer(message, "Привет из моего мода!")
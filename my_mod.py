import time
from .. import loader, utils

@loader.tds
class MyCoolMod(loader.Module):
    """Мой первый мод с полезными командами."""
    strings = {"name": "MyCoolMod"}

    @loader.command()
    async def ping(self, message):
        """Проверить скорость отклика."""
        start = time.perf_counter()
        msg = await utils.answer(message, "<b>🏓 Понг!</b>")
        end = time.perf_counter()
        # Считаем время в миллисекундах
        ping_time = round((end - start) * 1000, 2)
        await msg.edit(f"<b>🏓 Понг!</b>\n<i>Скорость: {ping_time} мс</i>")

    @loader.command()
    async def say(self, message):
        """Отправить сообщение от твоего имени. Использование: .say Привет"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "<b>❌ Ошибка:</b> Напиши текст после команды.")
            return
        
        # Удаляем сообщение с командой и отправляем текст
        await message.delete()
        await message.respond(args)
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
    FSInputFile
)

TOKEN = "8573340119:AAG-TnoICR57ZdmV8cLjN6PyyR0qZMWaz2A"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ================== КЛАВИАТУРА ПОДПИСКИ ==================
subscribe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔵 Группа VK",
                url="https://vk.com/marselincloting"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Канал Telegram",
                url="https://t.me/marselin"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Канал Disax",
                url="https://t.me/disaxm"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ Я подписался",
                callback_data="subscribed"
            )
        ]
    ]
)

# ================== ГЛАВНОЕ МЕНЮ ==================
main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛒 Открыть каталог",
                web_app=WebAppInfo(url="https://marselin.store/")
            )
        ],
        [
            InlineKeyboardButton(
                text="⭐ Отзывы",
                url="https://vk.com/topic-179566096_48206712"
            )
        ],
        [
            InlineKeyboardButton(
                text="🆘 Support",
                url="https://t.me/cata_CVV"
            )
        ]
    ]
)

# ================== /start ==================
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Перед началом подпишись на наши ресурсы 👇",
        reply_markup=subscribe_keyboard
    )

# ================== ПОСЛЕ ПОДПИСКИ ==================
@dp.callback_query(lambda c: c.data == "subscribed")
async def subscribed(callback: types.CallbackQuery):
    gif = FSInputFile("menu/hello.gif")

    await callback.message.answer_animation(
        animation=gif,
        caption=
        "🔥 **Добро пожаловать в магазин бренда Marselin** 🔥\n\n"
        "Как все мы наслышаны, Диса или же всеми уважаемый Архитектор жизни "
        "придумал нам пиздатые джерси и много другого шмота, "
        "чтобы мы ходили в нем и светили ярко.\n\n"
        "Если ты хочешь приобрести самый пиздатый шмот — "
        "открывай каталог и делай заказ.\n\n"
        "Также ты можешь ознакомиться с отзывами 👇",
        reply_markup=main_keyboard,
        parse_mode="Markdown"
    )

    await callback.answer()

# ================== ЗАПУСК ==================
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


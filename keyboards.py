from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура для команды /start
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет")], [KeyboardButton(text="Пока")]
    ], resize_keyboard=True)

# Клавиатура с URL-ссылками для команды /links
link_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url='https://news.example.com', callback_data='news')],
        [InlineKeyboardButton(text="Музыка", url='https://music.example.com', callback_data='music')],
        [InlineKeyboardButton(text="Видео", url='https://video.example.com', callback_data='video')]
    ]
)

# Клавиатура для команды /dynamic
dynamic_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data='show_more')]
    ]
)

# Клавиатура с опциями для команды /dynamic
dynamic_options_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data='option_1')],
        [InlineKeyboardButton(text="Опция 2", callback_data='option_2')]
    ]
)

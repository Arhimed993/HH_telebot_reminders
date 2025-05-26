import os
from telebot.types import Message

FILES_DIR = "data/resumes"

os.makedirs(FILES_DIR, exist_ok=True)

def register_handlers(bot):
    @bot.message_handler(commands=["files"])
    def list_files(message: Message):
        try:
            files = os.listdir(FILES_DIR)
            if not files:
                bot.send_message(message.chat.id, "❌ Нет доступных файлов.")
            else:
                msg = "📂 Доступные файлы:\n" + "\n".join(f"📄 {f}" for f in files)
                bot.send_message(message.chat.id, msg)
        except Exception as e:
            bot.send_message(message.chat.id, f"⚠️ Ошибка при получении списка файлов: {e}")

    @bot.message_handler(commands=["get_file"])
    def get_file(message: Message):
        try:
            filename = message.text.split(maxsplit=1)[1].strip() if len(message.text.split()) > 1 else ""
            
            if not filename:
                bot.send_message(message.chat.id, "❌ Укажите название файла после команды.")
                return

            filepath = os.path.join(FILES_DIR, filename)
            
            if os.path.isfile(filepath): 
                with open(filepath, "rb") as f:
                    bot.send_document(message.chat.id, f)
            else:
                bot.send_message(message.chat.id, "❌ Файл не найден.")
        except IndexError:
            bot.send_message(message.chat.id, "❌ Укажите название файла после команды.")
        except Exception as e:
            bot.send_message(message.chat.id, f"⚠️ Ошибка при получении файла: {e}")
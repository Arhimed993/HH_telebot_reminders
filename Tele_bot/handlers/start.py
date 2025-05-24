from telebot.types import Message

def register_handlers(bot):
    @bot.message_handler(commands=["start"])
    def start_handler(message: Message):
        bot.send_message(message.chat.id, 
            "👋 Добро пожаловать! Вот доступные команды:\n\n"
            "🔐 Авторизация:\n"
            "/auth - Войти через HH\n\n"
            "👥 Работа с кандидатами:\n"
            "/search_candidate [запрос] - Поиск в локальной базе\n"
            "/add_manual [ФИО];[Должность];[Город];[Опыт];[Ссылка] - Ручное добавление кандидатов\n"  # Новое
            # "/import_resume [ссылка] - Импорт резюме с HH.ru\n"  
            "/search_manual [запрос] - Поиск по ручной базе\n\n" 
            "📝 Управление заметками:\n"
            "/add_note [кандидат] [текст] - Добавить заметку\n"
            "/notes [кандидат] - Показать заметки\n"
            "/delete_note [кандидат] [номер] - Удалить заметку\n\n"
            "⏰ Напоминания:\n"
            "/schedule_interview [ФИО] [дата: ГГГГ-ММ-ДД ЧЧ:ММ] - Назначить собеседование\n"
            "/schedule_onetoone [ФИО] [дата: ГГГГ-ММ-ДД ЧЧ:ММ] - Назначить встречу\n"
            "/scheduled_interviews - Список напоминаний\n"
            "/delete_reminder [ID] - Удалить напоминание\n\n"
            "📁 Работа с файлами:\n"
            "/files - Список резюме\n"
            "/get_file [название] - Скачать резюме",
        )
import random
import time

import telebot

import bot_logic
import config

from bot_logic import Menu
from telebot import types
from trafficRules import rules, signs, markings, approval, failures
from trafficRules import tasks1, tasks2, tasks3, tasks4, tasks5, tasks6, tasks7, tasks8
from trafficRules import tasks9, tasks10, tasks11, tasks12, tasks13, tasks14, tasks15, tasks16
from trafficRules import tasks17, tasks18, tasks19, tasks20, tasks21, tasks22, tasks23, tasks24, tasks25, tasks26

bot = telebot.TeleBot(config.TOKEN)


# Bot launch
@bot.message_handler(commands=['start'])
def start(message):
    # Hello sticker + message + main menu button
    start_button_menu = Menu()
    sti = open('stickers/7.webp', 'rb')

    start_button_menu.add(types.InlineKeyboardButton('🏁 Главное меню', callback_data='main_menu'))

    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n\n<b>{1.first_name}</b> - это бот, который "
                                      "поможет Вам в изучении правил дорожного движения.\n\nУдачи и приятного "
                                      "пользования!".format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=start_button_menu.get())


# Message handler
@bot.message_handler(content_types=['text'])
def welcome(message):
    main_menu = Menu()
    sti = open('stickers/12.webp', 'rb')

    main_menu.add(types.InlineKeyboardButton(text='📚 Теория', callback_data='theory'))
    main_menu.add(types.InlineKeyboardButton(text='🗂 Темы', callback_data='topics'))
    main_menu.add(types.InlineKeyboardButton(text='✉ Билеты', callback_data='cards'))
    #    main_menu.add(types.InlineKeyboardButton(text='🚔 Экзамен', callback_data='exam'))

    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Бот не умеет читать, давайте пользоваться кнопками меню")
    bot.send_message(message.chat.id, "<b>ГЛАВНОЕ МЕНЮ</b>", reply_markup=main_menu.get(), parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Default
    if call.data == "main_menu":
        main_menu = Menu()

        main_menu.add(types.InlineKeyboardButton(text='📚 Теория', callback_data='theory'))
        main_menu.add(types.InlineKeyboardButton(text='🗂 Темы', callback_data='topics'))
        main_menu.add(types.InlineKeyboardButton(text='✉ Билеты', callback_data='cards'))
        #        main_menu.add(types.InlineKeyboardButton(text='🚔 Экзамен', callback_data='exam'))

        bot.edit_message_text("<b>ГЛАВНОЕ МЕНЮ</b>", call.message.chat.id, call.message.message_id,
                              reply_markup=main_menu.get(), parse_mode='html')

    # Listing of main menu
    elif call.data == 'theory':
        theory_menu = Menu(back_button=types.InlineKeyboardButton('⏪ Назад', callback_data='main_menu'))

        theory_menu.add(types.InlineKeyboardButton('🚦 ПДД', callback_data='rules'))
        theory_menu.add(types.InlineKeyboardButton('🚸 Знаки', callback_data='signs'))
        theory_menu.add(types.InlineKeyboardButton('🛣 Разметка', callback_data='markings'))
        theory_menu.add(types.InlineKeyboardButton('🚗 Допуск ТС', callback_data='approval'))
        theory_menu.add(types.InlineKeyboardButton('⚙ Неисправноти ТС', callback_data='failures'))

        bot.edit_message_text(
            "📚<b>ТЕОРИЯ</b>📚\n\n\n🚦 - Правила дорожного движения\n\n🚸 - Знаки\n\n🛣 - Разметка\n\n🚗 - "
            "Основные положения по допуску транспортных средств к эксплуатации и обязанности "
            "должностных лиц по обеспечению безопасности дорожного движения\n\n⚙ - Перечень "
            "неисправностей и условий, при которых запрещается эксплуатация транспортных "
            "средств\n\n⏪ - Назад", call.message.chat.id, call.message.message_id,
            reply_markup=theory_menu.get(), parse_mode='html')

    elif call.data == 'topics':
        topics_menu = Menu(back_button=types.InlineKeyboardButton('⏪ Назад', callback_data='main_menu'))

        topics_menu.fill_num('topic', 26)

        bot.edit_message_text("<b>ТЕМЫ</b>\n\n"
                              "🗂1. Общие положения\n"
                              "🗂2. Общие обязанности водителей\n"
                              "🗂3. Дорожные знаки\n"
                              "🗂4. Расположение транспортных средств на проезжей части\n"
                              "🗂5. Дорожная разметка\n"
                              "🗂6. Сигналы светофора и регулировщика\n"
                              "🗂7. Приоритет маршрутных транспортных средств\n"
                              "🗂8. Начало движения, маневрирование\n"
                              "🗂9. Буксировка механических транспортных средств\n"
                              "🗂10. Скорость движения\n"
                              "🗂11. Применение специальных сигналов\n"
                              "🗂12. Обгон, опережение, встречный разъезд\n"
                              "🗂13. Движение по автомагистралям\n"
                              "🗂14. Остановка и стоянка\n"
                              "🗂15. Учебная езда и дополнительные требования к движению велосипедистов\n"
                              "🗂16. Проезд перекрестков\n"
                              "🗂17. Движение в жилых зонах\n"
                              "🗂18. Пользование внешними световыми приборами и звуковыми сигналами\n"
                              "🗂19. Движение через железнодорожные пути\n"
                              "🗂20. Неисправности и условия допуска транспортных средств к эксплуатации\n"
                              "🗂21. Пешеходные переходы и места остановок маршрутных транспортных средств\n"
                              "🗂22. Безопасность движения и техника управления автомобилем\n"
                              "🗂23. Перевозка людей и грузов\n"
                              "🗂24. Оказание доврачебной медицинской помощи\n"
                              "🗂25. Ответственность водителя\n"
                              "🗂26. Применение аварийной сигнализации и знака аварийной остановки\n",
                              call.message.chat.id, call.message.message_id, reply_markup=topics_menu.get(),
                              parse_mode='html'),

    elif call.data == 'cards':
        cards_menu = Menu(back_button=types.InlineKeyboardButton('⏪ Назад', callback_data='main_menu'))

        #        cards_menu.fill_num('card', 40)
        cards_menu.add(types.InlineKeyboardButton('🏁 Решать сгенерированный билет', callback_data='card'))
        bot_logic.main_card = bot_logic.generate_card()
        bot_logic.correct_answers = -1

        bot.edit_message_text("✉<b>БИЛЕТЫ</b>✉\n\n"
                              "Билет состоит из 20 вопросов, собранных в случайном порядке",
                              call.message.chat.id, call.message.message_id, reply_markup=cards_menu.get(),
                              parse_mode='html'),

    # Listing of theory menu
    elif call.data == 'rules':
        rules_menu = Menu(back_button=types.InlineKeyboardButton('⏪ Назад', callback_data='theory'))

        bot.edit_message_text(f"*ПРАВИЛА ДОРОЖНОГО ДВИЖЕНИЯ*\n\n"
                              f"🚦1 [Общие положения]({rules[0]})\n"
                              f"🚦2 [Общие обязанности водителей]({rules[1]})\n"
                              f"🚦3 [Применение специальных сигналов]({rules[2]})\n"
                              f"🚦4 [Обязанности пешеходов]({rules[3]})\n"
                              f"🚦5 [Обязанности пассажиров]({rules[4]})\n"
                              f"🚦6 [Сигналы светофора и регулировщика]({rules[5]})\n"
                              f"🚦7 [Применение аварийной сигнализации и знака аварийной остановки]({rules[6]})\n"
                              f"🚦8 [Начало движения, маневрирование]({rules[7]})\n"
                              f"🚦9 [Расположение транспортных средств на проезжей части]({rules[8]})\n"
                              f"🚦10 [Скорость движения]({rules[9]})\n"
                              f"🚦11 [Обгон, опережение, встречный разъезд]({rules[10]})\n"
                              f"🚦12 [Остановка и стоянка]({rules[11]})\n"
                              f"🚦13 [Проезд перекрёстков]({rules[12]})\n"
                              f"🚦14 [Пешеходные переходы и места остановок маршрутных транспортных средств]({rules[13]})\n"
                              f"🚦15 [Движение через железнодорожные пути]({rules[14]})\n"
                              f"🚦16 [Движение по автомагистралям]({rules[15]})\n"
                              f"🚦17 [Движение в жилых зонах]({rules[16]})\n"
                              f"🚦18 [Приоритет маршрутных транспортных средств]({rules[17]})\n"
                              f"🚦19 [Пользование внешними световыми приборами и звуковыми сигналами]({rules[18]})\n"
                              f"🚦20 [Буксировка механических транспортных средств]({rules[19]})\n"
                              f"🚦21 [Учебная езда]({rules[20]})\n"
                              f"🚦22 [Перевозка людей]({rules[21]})\n"
                              f"🚦23 [Перевозка грузов]({rules[22]})\n"
                              f"🚦24 [Дополнительные требования к движению велосипедистов и водителей мопедов]({rules[23]})\n"
                              f"🚦25 [Дополнительные требования к движению гужевых повозок, а также к прогону животных]({rules[24]})\n"
                              f"🚦26 [Нормы времени управления транспортным средством и отдыха]({rules[25]})\n",
                              call.message.chat.id, call.message.message_id, reply_markup=rules_menu.get(),
                              parse_mode='MarkdownV2', disable_web_page_preview=True)

    elif call.data == 'signs':
        signs_menu = Menu(back_button=types.InlineKeyboardButton('⏪ Назад', callback_data='theory'))

        bot.edit_message_text(f"*ЗНАКИ*\n\n"
                              f"🚸1 [Предупреждающие знаки]({signs[0]})\n"
                              f"🚸2 [Знаки приоритета]({signs[1]})\n"
                              f"🚸3 [Запрещающие знаки]({signs[2]})\n"
                              f"🚸4 [Предписывающие знаки]({signs[3]})\n"
                              f"🚸5 [Знаки особых предписаний]({signs[4]})\n"
                              f"🚸6 [Информационные знаки]({signs[5]})\n"
                              f"🚸7 [Знаки сервиса]({signs[6]})\n"
                              f"🚸8 [Знаки дополнительной информации или таблички]({signs[7]})\n",
                              call.message.chat.id, call.message.message_id, reply_markup=signs_menu.get(),
                              parse_mode='MarkdownV2', disable_web_page_preview=True)

    elif call.data == 'markings':
        markings_menu = Menu(back_button=types.InlineKeyboardButton('⏪ Назад', callback_data='theory'))

        bot.edit_message_text(f"*РАЗМЕТКА*\n\n"
                              f"🛣1 [Горизонтальная разметка]({markings[0]})\n"
                              f"🛣2 [Вертикальная разметка]({markings[1]})\n",
                              call.message.chat.id, call.message.message_id, reply_markup=markings_menu.get(),
                              parse_mode='MarkdownV2', disable_web_page_preview=True)

    elif call.data == 'approval':
        approval_menu = Menu(back_button=types.InlineKeyboardButton('⏪ Назад', callback_data='theory'))

        bot.edit_message_text(f"*ДОПУСК*\n\n"
                              f"🚗1 [Основные положения по допуску ТС к эксплуатации]({approval[0]})\n",
                              call.message.chat.id, call.message.message_id, reply_markup=approval_menu.get(),
                              parse_mode='MarkdownV2', disable_web_page_preview=True)

    elif call.data == 'failures':
        failures_menu = Menu(back_button=types.InlineKeyboardButton('⏪ Назад', callback_data='theory'))

        bot.edit_message_text(f"*НЕИСПРОВНОСТИ*\n\n"
                              f"⚙1 [Перечень неисправностей, при которых запрещается эксплуатация ТС]({failures[0]})\n",
                              call.message.chat.id, call.message.message_id, reply_markup=failures_menu.get(),
                              parse_mode='MarkdownV2', disable_web_page_preview=True)

    # Topics
    elif call.data == 'topic1':
        bot_logic.task_sender(bot, call, 1)
    elif call.data == 'topic2':
        bot_logic.task_sender(bot, call, 2)
    elif call.data == 'topic3':
        bot_logic.task_sender(bot, call, 3)
    elif call.data == 'topic4':
        bot_logic.task_sender(bot, call, 4)
    elif call.data == 'topic5':
        bot_logic.task_sender(bot, call, 5)
    elif call.data == 'topic6':
        bot_logic.task_sender(bot, call, 6)
    elif call.data == 'topic7':
        bot_logic.task_sender(bot, call, 7)
    elif call.data == 'topic8':
        bot_logic.task_sender(bot, call, 8)
    elif call.data == 'topic9':
        bot_logic.task_sender(bot, call, 9)
    elif call.data == 'topic10':
        bot_logic.task_sender(bot, call, 10)
    elif call.data == 'topic11':
        bot_logic.task_sender(bot, call, 11)
    elif call.data == 'topic12':
        bot_logic.task_sender(bot, call, 12)
    elif call.data == 'topic13':
        bot_logic.task_sender(bot, call, 13)
    elif call.data == 'topic14':
        bot_logic.task_sender(bot, call, 14)
    elif call.data == 'topic15':
        bot_logic.task_sender(bot, call, 15)
    elif call.data == 'topic16':
        bot_logic.task_sender(bot, call, 16)
    elif call.data == 'topic17':
        bot_logic.task_sender(bot, call, 17)
    elif call.data == 'topic18':
        bot_logic.task_sender(bot, call, 18)
    elif call.data == 'topic19':
        bot_logic.task_sender(bot, call, 19)
    elif call.data == 'topic20':
        bot_logic.task_sender(bot, call, 20)
    elif call.data == 'topic21':
        bot_logic.task_sender(bot, call, 21)
    elif call.data == 'topic22':
        bot_logic.task_sender(bot, call, 22)
    elif call.data == 'topic23':
        bot_logic.task_sender(bot, call, 23)
    elif call.data == 'topic24':
        bot_logic.task_sender(bot, call, 24)
    elif call.data == 'topic25':
        bot_logic.task_sender(bot, call, 25)
    elif call.data == 'topic26':
        bot_logic.task_sender(bot, call, 26)

    # Cards
    elif call.data == 'card':
        if len(bot_logic.main_card) != 0:
            random.shuffle(bot_logic.main_card)
            card_task = bot_logic.main_card[0]
            bot_logic.send_card_task(card_task, bot, call)
            bot_logic.main_card.remove(card_task)
            bot_logic.correct_answers += 1
            print(bot_logic.correct_answers)
        else:
            back_menu = Menu()
            back_menu.add(types.InlineKeyboardButton('⏪ Назад', callback_data='cards'))
            bot_logic.correct_answers += 1
            if bot_logic.correct_answers >= 18:
                bot.send_message(call.message.chat.id, "<b>РЕЗУЛЬТАТ</b>\n\n"
                                                       "Поздравляем, Вы сдали билет!\n\n"
                                                       f"Решено: {bot_logic.correct_answers} из 20",
                                 reply_markup=back_menu.get(),
                                 parse_mode='html')
            else:
                bot.send_message(call.message.chat.id, "<b>РЕЗУЛЬТАТ</b>\n\n"
                                                       "К сожалению, Вы не сдали билет. Надо больше тренироваться\n\n"
                                                       f"Решено: {bot_logic.correct_answers} из 20",
                                 reply_markup=back_menu.get(),
                                 parse_mode='html')

    #    elif call.data == 'wrong_in_card':

    # Hints
    elif call.data == 'hint1':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks1[0].correct}</b>\n\n{tasks1[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint2':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks2[0].correct}</b>\n\n{tasks2[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint3':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks3[0].correct}</b>\n\n{tasks3[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint4':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks4[0].correct}</b>\n\n{tasks4[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint5':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks5[0].correct}</b>\n\n{tasks5[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint6':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks6[0].correct}</b>\n\n{tasks6[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint7':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks7[0].correct}</b>\n\n{tasks7[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint8':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks8[0].correct}</b>\n\n{tasks8[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint9':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks9[0].correct}</b>\n\n{tasks9[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint10':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks10[0].correct}</b>\n\n{tasks10[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint11':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks11[0].correct}</b>\n\n{tasks11[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint12':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks12[0].correct}</b>\n\n{tasks12[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint13':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks13[0].correct}</b>\n\n{tasks13[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint14':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks14[0].correct}</b>\n\n{tasks14[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint15':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks15[0].correct}</b>\n\n{tasks15[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint16':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks16[0].correct}</b>\n\n{tasks16[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint17':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks17[0].correct}</b>\n\n{tasks17[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint18':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks18[0].correct}</b>\n\n{tasks18[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint19':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks19[0].correct}</b>\n\n{tasks19[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint20':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks20[0].correct}</b>\n\n{tasks20[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint21':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks21[0].correct}</b>\n\n{tasks21[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint22':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks22[0].correct}</b>\n\n{tasks22[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint23':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks23[0].correct}</b>\n\n{tasks23[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint24':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks24[0].correct}</b>\n\n{tasks24[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint25':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks25[0].correct}</b>\n\n{tasks25[0].hint}",
                         parse_mode='html')
    elif call.data == 'hint26':
        bot.send_message(call.message.chat.id, f"<b>Правильный ответ: {tasks26[0].correct}</b>\n\n{tasks26[0].hint}",
                         parse_mode='html')

    elif call.data == 'wrong':
        bot.answer_callback_query(call.id, "❌Неверно, попробуйте ещё раз❌", show_alert=True)
    elif call.data == 'wrong_in_card':
        if len(bot_logic.main_card) != 0:
            random.shuffle(bot_logic.main_card)
            card_task = bot_logic.main_card[0]
            bot_logic.send_card_task(card_task, bot, call)
            bot_logic.main_card.remove(card_task)
            print(bot_logic.correct_answers)
        else:
            back_menu = Menu()
            back_menu.add(types.InlineKeyboardButton('⏪ Назад', callback_data='cards'))
            if bot_logic.correct_answers >= 18:
                bot.send_message(call.message.chat.id, "<b>РЕЗУЛЬТАТ</b>\n\n"
                                                       "Поздравляем, Вы сдали билет!\n\n"
                                                       f"Решено: {bot_logic.correct_answers} из 20",
                                 reply_markup=back_menu.get(),
                                 parse_mode='html')
            else:
                bot.send_message(call.message.chat.id, "<b>РЕЗУЛЬТАТ</b>\n\n"
                                                       "К сожалению, Вы не сдали билет. Надо больше тренироваться\n\n"
                                                       f"Решено: {bot_logic.correct_answers} из 20",
                                 reply_markup=back_menu.get(),
                                 parse_mode='html')


# Infinite polling of TG servers (to make bot work non-stop)
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)

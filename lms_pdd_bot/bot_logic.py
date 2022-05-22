from telebot import types
import random

from trafficRules import tasks1, tasks2, tasks3, tasks4, tasks5, tasks6, tasks7, tasks8
from trafficRules import tasks9, tasks10, tasks11, tasks12, tasks13, tasks14, tasks15, tasks16
from trafficRules import tasks17, tasks18, tasks19, tasks20, tasks21, tasks22, tasks23, tasks24, tasks25, tasks26

# Attributes
main_card = []
correct_answers = 19


# Set required tasks
def tasks_setter(tasks):
    if tasks == 1:
        tasks = tasks1
    elif tasks == 2:
        tasks = tasks2
    elif tasks == 3:
        tasks = tasks3
    elif tasks == 4:
        tasks = tasks4
    elif tasks == 5:
        tasks = tasks5
    elif tasks == 6:
        tasks = tasks6
    elif tasks == 7:
        tasks = tasks7
    elif tasks == 8:
        tasks = tasks8
    elif tasks == 9:
        tasks = tasks9
    elif tasks == 10:
        tasks = tasks10
    elif tasks == 11:
        tasks = tasks11
    elif tasks == 12:
        tasks = tasks12
    elif tasks == 13:
        tasks = tasks13
    elif tasks == 14:
        tasks = tasks14
    elif tasks == 15:
        tasks = tasks15
    elif tasks == 16:
        tasks = tasks16
    elif tasks == 17:
        tasks = tasks17
    elif tasks == 18:
        tasks = tasks18
    elif tasks == 19:
        tasks = tasks19
    elif tasks == 20:
        tasks = tasks20
    elif tasks == 21:
        tasks = tasks21
    elif tasks == 22:
        tasks = tasks22
    elif tasks == 23:
        tasks = tasks23
    elif tasks == 24:
        tasks = tasks24
    elif tasks == 25:
        tasks = tasks25
    elif tasks == 26:
        tasks = tasks26
    return tasks


# Topic sender
def task_sender(bot, call, tasks):
    topic_menu = Menu()
    current_topic = tasks_setter(tasks)
    random.shuffle(current_topic)
    current_task = current_topic[0]
    topic_menu.help_button = types.InlineKeyboardButton('💡', callback_data=f'hint{tasks}')
    topic_menu.back_button = types.InlineKeyboardButton('⏪', callback_data='topics')
    # Checking if picture exists
    if current_task.picture != '0':
        bot.send_photo(call.message.chat.id, open(current_task.picture, 'rb'))
    # Option verification
    if current_task.variant3 == '0':
        topic_menu.fill_var(2, current_topic[0].correct, call.data)
        bot.send_message(call.message.chat.id, f"<b>{current_task.question}</b>\n\n"
                                               f"{current_task.variant1}\n"
                                               f"{current_task.variant2}",
                         parse_mode='html', reply_markup=topic_menu.get())
    elif current_task.variant4 == '0':
        topic_menu.fill_var(3, current_topic[0].correct, call.data)
        bot.send_message(call.message.chat.id, f"<b>{current_task.question}</b>\n\n"
                                               f"{current_task.variant1}\n"
                                               f"{current_task.variant2}\n"
                                               f"{current_task.variant3}",
                         parse_mode='html', reply_markup=topic_menu.get())
    elif current_task.variant5 == '0':
        topic_menu.fill_var(4, current_topic[0].correct, call.data)
        bot.send_message(call.message.chat.id, f"<b>{current_task.question}</b>\n\n"
                                               f"{current_task.variant1}\n"
                                               f"{current_task.variant2}\n"
                                               f"{current_task.variant3}\n"
                                               f"{current_task.variant4}",
                         parse_mode='html', reply_markup=topic_menu.get())
    else:
        topic_menu.fill_var(5, current_topic[0].correct, call.data)
        bot.send_message(call.message.chat.id, f"<b>{current_task.question}</b>\n\n"
                                               f"{current_task.variant1}\n"
                                               f"{current_task.variant2}\n"
                                               f"{current_task.variant3}\n"
                                               f"{current_task.variant4}\n"
                                               f"{current_task.variant5}",
                         parse_mode='html', reply_markup=topic_menu.get())


# Create a card with 20 questions
def generate_card():
    generated_card = []
    for i in range(20):
        topic = tasks_setter(random.randint(1, 26))
        random.shuffle(topic)
        generated_card.append(topic[0])
    return generated_card


# Generating markups for each task in card
def send_card_task(task, bot, call):
    task_menu = Menu()
    if task.picture != '0':
        bot.send_photo(call.message.chat.id, open(task.picture, 'rb'))
    # Option verification
    if task.variant3 == '0':
        task_menu.fill_var(2, task.correct, "card", 'wrong_in_card')
        bot.send_message(call.message.chat.id, f"<b>{task.question}</b>\n\n"
                                               f"{task.variant1}\n"
                                               f"{task.variant2}",
                         parse_mode='html', reply_markup=task_menu.get())
    elif task.variant4 == '0':
        task_menu.fill_var(3, task.correct, "card", 'wrong_in_card')
        bot.send_message(call.message.chat.id, f"<b>{task.question}</b>\n\n"
                                               f"{task.variant1}\n"
                                               f"{task.variant2}\n"
                                               f"{task.variant3}",
                         parse_mode='html', reply_markup=task_menu.get())
    elif task.variant5 == '0':
        task_menu.fill_var(4, task.correct, "card", 'wrong_in_card')
        bot.send_message(call.message.chat.id, f"<b>{task.question}</b>\n\n"
                                               f"{task.variant1}\n"
                                               f"{task.variant2}\n"
                                               f"{task.variant3}\n"
                                               f"{task.variant4}",
                         parse_mode='html', reply_markup=task_menu.get())
    else:
        task_menu.fill_var(5, task.correct, "card", 'wrong_in_card')
        bot.send_message(call.message.chat.id, f"<b>{task.question}</b>\n\n"
                                               f"{task.variant1}\n"
                                               f"{task.variant2}\n"
                                               f"{task.variant3}\n"
                                               f"{task.variant4}\n"
                                               f"{task.variant5}",
                         parse_mode='html', reply_markup=task_menu.get())


class Menu:

    # Constructor of Menu()
    def __init__(self, back_button=0, forward_button=0, help_button=0):
        self.markup = types.InlineKeyboardMarkup()
        self.buttons = []
        self.back_button = back_button
        self.forward_button = forward_button
        self.help_button = help_button

    # Adding a new button
    def add(self, button):
        self.buttons.append(button)

    # Building a menu
    def build(self):
        # Building of special markups
        if len(self.buttons) == 26:
            for i in range(0, 24, 4):
                self.markup.row(self.buttons[i], self.buttons[i + 1], self.buttons[i + 2], self.buttons[i + 3])
            self.markup.row(self.buttons[24], self.buttons[25])
        #        elif len(self.buttons) == 40:
        #            for i in range(0, 40, 8):
        #                self.markup.row(self.buttons[i], self.buttons[i + 1], self.buttons[i + 2], self.buttons[i + 3],
        #                                self.buttons[i + 4], self.buttons[i + 5], self.buttons[i + 6], self.buttons[i + 7])
        # Default building
        elif len(self.buttons) % 2 == 0:
            for i in range(0, len(self.buttons), 2):
                self.markup.row(self.buttons[i], self.buttons[i + 1])
        else:
            for i in range(0, len(self.buttons) - 1, 2):
                self.markup.row(self.buttons[i], self.buttons[i + 1])
            self.markup.row(self.buttons[len(self.buttons) - 1])

        # Building of service buttons
        if self.help_button != 0:
            self.markup.row(self.help_button)

        if self.back_button != 0 and self.forward_button == 0:
            self.markup.row(self.back_button)
        elif self.back_button == 0 and self.forward_button != 0:
            self.markup.row(self.forward_button)
        elif self.back_button != 0 and self.forward_button != 0:
            self.markup.row(self.back_button, self.forward_button)

    # Filling a menu with numbered buttons
    def fill_num(self, menu_type, count):
        for number in range(count):
            self.add(types.InlineKeyboardButton(f'{number + 1}', callback_data=f'{menu_type}{number + 1}'))

    # Filling a question menu
    def fill_var(self, count, correct, callback, wrong='wrong'):
        for i in range(count):
            self.add(types.InlineKeyboardButton(f'{i + 1}', callback_data=wrong))
            if i + 1 == int(correct):
                self.buttons[i].callback_data = callback

    # Returning a prepared markup
    def get(self):
        self.build()
        return self.markup

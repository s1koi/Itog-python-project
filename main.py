import telebot 
from config import token
from logic import Pokemon, Wizard, Fighter
from random import randint

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
    Приветствую!
    
    Я бот для игры в Покемонов!
    Вот все команды которые у меня есть:
    /go для получения своего покемона
    /attack (в ответ на сообщение) начать битву с соперником
    /reload пересоздать покемона (есть откат в 12ч)
    /info информация о твоем покемоне
    /feed покормить покемона(можно получить бонус) с откатом в несколько минут
    /gacha испытать удачу и можно получить разные приятные бонусы(откат 12ч)
    /anim получить анимацию покемона
    """
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать") 
    
@bot.message_handler(commands=['reload'])
def reload(message):
        bot.reply_to(message, "Покемон пересоздан!")
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())\
        
@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.reply_to(message, pok.info())
        bot.send_photo(message.chat.id, pok.show_img())
    else:
        bot.reply_to(message, "покемона нету")

@bot.message_handler(commands=['anim'])
def anim(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_video(message.chat.id, pok.anim())
    else:
        bot.reply_to(message, "покемона нету")

@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        result = pokemon.feed()
        bot.reply_to(message, result)
        
    else:
        bot.reply_to(message, "У вас нет покемона. Создайте его с помощью /go")
@bot.message_handler(commands=['gacha'])
def gacha(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        result = pokemon.gacha()
        bot.reply_to(message, result)
        
    else:
        bot.reply_to(message, "произошла какая-то ошибка")
bot.infinity_polling(none_stop=True)


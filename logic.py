from random import randint
import requests
from datetime import datetime, timedelta


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.atk = self.get_atk()
        self.deff = self.get_deff()
        self.rare = self.rare() 
        self.gif = self.get_gif()
        self.last_feed_time = datetime.now()
        
        self.last_gacha_time = datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self
    def rare(self):
        if self.pokemon_number >= 1 and self.pokemon_number < 500:
            rare = "редкий"
        elif self.pokemon_number > 500 and self.pokemon_number < 600 :
            rare = "супер редкий"
            self.atk =+ 1
            self.hp =+ 5
        elif self.pokemon_number > 600 and self.pokemon_number < 700 :
            rare = "ультра редкий"
            self.atk =+ 5
            self.hp =+ 10
        elif self.pokemon_number > 700 and self.pokemon_number < 800 :
            rare = "эпический"
            self.atk =+ 10
            self.hp =+ 20
        elif self.pokemon_number > 800 and self.pokemon_number < 950 :
            rare = "мифический"
            self.atk =+ 20
            self.hp =+ 30
        elif self.pokemon_number > 950 and self.pokemon_number < 1000 :
            rare = "легендарный"
            self.atk =+ 50
            self.hp =+ 40
        return (rare)
    
    def feed(self, feed_interval = 5, hp_increase = 10):
        current_time = datetime.now()  
        delta_time = timedelta(minutes=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            chanse = randint(1,50)
            if chanse == 1:
                self.hp += hp_increase
                self.hp += hp_increase
                self.hp += hp_increase
                self.last_feed_time = current_time
                return "Тебе улыбнулась удача и здоровье покемона увеличено x3!"
            self.hp += hp_increase
            self.last_feed_time = current_time

            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"
    
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
    
    # Метод для получения имени покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Ne povezlo ne fortanulo"
    def get_gif(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['showdown']['front_default'])
        else:
            return "Ne povezlo ne fortanulo"
    
    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][0]['base_stat'])
        else:
            return "Ne povezlo ne fortanulo"
    
    def get_atk(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][1]['base_stat'])
        else:
            return "Ne povezlo ne fortanulo"
        
    def get_deff(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][2]['base_stat'])
        else:
            return "Ne povezlo ne fortanulo"
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            шанс = randint(1,5)
            if шанс == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.atk:
            enemy.hp -= self.atk
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"

        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    def gacha(self):
        chance = randint(1,100)
        current_time = datetime.now()  
        delta_time = timedelta(hours=12)  
        if (current_time - self.last_gacha_time) > delta_time:
            if chance <= 50:
                return f"эх, увы, но тебе ничего не выпало, попробуй позже в {current_time+delta_time}"
            elif chance > 50 and chance <= 75:
                self.atk += 10
                return f"тебе выпало увеличение атаки! следующая попытка {current_time+delta_time}"
            elif chance > 75 and chance <= 100:
                self.hp += 15
                return f"тебе выпало увеличение хп! следующая попытка {current_time+delta_time}"
        return f"Следующее время испытания удачи: {current_time+delta_time}"
    
    def anim(self):
        return self.gif
        

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\n\nHP покемона: {self.hp}\n\nATK покемона: {self.atk}\n\nзащита покемона: {self.deff}\n\nРедкость: {self.rare}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def show_hp(self):
        return self.hp


class Wizard(Pokemon):
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            шанс = randint(1,5)
            if шанс == 1:
                return "Покемон-волшебник применил щит в сражении"
    def feed(self, feed_interval=20, hp_increase=20):
        return super().feed(feed_interval, hp_increase)
    def info(self):
        base_info = super().info()
        return "У тебя покемон-волшебник\n\n" + base_info

class Fighter(Pokemon):
    def attack(self, enemy):
        супер_сила = randint(5,15)
        self.atk += супер_сила
        результат = super().attack(enemy)
        self.atk -= супер_сила
        return результат + f"\nБоец применил супер-атаку силой:{супер_сила} "
    def feed(self, feed_interval=10, hp_increase=10):
        return super().feed(feed_interval, hp_increase)
    def info(self):
        base_info = super().info()
        return "У тебя покемон-боец!\n\n" + base_info






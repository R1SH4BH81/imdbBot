import telebot
import logging
import pyfiglet
import imdb
import datetime
from telebot import types

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Instantiate bot
bot = telebot.TeleBot('')
word = pyfiglet.figlet_format('SERVER   IS ONLINE')
print(word)


@bot.message_handler(commands=['start'])
def start(message):
    user_first_name = str(message.chat.first_name)
    user_last_name = str(message.chat.last_name)
    current_time = datetime.datetime.now().time()
    if current_time.hour < 12:
        msge_1 = f"Gᴏᴏᴅ Mᴏʀɴɪɴɢ {user_first_name} 🌤️ \n What would to like to watch today ?  "
    elif current_time.hour < 16:
        msge_1 = f" Gᴏᴏᴅ AFᴛᴇʀɴᴏᴏɴ {user_first_name}  🌞 \n What would to like to watch today ?"
    elif current_time.hour < 20:
        msge_1 = f"Gᴏᴏᴅ Eᴠᴇɴɪɴɢ {user_first_name}  🌥️\n What would to like to watch today ?"
    else:
        msge_1 = f" Hi {user_first_name}  \n What would to like to watch today ?"

    logger.info(f"User {user_first_name} started the conversation.")

    bot.send_message(message.chat.id, msge_1)
    bot.register_next_step_handler(message, movies69)


def movies69(message):
    user_input = message.text
    bot.send_message(message.chat.id, "Fetching Data \n Hold on Tight !")

    ia = imdb.IMDb()
    search_results = ia.search_movie(user_input)
    movie_id = search_results[0].getID()  # get the first search result (assuming it's the correct movie)
    movie = ia.get_movie(movie_id)  # retrieve information about the movie using the movie ID
    bot.send_message(message.chat.id, f"Title: {movie['title']}")
    bot.send_message(message.chat.id, f"Year: {movie['year']}")
    bot.send_message(message.chat.id, f"Genres: {', '.join(movie['genres'])}")
    bot.send_message(message.chat.id, f"Runtime: {movie['runtime'][0]} minutes")
    bot.send_message(message.chat.id, f"Rating: {movie['rating']}")
    bot.send_message(message.chat.id, f"Cast: {', '.join([c['name'] for c in movie['cast'][:5]])}")

    '''keyboard = types.ReplyKeyboardMarkup(row_width=2)
    yes_button = types.KeyboardButton(text="Yes")
    no_button = types.KeyboardButton(text="No")
    keyboard.add(yes_button, no_button)
    bot.send_message(message.chat.id, "Do you want to see related content?", reply_markup=keyboard)
    bot.register_next_step_handler(message, handle_related_content_response)

    # Fix indentation of handle_related_content_response
    def handle_related_content_response(message):
        if message.text == "Yes":
            movie_id = search_results[1].getID() # get the first search result (assuming it's the correct movie)
            movie = ia.get_movie(movie_id) # retrieve information about the movie using the movie ID
            bot.send_message(message.chat.id,f"Title: {movie['title']}")
            bot.send_message(message.chat.id,f"Year: {movie['year']}")
            bot.send_message(message.chat.id,f"Genres: {', '.join(movie['genres'])}")
            bot.send_message(message.chat.id,f"Runtime: {movie['runtime'][0]} minutes")
            bot.send_message(message.chat.id,f"Rating: {movie['rating']}")
            bot.send_message(message.chat.id,f"Cast: {', '.join([c['name'] for c in movie['cast'][:5]])}")
        
        elif message.text == "No":
            bot.send_message(message.chat.id, "Your majesty...")
        
        else:
            bot.send_message(message.chat.id, "Invalid input. Please choose 'Yes' or 'No'.")'''


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    list54 = ['😞', '😔', '😟', '😕', '🙁', '☹', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '🧐', '🤨', '🤔']
    import random
    list4 = random.choice(list54)
    bot.send_message(message.chat.id, list4)
    bot.send_message(message.chat.id, 'Unrecognized command see menu\n👇            /refresh_page')


bot.polling()

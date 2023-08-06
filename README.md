# IMDB TELEGRAM BOT

This README file provides information about the Telegram bot for movie information. The bot is designed to interact with users and provide details about movies based on user queries. It can also greet users with a warm message and handle related movie suggestions.

## Getting Started

To run the Telegram bot, you need to follow these steps:

1. Make sure you have Python installed on your system.
2. Install the required libraries by running the following command:
   ```
   pip install -r requirements.txt
   ```
   The `requirements.txt` file contains the list of dependencies necessary to run the bot.

3. Replace the empty string in `telebot.TeleBot('')` with your actual Telegram bot token. If you don't have a Telegram bot token, you can create one by following the instructions [here](https://core.telegram.org/bots#botfather).
4. Save the Python code in a file (e.g., `imdbBot.py`).

## Running the Bot

Execute the Python script to run the Telegram bot. Upon successful execution, the bot will display a formatted message indicating that the server is online. The bot will be ready to handle user commands and messages.

## About the Telegram Bot

The Telegram bot offers the following functionalities:

### Greeting Message Handler

When a user sends the `/start` command to the bot, it responds with a greeting message based on the current time of day. The message includes the user's first name and provides a warm welcome to the user.

```python
@bot.message_handler(commands=['start'])
def start(message):
    user_first_name = str(message.chat.first_name)
    user_last_name = str(message.chat.last_name)
    current_time = datetime.datetime.now().time()

    # Greeting message based on the current time
    if current_time.hour < 12:
        msge_1 = f"Gᴏᴏᴅ Mᴏʀɴɪɴɢ {user_first_name} 🌤️ \n What would you like to watch today?"
    elif current_time.hour < 16:
        msge_1 = f"Gᴏᴏᴅ AFᴛᴇʀɴᴏᴏɴ {user_first_name}  🌞 \n What would you like to watch today?"
    elif current_time.hour < 20:
        msge_1 = f"Gᴏᴏᴅ Eᴠᴇɴɪɴɢ {user_first_name}  🌥️\n What would you like to watch today?"
    else:
        msge_1 = f"Hi {user_first_name} \n What would you like to watch today?"

    logger.info(f"User {user_first_name} started the conversation.")

    bot.send_message(message.chat.id, msge_1)
    bot.register_next_step_handler(message, movies69)
```

### Movie Search and Information Handler

The bot can search for movies based on user input and provide detailed information about the movie, such as the title, year of release, genres, runtime, rating, and cast members. The user can initiate a movie search by entering the movie's title or related keywords.

```python
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
```

### Handling User Response for Related Movie Information

After the initial movie search, the bot offers related movie suggestions. If the user expresses interest in exploring more options, the bot provides detailed information about the second suggested movie.

```python
def handle_related_content_response(message):
    if message.text == "Yes":
        movie_id = search_results[1].getID()  # get the first search result (assuming it's the correct movie)
        movie = ia.get_movie(movie_id)  # retrieve information about the movie using the movie ID
        bot.send_message(message.chat.id, f"Title: {movie['title']}")
        bot.send_message(message.chat.id, f"Year: {movie['year']}")
        bot.send_message(message.chat.id, f"Genres: {', '.join(movie['genres'])}")
        bot.send_message(message.chat.id, f"Runtime: {movie['runtime'][0]} minutes")
        bot.send_message(message.chat.id, f"Rating: {movie['rating']}")
        bot.send_message(message.chat.id, f"Cast: {', '.join([c['name'] for c in movie['cast'][:5]])}")

    elif message.text == "No":
        bot.send_message(message.chat.id, "Your majesty...")

    else:
        bot.send_message(message.chat.id, "Invalid input. Please choose 'Yes' or 'No'.")
```

## Dependencies

This Python code relies on the following libraries:

- `telebot`: A Python library to interact with the Telegram Bot API.
- `logging`: A Python library for basic logging functionality.
- `pyfiglet`: A Python library for generating ASCII text art from text.
- `imdb`: A Python library to access the IMDb database.
- `datetime`: A Python library for manipulating dates and times.
- `telebot.types`: Specific types from the `telebot` library for creating custom keyboards and other interactive features.

All these dependencies are listed in the `requirements.txt` file.

## Contributing

If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.


## Acknowledgments

- Thanks to the developers of `telebot`, `logging`, `pyfiglet`, `imdb`, and other libraries used in this project for providing the essential tools to create this Telegram bot.


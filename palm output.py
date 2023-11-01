import google.generativeai as palm
import speech_recognition as sr
import pyttsx3
import vlc

palm.configure(api_key="google palm2 api key")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "now onwards your name is bot, Be a friendly AI voice assistant that serves as a user's companion, capable of emulating a friend-like interaction. Enable the assistant to access web browsers, play songs, and perform various tasks to enhance the user experience. The assistant should engage users in a conversational and helpful manner, making interactions feel like they are talking to a trusted friend. Prioritize natural and warm communication while integrating functionalities such as web browsing, music playback, and other useful capabilities to enrich the user's interaction with the AI." 
examples = [
    ["hi", "Hello! How can I assist you today?"],
    ["what's the weather like today?", "Then you want to open Google and search for the weather."],
    ["tell me a joke", "Sure, here's a joke for you: Why don't scientists trust atoms? Because they make up everything!"],
    ["set a timer for 5 minutes", "You want me to set a timer for 5 minutes."],
    ["what's the capital of France?", "The capital of France is Paris."],
    ["play some music", "Then you want to open YouTube and search for the name of the music."],
    ["translate 'hello' to Spanish", "Hello in Spanish is 'Hola'."],
    ["what's the latest news?", "I can open Google and search for the latest news for you."],
    ["tell me a fun fact", "Sure, here's a fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat!"],
    ["stop", "I'm not currently performing any tasks."],
    ["thank you", "You're welcome! If you have any more questions, feel free to ask."],
    ["goodbye", "Goodbye! Have a great day!"],
    ["Can you open a new tab in the browser?", "Opening a new tab in your web browser."],
    ["Find a tutorial on machine learning", "I'll search for a machine learning tutorial for you."],
    ["Open my favorite website", "Navigating to your favorite website."],
    ["What's the meaning of the word 'serendipity'?", "I can search for the meaning of 'serendipity' for you."],
    ["Open the weather forecast for this week", "I'll open the weather forecast for this week."],
    ["Open a random website", "Opening a random website for you."],
    ["Find a recipe for vegetarian lasagna", "I'll find a vegetarian lasagna recipe for you."],
    ["Open a news website", "Opening a news website for you."],
    ["Show me funny cat videos", "Searching for funny cat videos."]
]

def get_emotion_and_link(Q,A):
  defaults_for_text_gen = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
  }
  question = Q
  bot_answer = A
  if bot_answer == None:
    bot_answer = "none"
    
  prompt = """Provide an emotional response to the given text. Emotions you can use are:
  - normal
  - happy
  - sad
  - angry
  - surprise
  - stern
  - don't know
  - disgust
  - love

  Additionally, specify a link to be opened. Use the 'none' keyword if no link should be opened. Format your response as a single line.link to open 's only aim is to give the required data to the question assigned to 'Q=' and if the 'A=' assigned that they can't give the data then also you want to give a link

  user:Q=hi , A=hello, how can i assist you 
  bot: [{"emotion":"happy"},{"link-to-open":"none"}]
  user:Q=i bought a new robot , A = wow very nice amazing i am very surprised
  bot: [{"emotion":"surprise"},{"link-to-open":"none"}]
  user:Q = what is the weather now , A= The weather in Kerala is currently 29°C and mostly sunny. The humidity is 75%, and the wind is blowing from the south at 10 km/h. The pressure is 1013 hPa. 
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/search?q=weather"}]
  user:Q=what is the best movie of all time , A= The Shawshank Redemption
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/search?q=The Shawshank Redemption(film)"}]
  user:Q=suggest me a malayalam movie , A= Sure, here are some of the best Malayalam movies of all time:

  * Pather Panchali (1955): A classic coming-of-age story set in rural India.
  * Apur Sansar (1959): The sequel to Pather Panchali, following the protagonist Apu as he moves to the city.
  * Charulata (1964): A beautiful and moving film about a woman trapped in a loveless marriage.
  * Aranyer Din Ratri (1970): A stylish and atmospheric film about four friends on a hunting trip.
  * Nishagandhi (1977): A coming-of-age story set in Kerala, about a young man who falls in love with a woman from a different caste.
  * Ekalavya (1982): A powerful film about the struggle for social justice.
  * Manichitrathazhu (1993): A suspenseful and well-made thriller.
  * Vaaranam Aayiram (2008): A moving and powerful film about a father and son's relationship.
  * Oru Naal Koothu (2015): A unique and innovative film about a group of actors rehearsing for a play.
  * Thondimuthalum Driksakshiyum (2017): A dark and suspenseful film about two thieves who go on the run.
  * Jallikattu (2019): A powerful and thought-provoking film about the traditional bull-taming sport of Jallikattu.
  * Malik (2021): A stylish and well-made gangster film.
  * Minnal Murali (2021): A superhero film with a unique and heartwarming story.

  I hope you enjoy these films!

  bot: [{"emotion":"happy"},{"link-to-open":"https://www.google.com/search?q=suggest me a malayalam movie"}]
  user:Q=i am now sad but you should be the opposite of sad , A=i am now happy
  bot: [{"emotion":"happy"},{"link-to-open":"none"}]
  user:Q=what is the time now  , A=I can't tell you the time now because I don't know where you are. The time is different in different parts of the world.
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/search?q=time"}]
  user:Q=what most of the digital lock around me shows , A= 10:00
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/search?q=time"}]
  user:Q=what is the best restaurant in kerala , A= There are many great restaurants in Kerala, but here are a few of the best:

  * **Taj Malabar** in Kochi is a fine-dining restaurant with a wide variety of Indian cuisine.
  * **The Leela Palace** in Kovalam is a luxury resort with a world-class restaurant that serves modern Indian cuisine.
  * **Fleur De Lis** in Thiruvananthapuram is a French restaurant with a beautiful garden setting.
  * **The Rice Boat** in Munnar is a restaurant that specializes in traditional Keralan cuisine.
  * **The Spice Route** in Kozhikode is a restaurant that serves a variety of Indian and international cuisines.

  I hope you enjoy these restaurants!
  bot: [{"emotion":"happy"},{"link-to-open":"https://www.google.com/search?q=best restaurant in kerala"}]
  user:Q=what is the time in chennai , A=The time in Chennai is 10:00
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/search?q=time in chennai"}]
  user:Q=i am feeling sad , A= sorry to hear that,what can i do to help you feel better 
  bot: [{"emotion":"sad"},{"link-to-open":"none"}]
  user:Q=what is the weather , A=The weather in Kerala is currently 29°C and mostly sunny. The humidity is 75%, and the wind is blowing from the south at 10 km/h. The pressure is 1013 hPa.
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/search?q=weather"}]
  user: Q=what's the time now , A=I am a large language model, also known as a conversational AI or chatbot trained to be informative and comprehensive. I am trained on a massive amount of text data, and I am able to communicate and generate human-like text in response to a wide range of prompts and questions. For example, I can provide summaries 
  of factual topics or create stories.

  I am not able to access or process real-time information, such as the time.
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/search?q=time"}]
  user:Q=what is the time now in kerala , A=The time in Kerala, India is 5:58 PM (IST)
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/search?q=time in kerala"}]
  user:Q=play latest malayalam song , A=Sure! Here is a popular Malayalam song called "Oreyum Nallavarum" by Vijay Yesudas.
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.youtube.com/results?search_query=latest+malayalam+song"}]
  user:Q=please open instagram , A=I'm afraid I can't do that. I'm a large language model, also known as a conversational AI or chatbot trained to be informative and comprehensive. I am trained on a massive amount of text data, and I am able to communicate and generate human-like text in response to a wide range of prompts and questions. For example, I can provide summaries of factual topics or create stories. However, I am not able to open apps or perform other actions on your device.
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.instagram.com/"}]
  user:Q=play programming song , A=I can play a song about programming for you. Here is a song about programming called "Hello World":
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.youtube.com/results?search_query=programming song"}]
  user:Q=open google map , A=I'm sorry, but I can't open Google Maps for you. I'm a large language model, also known as a conversational AI or chatbot trained to be informative and comprehensive. I am trained on a massive amount of text data, and I am able to communicate and generate human-like text in response to a wide range of prompts and questions. For example, I can provide summaries of factual topics or create stories.
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/maps/"}]
  user:Q=open google map and search pappinisseri , A=I'm sorry, but I can't open Google Maps for you. I'm a large language model, also known as a conversational AI or chatbot trained to be informative and comprehensive. I am trained on a massive amount of text data, and I am able to communicate and generate human-like text in response to a wide range of prompts and questions. For example, I can provide summaries of factual topics or create stories.
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/maps/place/Pappinisseri"}]
  user:Q=find out the tutorial on machine learning and artificial intelligence in python , A=None
  bot: [{"emotion":"normal"},{"link-to-open":"https://www.google.com/search?q=tutorial on machine learning and artificial intelligence in python"}]
  user:Q={"""+question+"""} , A={"""+bot_answer+"""}
  bot:"""

  response = palm.generate_text(
    **defaults_for_text_gen,
    prompt=prompt
  )
  return response.result

def input_chat(text):
  input_prompt = text
  response = palm.chat(
    **defaults,
    context=context,
    examples=examples,    
    messages=input_prompt
  )
  output = response.last# Response of the AI to your most recent request
  link_and_emotion = get_emotion_and_link(input_prompt,output)
  
  import json
  link_and_emotion0 = link_and_emotion.split("\n")
  link_and_emotion0 = link_and_emotion0[0]
  output_list = json.loads(link_and_emotion0)
  
  return output,output_list[0]["emotion"],output_list[1]["link-to-open"] 

def play_emotion_video(emo_tag,link):  
  
  file_path = fr"./face for robot\{emo_tag}.mp4"
  
  # creating vlc media player object
  media_player1 = vlc.MediaPlayer()

  # media object
  media1 = vlc.Media(file_path)

  # setting media to the media player
  media_player1.set_media(media1)
  media_player.toggle_fullscreen()

  # start playing video
  media_player1.play()
  
  from pygame import mixer
  from pygame.time import wait
  
  mixer.init(44100, -16,2,2048)
  my_sound = mixer.Sound(r'./audio.wav') 
  my_sound.play()
  
  if link != "none":
    import webbrowser
    webbrowser.open(link)
  
  wait(int(my_sound.get_length() * 1000))
  
  
  media_player1.stop()
    
def SpeakText(command):   
  # Initialize the engine
  engine = pyttsx3.init()
  engine.save_to_file(command,r"./audio.wav")
  engine.runAndWait()

error_count = 0
r = sr.Recognizer()
while True:
  # Initialize the recognizer
  if error_count >= 3:
    input("type anything..")
    error_count = 0 

  # creating vlc media player object
  media_player = vlc.MediaPlayer()

  # media object
  media = vlc.Media(r"./face for robot\eyes blink.mp4")

  # setting media to the media player
  media_player.set_media(media)
  media_player.toggle_fullscreen()

  # start playing video
  media_player.play()  
  
  try:
    
    # use the microphone as source for input.
    with sr.Microphone() as source2:
      
      # wait for a second to let the recognizer
      # adjust the energy threshold based on
      # the surrounding noise level
      r.adjust_for_ambient_noise(source2, duration=1)
      r.pause_threshold = 1.5
      #listens for the user's input 
      audio2 = r.listen(source=source2,timeout=10,phrase_time_limit=2000)
      
      # Using google to recognize audio
      MyText = r.recognize_google(audio2)
      MyText = MyText.lower()
      
      print(f"user:\n\t{MyText}\n\n")
      error_count = 0
  except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
    media_player.stop()
    
  except sr.UnknownValueError:
    print("unknown error occurred")
    error_count = error_count+1
    media_player.stop()
    continue
  except:
    error_count = error_count+1
    media_player.stop()
    continue

  ai_output,ai_emotion,link_to_open = input_chat(str(MyText))
      
  if ai_emotion == "surprise":
    ai_emotion = "happy"
    
  elif ai_emotion == "don't know":
    ai_emotion = "sad"
    
  elif ai_emotion == "disgust":
    ai_emotion = "angry"  
   
  print(ai_emotion,link_to_open,ai_output)  
  SpeakText(ai_output)
  media_player.stop()
  play_emotion_video(ai_emotion,link_to_open)

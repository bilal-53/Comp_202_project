print("Bot or Human? Let's figure this out !")

# Unchanging values
BEG_BOT_RESPONSE_HOUR = 2
END_BOT_RESPONSE_HOUR = 5
MIN_RESPONSE_TIME_HUM = 0.15 # 9 seconds = 0.15 minutes
MIN_WPM_HUM = 66
BOT_TYPOS = 0
NUMBER_OF_T = 3

# Asking for the hour of response and checking if it corresponds to a bot
hour_of_response = float(input('When did you receive your response \
(type a float between 0 and 24)? '))
if BEG_BOT_RESPONSE_HOUR <= hour_of_response <= END_BOT_RESPONSE_HOUR:
    print('You just talked to a bot')

# Asking for response time and verifying if it corresponds to a bot
else:
    response_time = float(input('How long did it take to get \
your response (in min)? '))
    if response_time < MIN_RESPONSE_TIME_HUM:
      print('You just talked to a bot')

# Asking for numbers of words to calculate wpm
    else:
        number_of_words = int(input('How many words in your response? '))
        wpm = number_of_words / response_time
        if wpm < MIN_WPM_HUM:
           print('You just talked to a fellow human')

# Asking if there are typos to see if it is a human
        else:
            typos =  int(input('How many typos in the \
response (grammatical errors, mispelled words, etc.)? '))
            if typos != BOT_TYPOS:
                print('You just talked to a fellow human')
             
# Test the responder to conclude on the identity of the responder 
            else:
                test = int(input("Ask the responder how many 't' \
there are in 'eeooeotetto' and type their answer? "))
                if test == NUMBER_OF_T:
                    print('You just talked to a fellow human')
                else:
                    print('You just talked to a bot')
import pywhatkit as pw

text = '''1. QR Code Generator

alias : Pet Name : Alternative Name

2. Email Validation in Python (Using String Functions)

3. How to trace mobile number current location

4. Email Validation in Python (Using Regex)

5. How to make a Simplest Instagram Bot in Python

6. Voice Assistant in Python

#Convert Voice to Text
#Speech Recognizer
#Convert Text to Speech

#Additional Modules
#web browser
#pyjokes
#SMTP
#datetime
#pyttsx3

(source: Any, timeout: Any | None = None, phrase_time_limit: Any | None = None, snowboy_configuration: Any | None = None) -> AudioData
Records a single phrase from source (an AudioSource instance) into an AudioData instance, which it returns.

This is done by waiting until the audio has an energy above recognizer_instance.energy_threshold (the user has started speaking), and then recording until it encounters recognizer_instance.pause_threshold seconds of non-speaking or there is no more audio input. The ending silence is not included.

The timeout parameter is the maximum number of seconds that this will wait for a phrase to start before giving up and throwing an speech_recognition.WaitTimeoutError exception. If timeout is None, there will be no wait timeout.

The phrase_time_limit parameter is the maximum number of seconds that this will allow a phrase to continue before stopping and returning the part of the phrase processed before the time limit was reached. The resulting audio will be the phrase cut off at the time limit. If phrase_timeout is None, there will be no phrase time limit.

The snowboy_configuration parameter allows integration with Snowboy <https://snowboy.kitt.ai/>__, an offline, high-accuracy, power-efficient hotword recognition engine. When used, this function will pause until Snowboy detects a hotword, after which it will unpause. This parameter should either be None to turn off Snowboy support, or a tuple of the form (SNOWBOY_LOCATION, LIST_OF_HOT_WORD_FILES), where SNOWBOY_LOCATION is the path to the Snowboy root directory, and LIST_OF_HOT_WORD_FILES is a list of paths to Snowboy hotword configuration files (*.pmdl or *.umdl format).

This operation will always complete within timeout + phrase_timeout seconds if both are numbers, either by returning the audio data, or by raising a speech_recognition.WaitTimeoutError exception.

7. Send Emails Using Python

8. Typing Speed Calculator

9. How to Make Google Translator

10. Sign Language Translator in Python

11. Text to Handwriting Using Python

12. 

'''

pw.text_to_handwriting(text, 'Hand_Written_Notes.png', (0, 0, 0))
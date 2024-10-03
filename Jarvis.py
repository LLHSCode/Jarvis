import ollama
import time
import pyttsx3
import pygame
import os

pygame.init()
pygame.mixer.music.load('e:\download\AI\AI\Jarvis.mp3')
pygame.mixer.music.play()

os.system('cls')

print("你好，我是Jarvis，请问有什么可以帮助您？")

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def stream_response(response):
    for chunk in response:
        yield chunk['message']['content']

while True:
    start = input('>>> ')
    if start == '/exit':
        break
    question = start +'。回答要求：中文简洁回答，回答完问题后在末尾加"先生"'
    response = ollama.chat(model='Jarvis', messages=[
    {
        'role': 'user',
        'content': question,
    },
    ], stream=True)  
    record = ''
    for word in stream_response(response):
        print(word,end='',flush=True)
        record += word
    pyttsx3.speak(record)
    print()
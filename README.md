# RPiPico-Telegram-Bot
Simple Telegram Bot which can can run on Raspberry Pi Pico.
It can be used for IOT projects.Can use OPEN AI for integrations and all!!!

# About RPiPico-Telegram-Bot
A Raspberry Pi Pico Telegram bot is a small, low-cost computer board that can be programmed to interact with the popular messaging app, Telegram. The Raspberry Pi Pico is a microcontroller board with a powerful processor that allows it to run custom programs written in a variety of programming languages. With the right software and programming, the board can connect to the Telegram API to send and receive messages, images, and other types of media. This makes it possible to build chatbots, notification systems, or other types of messaging applications that can be controlled remotely via Telegram. The Raspberry Pi Pico Telegram bot is a fun and interesting way to explore the possibilities of combining hardware and software to create new and innovative projects.

# Things to have or required

1- Raspberry Pi Pico W 
2- Pc/Laptop
3- Good Wifi or Internet Access

# How it works

Since Pico cant store wifi credentials, we need to write the code to connect to wifi everytime we run the code.
After that the main program where its uses the Telegram API for getting and sending messaging.

# Modules Used

Since Pico come with pre installed Python modules called Micro Python Modules.We cant installed any other modules other than that.
So we use in-built modules like:
1- urequests
2- time
3- machine

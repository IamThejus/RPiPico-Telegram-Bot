# Simple Telegram Bot for Raspberry Pi Pico

from machine import Pin
import time
import network
import urequests
import ujson

sys_led=Pin('LED',Pin.OUT)



sys_led.value(0)



def led_indicator():
    sys_led.value(1)
    time.sleep(0.5)
    sys_led.value(0)
    



wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID OR WIFI NAME', 'PASSWORD')

_thread.start_new_thread(set_program_off_on,())

url='https://api.telegram.org/bot{}/'
api_key='YOUR API TOKEN'

base_url=url.format(api_key)



def get_updates(offset):
    data=urequests.get(base_url+'getUpdates?offset={}'.format(offset))
    json_data=ujson.loads(data.content.decode('utf-8'))
    return json_data

def get_latest_offest():
    data=urequests.get(base_url+'getUpdates')
    json_data=ujson.loads(data.content.decode('utf-8'))
    return json_data['result'][1]['update_id']

def send_message(text, chat_id):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(api_key)
    payload = {'chat_id': chat_id, 'text': text}
    response = urequests.post(url, json=payload)
    return response.json()


led_indicator()
print('Program started')


condtion=False
while condtion==False:
    try:
        offset=get_latest_offest()
        condtion=True
    except:
        continue



while True:
    data=get_updates(offset)
    if len(data['result'])!=0:
        led_indicator()
        chat_id=data['result'][0]['message']['chat']['id']
        text=data['result'][0]['message']['text']
        first_name=data['result'][0]['message']['chat']['first_name']
        text=text.lower()
        if text=='hi' or text=='hello' or text=='/start':
            send_message('Hello '+str(first_name),chat_id)

        '''Here You can add many more functionality to this code as you like using elfi statement :)'''
        
        else:
            send_message('i dont get u',chat_id)
        
        
        offset+=1
    else:
        continue

'''Usually the program doesnt end unless a error occurs..So if the below commands executes there is something wrong with the program or you used some other function to turn it off'''

print('Program Ended')

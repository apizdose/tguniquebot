import telebot
import os
from PIL import Image, ImageFilter
import random
import time

def tokenTGget():
    with open('token.txt','r') as tokenfile:
        return tokenfile.read()


if os.name == 'nt':
    folderpath='.\\'
else:
    folderpath='./'

transp=False
def tspose(filename):
    im = Image.open(filename)
      
    if transp:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    pix = [(pixel[0], pixel[1], pixel[2]) for pixel in im.getdata()]
    for i in range(20):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255) 

        ran=random.randint(10,(len(pix) - 10))

        pix[ran] = (red, green, blue)

    im.putdata(pix)
    #im = im.filter(ImageFilter.GaussianBlur(3))
    im.save(filename)
    
    


TOKENTG = tokenTGget().rstrip()
bot = telebot.TeleBot(TOKENTG)


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def send_echo(message):
    if '/transp' in message.text:
        global transp
        transp= not transp
        if transp:
            bot.send_message(message.chat.id,'TRANSPOSE ENABLED')
        else:
            bot.send_message(message.chat.id,'TRANSPOSE DISABLED')
        
    bot.send_message(message.chat.id,'Давай уже сюда картиночку свою!')


@bot.message_handler(content_types=['photo'])
def send_photo(message):
    file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = folderpath + file_info.file_path
    with open(src, "wb") as new_file:
        new_file.write(downloaded_file)
    tspose(src)     
    with open(src, "rb") as new_file:
            
        bot.send_photo(message.chat.id, new_file)
        
    randm=random.randint(1,9)
    if randm <=3:
        bot.send_message(message.chat.id,'фыр-фыр-фыр')


print('\n------------------ Running...------------------')

bot.polling()
'''
while True:
    try:
        bot.polling()
    except:
        input('ERROR!')
        continue
        '''

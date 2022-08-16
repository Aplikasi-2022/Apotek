import telebot
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Aplikasi_Apotek2022.settings' 
django.setup()

#from .models import *
from telegram.ext import *
# from .models import Model_kategori
from Aplikasi_Apotek2022.models import Model_kategori

api = '5384687037:AAF6OFTgOSFzJkBRFKzZTyPvMPXPIBLO_bM'
bot = telebot.TeleBot(api)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Selamat Datang Di Apotek (BUNDA)')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    # info
    bot.reply_to(message, 'Informasi Data Layanan Obat Apotek')

#@bot.message_handler(commands=['data'])
def isValidPinCode(pinCode):
    regex = "^[1-9]{1}[0-9]{2}\\S{0,1}[0-9]{3}$";
    p = re.compile(regex)
    if (pinCode == ''):
        return False;
    m = re.match(p, pinCode)
    if m is None:
        return False
    else:
        return True

def here(S):
    return any(i.isdigit() for i in S)

def tampildata(update, context):
    text = str(update.message.text).lower()
    
    data_obat = Model_kategori.objects.all()
    message = f""" Total Daftar Obat {data_obat.count()} """
            
    for data in data_obat:              
                message += f"""Apotek (BUNDA)

                            Nama Obat = {data.nama_kategori}    
                            Harga = {data.harga} 
                            Keterangan = {data.keterangan}  \n \n 

                            """


    update.message.reply_text(f"{message}") 
    return  
    #print(update)
    update.message.reply_text(f"Hi, {update['message']['chat']['first_name']} Informasi Manajemen Apotek (BUNDA) Sidopekso")



print('bot Success Running')
# print(Surat.objects.first())
bot.polling()


if __name__== '__main__':
    updater = Updater(api, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, tampildata))

    updater.start_polling(1.0)
    updater.idle()
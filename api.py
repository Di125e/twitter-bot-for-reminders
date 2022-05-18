
from email import message
from operator import truediv
import tweepy
import schedule
import time

consumer_key="FvMvdT4KZLKEBVwOCKukw7GCF"
consumer_secret="OkT9S2dAIPXXv8menoa2T2cuRC6BoIndQgHGHsGFKpdmp1l0I9"
access_token="1526386194447273984-vzqWX1U3HpjShHHOJuSHwbZaNgQW4I"
access_token_secret="AYnuMKXWhqTZhDpmSr32h0FnF8WzavZovYO8bh7Phw4nK"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def PublicarTweet1 ():
        api.update_status("Hoy es Lunes \n 14:00-15:20 Redes III \n 15:30-16:50 Programación Web \n 17:00-19:10 Lengua Extranjera Técnica \n 19:10-21:20 Proyecto")
def PublicarTweet2 ():
        api.update_status("Hoy es Martes \n 14:00-15:20 Diseño Multimedial \n 15:30-16:50 Aplicaciones en Redes \n 17:00-19:10 Probabilidad y Estadística")
def PublicarTweet3 ():
        api.update_status("Hoy es Miercoles \n 14:00-15:20 Microemprendimiento \n 15:30-16:50 Programación Web \n 17:00-18:20 Proyecto \n 18:30-21:20 Laboratorio de Hardware")
def PublicarTweet4 ():
        api.update_status("Hoy es Jueves \n 14:00-15:20 Sistema Operativo de Red \n 15:30-16:50 Microemprendimiento \n 17:00-19:10 Marco Jurídico")
def PublicarTweet5 ():
        api.update_status("Hoy es Viernes \n 14:00-15:20 Redes III \n 15:30-16:50 Diseño Multimedial \n 17:00-18:20 Aplicaciones en Redes \n 18:30-19:50 Sistema Operativo de Red")
def main():
    schedule.every().monday.at("05:30").do(PublicarTweet1)
    schedule.every().tuesday.at("05:30").do(PublicarTweet2)
    schedule.every().wednesday.at("05:30").do(PublicarTweet3)
    schedule.every().thursday.at("05:30").do(PublicarTweet4)
    schedule.every().friday.at("05:30").do(PublicarTweet5)
    while True: 
        try:
          schedule.run_pending()
        except tweepy.TweepError as e:
          raise e
                
if __name__ == "__main__":
        main()

       
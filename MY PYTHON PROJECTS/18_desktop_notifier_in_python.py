from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title='***Take Rest***',
            message = 'Rest is vital for mental health, increased cencentration and memory, a healthier immune system, reduced stress, improved mood and even a better metabolism.',
            app_icon = 'C:/Users/welcome/Documents/My Files/Python/Python Projects/rest_icon.ico',
            timeout = 5,)
        # time.sleep(60*60)
        # time.sleep(3600)
        time.sleep(20)
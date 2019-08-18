# -*- coding: UTF-8 -*-
####################################
#KeyKmr by Fomegne Meudje          #
#Email: fomegnemeudje@outlook.com  #
####################################
from os import system
system('title KeyKmr by FOMEGNE MEUDJE.')
import keyboard
from time import sleep
import string

print('code KeyKmr')
h="""
af no  af0 yes
af1 af2 etc
New: af4 = ᾰ
-p = ʔ
-* = ’
"""
b=[0]
keyword = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
relay = 0.001
sp_char = '+'

def press_and_release(Key):
    global relay
    if keyboard.is_pressed(Key):
        while keyboard.is_pressed(Key):
            sleep(relay )
            pass
        return True
    else:
        return False

def breaker(x):
    for i in keyword:
        if not i in x:
            if press_and_release(i):
                t = True
                break
        else:
            t = False
    if t:
        return True

def translate():
    global relay
    if press_and_release('a'):#AAAAAAAAAAAAAAAAA
        while True:
            sleep(relay)
            if press_and_release('1'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('à')
                break
            if press_and_release('2'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('á')
                break
            if press_and_release('3'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ā')
                break
            if press_and_release('5'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('â')
                break
            if press_and_release('7'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ǎ')
                break
            if press_and_release('f'):
                while True:
                    sleep(relay)
                    if press_and_release('0'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('α')
                        b[0]=1
                        break
                    if press_and_release('1'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ὰ')
                        b[0]=1
                        break
                    if press_and_release('2'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ά')
                        b[0]=1
                        break
                    if press_and_release('3'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ᾱ')
                        b[0]=1
                        break
                    if press_and_release('4'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ᾰ')
                        b[0]=1
                        break
                    if press_and_release('5'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɑ̂')
                        b[0]=1
                        break
                    if press_and_release('7'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɑ̌')
                        b[0]=1
                        break
                    if press_and_release('backspace'):
                        break
                    if breaker(['0','1','2','3','4','5','7']):break
                    if press_and_release('space'):
                        break
            if press_and_release('e'):
                while True:
                    sleep(relay)
                    if press_and_release(sp_char):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('æ')
                        b[0]=1
                        break
                    if press_and_release('backspace'):
                        break
                    if breaker([sp_char]):break
                    if press_and_release('space'):
                        break
            if press_and_release('i'):
                while True:
                    sleep(relay)
                    if press_and_release('0'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɛ')
                        b[0]=1
                        break
                    if press_and_release('1'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɛ̀')
                        b[0]=1
                        break
                    if press_and_release('2'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('έ')
                        b[0]=1
                        break
                    if press_and_release('3'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɛ̄')
                        b[0]=1
                        break
                    if press_and_release('5'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɛ̂')
                        b[0]=1
                        break
                    if press_and_release('7'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɛ̌')
                        break
                    if press_and_release('backspace'):
                        break
                    if breaker(['0','1','2','3','5','7']):break
                    if press_and_release('space'):
                        break
            if press_and_release('backspace'):
                break
            if breaker(['0','1','2','3','5','7']):break
            if press_and_release('space'):
                break
            if b[0] is 1:
                b[0]=0
                break

                break

    if press_and_release('e'):#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        while True:
            sleep(relay)
            if press_and_release('1'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('è')
                break
            if press_and_release('2'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('é')
                break
            if press_and_release('3'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ē')
                break
            if press_and_release('5'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ê')
                break
            if press_and_release('7'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ě')
                break
            if press_and_release('u'):
                while True:
                    sleep(relay)
                    if press_and_release('0'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ə')
                        b[0]=1
                        break
                    if press_and_release('1'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ə̀')
                        b[0]=1
                        break
                    if press_and_release('2'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ə́')
                        b[0]=1
                        break
                    if press_and_release('3'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ə̄')
                        b[0]=1
                        break
                    if press_and_release('5'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ə̂')
                        b[0]=1
                        break
                    if press_and_release('7'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ə̌')
                        b[0]=1
                        break
                    if press_and_release('backspace'):
                        break
                    if breaker(['0','1','2','3','5','7']):break
                    if press_and_release('space'):
                        break
            if press_and_release('backspace'):
                break
            if breaker(['0','1','2','3','5','7']):break
            if press_and_release('space'):
                break
            if b[0] is 1:
                b[0]=0
                break

    if press_and_release('i'):#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        while True:
            sleep(relay)
            if press_and_release('1'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ì')
                break
            if press_and_release('2'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('í')
                break
            if press_and_release('3'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ī')
                break
            if press_and_release('5'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('î')
                break
            if press_and_release('7'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ǐ')
                break
            if press_and_release('backspace'):
                break
            if breaker(['0','1','2','3','5','7']):break
            if press_and_release('space'):
                break
    if press_and_release('o'):#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        while True:
            sleep(relay)
            if press_and_release('1'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ò')
                break
            if press_and_release('2'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ó')
                break
            if press_and_release('3'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ō')
                break
            if press_and_release('5'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ô')
                break
            if press_and_release('7'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ǒ')
                break
            if press_and_release('/'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ø')
                break
            if press_and_release(sp_char):
                while True:
                    sleep(relay)
                    if press_and_release('0'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɔ')
                        b[0]=1
                        break
                    if press_and_release('1'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɔ̀')
                        b[0]=1
                        break
                    if press_and_release('2'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɔ́́')
                    if press_and_release('3'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɔ̄')
                        b[0]=1
                        break
                    if press_and_release('5'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɔ̂')
                        b[0]=1
                        break
                    if press_and_release('7'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɔ̌')
                        b[0]=1
                        break
                    if press_and_release('backspace'):
                        break
                    if breaker(['0','1','2','3','5','7']):break
                    if press_and_release('space'):
                        break
            if press_and_release('e'):
                while True:
                    sleep(relay)
                    if press_and_release(sp_char):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('œ')
                        b[0]=1
                        break
                    if press_and_release('backspace'):
                        break
                    if breaker([sp_char]):break
                    if press_and_release('space'):
                        break
            if press_and_release('backspace'):
                break
            if breaker(['0','1','2','3','5','7']):break
            if press_and_release('space'):
                break
            if b[0] is 1:
                b[0]=0
                break
    if press_and_release('u'):#UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
        while True:
            sleep(relay)
            if press_and_release('1'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ù')
                break
            if press_and_release('2'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ú')
                break
            if press_and_release('3'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ū')
                break
            if press_and_release('5'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('û')
                break
            if press_and_release('7'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ǔ')
                break
            if press_and_release('-'):
                while True:
                    sleep(relay)
                    if press_and_release('0'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ')
                        b[0]=1
                        break
                    if press_and_release('1'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ̀')
                        b[0]=1
                        break
                    if press_and_release('2'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ́')
                        b[0]=1
                        break
                    if press_and_release('3'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ̄')
                        b[0]=1
                        break
                    if press_and_release('5'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ̂')
                        b[0]=1
                        break
                    if press_and_release('7'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ̌')
                        b[0]=1
                        break
                    if press_and_release('backspace'):
                        break
                    if breaker(['0','1','2','3','5','7']):break
                    if press_and_release('space'):
                        break
            if press_and_release('u'):
                while True:
                    sleep(relay)
                    if press_and_release('0'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ')
                        b[0]=1
                        break
                    if press_and_release('1'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ̀')
                        b[0]=1
                        break
                    if press_and_release('2'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ́')
                        b[0]=1
                        break
                    if press_and_release('3'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ̄')
                        b[0]=1
                        break
                    if press_and_release('5'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ̂')
                        b[0]=1
                        break
                    if press_and_release('7'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ʉ̌')
                        b[0]=1
                        break
                    if press_and_release('backspace'):
                        break
                    if breaker(['0','1','2','3','5','7']):break
                    if press_and_release('space'):
                        break
            if press_and_release('backspace'):
                break
            if breaker(['0','1','2','3','5','7']):break
            if press_and_release('space'):
                break
            if b[0] is 1:
                b[0]=0
                break

    if press_and_release(sp_char):#<sp_char> <sp_char> <sp_char> <sp_char> <sp_char> <sp_char> <sp_char>
        while True:
            sleep(relay)
            if press_and_release('b'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ɓ')
                b[0]=1
                break
            if press_and_release('d'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ɗ')
                b[0]=1
                break
            if press_and_release('g'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ɠ')
                b[0]=1
                break
            if press_and_release('v'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ɣ')
                b[0]=1
                break
            if press_and_release('h'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ɦ')
                b[0]=1
                break
            if press_and_release('w'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ɯ')
                b[0]=1
                break
            if press_and_release('f'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ʃ')
                b[0]=1
                break
            if press_and_release('b'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ɓ')
                b[0]=1
                break
            if press_and_release('y'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ƴ')
                b[0]=1
                break
            if press_and_release('z'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ʒ')
                b[0]=1
                break
            if press_and_release('p'):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('ʔ')
                b[0]=1
                break
            if press_and_release("'"):
                sleep(relay)
                keyboard.send('backspace,backspace')
                print('5/5')
                keyboard.write('’')
                b[0]=1
                break
            if press_and_release('n'):
                while True:
                    sleep(relay)
                    if press_and_release('0'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɲ')
                        b[0]=1
                        break
                    if press_and_release('1'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɲ̀')
                        b[0]=1
                        break
                    if press_and_release('2'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɲ́')
                        b[0]=1
                        break
                    if press_and_release('3'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɲ̄')
                        b[0]=1
                        break
                    if press_and_release('5'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɲ̂')
                        b[0]=1
                        break
                    if press_and_release('7'):
                        sleep(relay)
                        keyboard.send('backspace,backspace,backspace')
                        print('5/5')
                        keyboard.write('ɲ̌')
                        break
                    if press_and_release(sp_char):
                        while True:
                            sleep(relay)
                            if press_and_release('0'):
                                sleep(relay)
                                keyboard.send('backspace,backspace,backspace,backspace')
                                print('5/5')
                                keyboard.write('ŋ')
                                b[0]=1
                                break
                            if press_and_release('1'):
                                sleep(relay)
                                keyboard.send('backspace,backspace,backspace,backspace')
                                print('5/5')
                                keyboard.write('ŋ̀')
                                b[0]=1
                                break
                            if press_and_release('2'):
                                sleep(relay)
                                keyboard.send('backspace,backspace,backspace,backspace')
                                print('5/5')
                                keyboard.write('ŋ́')
                                b[0]=1
                                break
                            if press_and_release('3'):
                                sleep(relay)
                                keyboard.send('backspace,backspace,backspace,backspace')
                                print('5/5')
                                keyboard.write('ŋ̄')
                                b[0]=1
                                break
                            if press_and_release('5'):
                                sleep(relay)
                                keyboard.send('backspace,backspace,backspace,backspace')
                                print('5/5')
                                keyboard.write('ŋ̂')
                                b[0]=1
                                break
                            if press_and_release('7'):
                                sleep(relay)
                                keyboard.send('backspace,backspace,backspace,backspace')
                                print('5/5')
                                keyboard.write('ŋ̌')
                                b[0]=1
                                break
                            if press_and_release('backspace'):
                                break
                            if breaker(['0','1','2','3','5','7']):break
                            if press_and_release('space'):
                                break
                    if press_and_release('backspace'):
                        break
                    if breaker(['0','1','2','3','5','7','b','d','g','v','h','w','f','y','a','z','p',"'"]):break
                    if press_and_release('space'):
                        break
            if press_and_release('backspace'):
                break
            if breaker(['n']):break
            if press_and_release('space'):
                break
            if b[0] is 1:
                b[0]=0
                break   
while True:
    sleep(relay)
    try:
        translate()
    except KeyboardInterrupt:
        sys.exit('STOP')
    except Exception as error:
        print('Fatal Error')
        print(error)

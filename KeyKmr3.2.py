# -*- coding: UTF-8 -*-
####################################
#KeyKmr by Fomegne Meudje          #
#Email: fomegnemeudje@outlook.com  #
####################################

import keyboard
import time
import sys

char = ['ɑ̀ɑ̀','ɑ́ɑ́','ɑ̄ɑ̄','ç','ç','Ç','Ç','a᷅','a᷇','a᷄','ɑ᷅','ɑ᷇','ɑ᷄','ɛ᷅','ɛ᷇','ɛ᷄','e᷅','e᷇','e᷄','ə᷅','ə᷇','ə᷄','i᷅','i᷇','i᷄','ɔ᷅','ɔ᷇','ɔ᷄','o᷅','o᷇','o᷄','u᷅','u᷇','u᷄','ʉ᷅','ʉ᷇','ʉ᷄','àà','áá','āā','ɑ̀ɑ̀','ɑ́ɑ́','ɑ̄ɑ̄','èè','éé','ēē','ə̀ə̀','ə́ə́','ə̄ə̄','ɛ̀ɛ̀','έέ','ɛ̄ɛ̄','ìì','íí','īī','òò','óó','ōō','ɔ̀ɔ̀','ɔ́ɔ́','ɔ̄ɔ̄','ʉ̀ʉ̀','ʉ́ʉ́','ʉ̄ʉ̄','ùù','úú','ūū','ʉ̀ʉ̀','ʉ́ʉ́','ʉ̄ʉ̄','ʉ̀ɑ̀','ʉ́ɑ́','ʉ̄ɑ̄','ʉ̀ɑ̀','ʉ́ɑ́','ʉ̄ɑ̄','ɛ̀ɛ̀','ɔ̂','ɔ̌','ɔ̌','ɔ̂','ɑ̀ɑ̀','ɑ̌','ʉɑ̂','ʉɑ̌','ʉɑ','ìɑ̀','íɑ́','īɑ̄','ùɑ̀','úɑ́','ūɑ̄','ɑ̂','ɑ̌','ə̌','ə̌','ə̂','ɛ̌','ɛ̌','ɛ̂','ǒǒ','ôô','ʉ̌','ʉ̌','ʉ̂','ɑ̂','ə̂','ɛ̂','ʉ̂','ɑ̀ɑ̀','ɑ̀ɑ̀','ùɑ̀','ìɑ̀','ɑ́ɑ́','ɑ́ɑ́','úɑ́','íɑ́','iɑ̂','iɑ̌','ūɑ̄','īɑ̄','ǒǒ','ôô','ɑ̈','ɛ̈','ə̈','ɔ̈','ʉ̈','ɨ̌','ɑ̠̀','ὲ̠','ə̠̀','ɔ̠̀','ʉ̠̀','ɨ̂','ɑ̠́','έ̠','ìì','ɛ̀','ìì','ɔ́','ɔ̄','ɔ̀','ʉ̀','ə̀','ə́','έ','ʉ́','ə̄','ʉ̄','ǎ','ǎ','iɑ','ě','ǐ','ǐ','òò','óó','ōō','ô','ǒ','ǔ','ǔ','â','â','ê','ê','èè','î','î','û','û','àà','ùà','ìà','àà','ɑɑ','èè','ìè','ìì','ìà','ìè','ùà','ɑ̀','áá','áá','éé','éé','ě','íí','íí','íá','íé','íé','óó','úá','íá','úá','ɑ́','āā','ēē','īī','ɛ̄','īī','īā','īē','ēē','īē','ōō','ūā','īā','āā','ūā','ɑ̄','ǒ','òò','ô','ɔ̌','ɔ̂','ɑ̌','ɑ̂','ɑ̌','ə̌','ə̌','ə̂','ɛ̌','ɛ̌','ɛ̂','ǒǒ','ôô','ʉ̌','ʉ̌','ʉ̂','ɑ̂','ə̂','ɛ̂','ʉ̂','ǒǒ','ôô','ä','b̈','c̈','d̈','ë','f̈','g̈','ḧ','ï','j̈','k̈','l̈','m̈','n̈','ö','p̈','q̈','r̈','s̈','ẗ','ü','v̈','ẅ','ẍ','ÿ','z̈','ɑ̇','ε̇','ə̇','ɔ̇','ʉ̇','č','m̌','ň','š','à̠','è̠','ɨ̀','ì̠','ò̠','ù̠','ĉ','m̂','n̂','ŝ','á̠','ù','ú','ɔ','ɔ','ì','ū','à','è','ŋ̀','ŋ́','ŋ̄','ŋ̌','ŋ̂','ŋ̀','ŋ́','ŋ̄','ŋ̌','ŋ̂','ŋ','í','é','á','ī','ē','ā','ò','ó','ō','ǎ','ǎ','ě','ǐ','ǐ','ô','ǒ','ǔ','ǔ','â','â','ê','ê','î','î','û','û','ě','ǒ','ô','ʔ','ȧ','ḃ','ċ','ḋ','ė','ḟ','ġ','ḣ','i̇','j̇','k̇','l̇','ṁ','ṅ','ȯ','ṗ','q̇','ṙ','ṡ','ṫ','u̇','v̇','ẇ','ẋ','ẏ','ż','ʔ','c̀','h̀','m̀','ǹ','s̀','ʉ̀','ʉ́','ʉ̄','ɑ','ə','ε','ʉ','ʉ̂','ʉ̌','ʉ','ʉ','ǹ','ń','n̄','ň','n̂','m̀','ḿ','m̄','m̌','m̂','Ǹ','Ń','N̄','Ň','N̂','Ŋ̀','Ŋ́','Ŋ̄','Ŋ̌','Ŋ̂','Ŋ','M̀','Ḿ','M̄','M̌','M̂','À','Á','Ā','Ǎ','Â','È','É','Ē','Ě','Ê','Ò','Ó','Ō','Ǒ','Ô','Ɔ̀','Ɔ́','Ɔ̄','Ɔ̌','Ɔ̂','Ɔ','Ǎ','Â','Ǒ','Ô','ē̠','ē̠','ē̠','e̠','ʉ̂','ʉ̌','ɲ','ɓ','Ɓ','ɗ','Ɗ','Ɲ']
code = ['aff1','aff2','aff3','c_','c_ced','C_','C_ced','a13','a23','a32','af13','af23','af32','ai13','ai23','ai32','e13','e23','e32','eu13','eu23','eu32','i13','i23','i32','o*13','o*23','o*32','o13','o23','o32','u13','u23','u32','uu13','uu23','uu32','a11','a22','a33','af11','af22','af33','e11','e22','e33','eu11','eu22','eu33','ai11','ai22','ai33','i11','i22','i33','o11','o22','o33','o*11','o*22','o*33','uu11','uu22','uu33','u11','u22','u33','u-11','u-22','u-33','1uuaf','2uuaf','3uuaf','uuaf1','uuaf2','uuaf3','ai11','o*21','o*12','12o*','21o*','af11','af12','uuaf5','uuaf7','uuaf','1iaf','2iaf','3iaf','1uaf','2uaf','3uaf','21af','12af','eu12','12eu','21eu','ai12','12ai','21ai','12oo','21oo','uu12','12uu','21uu','af21','eu21','ai21','uu21','aff1','1aff','uaf1','iaf1','aff2','2aff','uaf2','iaf2','iaf5','iaf7','uaf3','iaf3','oo12','oo21','..af','..ai','..eu','..o*','..uu','12i-','1af_','1ai_','1eu_','1o*_','1uu_','21i-','2af_','2ai_','i11','ai1','ii1','o*2','o*3','o*1','uu1','eu1','eu2','ai2','uu2','eu3','uu3','a12','12a','iaf','e12','i12','12i','1oo','2oo','3oo','21o','12o','u12','12u','a21','21a','e21','21e','1ee','i21','21i','21u','u21','aa1','ua1','ia1','1aa','aff','ee1','ie1','1ii','1ia','1ie','1ua','af1','aa2','2aa','ee2','2ee','12e','ii2','2ii','2ia','ie2','2ie','oo2','ua2','ia2','2ua','af2','3aa','3ee','ii3','ai3','3ii','3ia','ie3','ee3','3ie','oo3','ua3','ia3','aa3','3ua','af3','o12','oo1','o21','o*7','o*5','af7','5af','7af','eu7','7eu','5eu','ai7','7ai','5ai','7oo','5oo','uu7','7uu','5uu','af5','eu5','ai5','uu5','oo7','oo5','..a','..b','..c','..d','..e','..f','..g','..h','..i','..j','..k','..l','..m','..n','..o','..p','..q','..r','..s','..t','..u','..v','..w','..x','..y','..z','.af','.ai','.eu','.o*','.uu','12c','12m','12n','12s','1a_','1e_','1i-','1i_','1o_','1u_','21c','21m','21n','21s','2a_','u1','u2','o*','o*','i1','u3','a1','e1','nn1','nn2','nn3','nn7','nn5','n*1','n*2','n*3','n*7','n*5','n*','i2','e2','a2','i3','e3','a3','o1','o2','o3','a7','7a','e7','i7','7i','5o','7o','7u','u7','a5','5a','e5','5e','i5','5i','5u','u5','7e','o7','o5','.?','.a','.b','.c','.d','.e','.f','.g','.h','.i','.j','.k','.l','.m','.n','.o','.p','.q','.r','.s','.t','.u','.v','.w','.x','.y','.z','?.','1c','1h','1m','1n','1s','u-1','u-2','u-3','af','eu','ai','uu','u-5','u-7','u-','u-','n1','n2','n3','n7','n5','m1','m2','m3','m7','m5','N1','N2','N3','N7','N5','N*1','N*2','N*3','N*7','N*5','N*','M1','M2','M3','M7','M5','A1','A2','A3','A7','A5','E1','E2','E3','E7','E5','O1','O2','O3','O7','O5','O*1','O*2','O*3','O*7','O*5','O*','A12','A21','O12','O21','e3_','3e_','e_3','e_','u-5','u-7','*n','b*','B*','d*','D*','*N']
text = ''

def transform(text):
    t = False
    for i in range(len(char)):
        if code[i] in text:
            t = True
            text=text.replace(code[i].lower(),char[i].lower())
    return [text,t]

def key(x):
    global text
    if x == 'space' or x == 'enter':
        text = text.replace(' ','')
        text = correction(text)
        result = transform(text)
        if result[1]:
            keyboard.send(backspace(text))
            keyboard.write(result[0])
        if x == 'enter':
            keyboard.send('enter')
        text = ''
    else:
        text = text + x

def correction(text):
    text = text.replace(' ','')
    text = text + ' '
    return text

def backspace(text):
    back = (len(text) * ',backspace')
    back = back[1::]
    return back

def press_and_release(Key):
    if keyboard.is_pressed(Key):
        while keyboard.is_pressed(Key):
            time.sleep(0.001)
            pass
        return True
    else:
        return False
    
def keyboard_input():
    time.sleep(0.001)
    if press_and_release('a'):
        print('a')
        key('a')

    elif press_and_release('b'):
        print('b')
        key('b')

    elif press_and_release('c'):
        print('c')
        key('c')

    elif press_and_release('d'):
        print('d')
        key('d')

    elif press_and_release('e'):
        print('e')
        key('e')

    elif press_and_release('f'):
        print('f')
        key('f')

    elif press_and_release('g'):
        print('g')
        key('g')

    elif press_and_release('h'):
        print('h')
        key('h')

    elif press_and_release('i'):
        print('i')
        key('i')

    elif press_and_release('j'):
        print('j')
        key('j')

    elif press_and_release('k'):
        print('k')
        key('k')

    elif press_and_release('l'):
        print('l')
        key('l')

    elif press_and_release('m'):
        print('m')
        key('m')

    elif press_and_release('n'):
        print('n')
        key('n')

    elif press_and_release('o'):
        print('o')
        key('o')

    elif press_and_release('p'):
        print('p')
        key('p')

    elif press_and_release('q'):
        print('q')
        key('q')

    elif press_and_release('r'):
        print('r')
        key('r')

    elif press_and_release('s'):
        print('s')
        key('s')

    elif press_and_release('t'):
        print('t')
        key('t')

    elif press_and_release('u'):
        print('u')
        key('u')

    elif press_and_release('v'):
        print('v')
        key('v')

    elif press_and_release('w'):
        print('w')
        key('w')

    elif press_and_release('x'):
        print('x')
        key('x')

    elif press_and_release('y'):
        print('y')
        key('y')

    elif press_and_release('z'):
        print('z')
        key('z')

    elif press_and_release('1'):
        print('1')
        key('1')

    elif press_and_release('2'):
        print('2')
        key('2')

    elif press_and_release('3'):
        print('3')
        key('3')

    elif press_and_release('4'):
        print('4')
        key('4')

    elif press_and_release('5'):
        print('5')
        key('5')

    elif press_and_release('6'):
        print('6')
        key('6')

    elif press_and_release('7'):
        print('7')
        key('7')

    elif press_and_release('8'):
        print('8')
        key('8')

    elif press_and_release('9'):
        print('9')
        key('9')

    elif press_and_release('0'):
        print('0')
        key('0')

    elif press_and_release('*'):
        print('*')
        key('*')

    elif press_and_release('_'):
        print('_')
        key('_')
        
    elif press_and_release('space'):
        print('space')
        key('space')

    elif press_and_release('enter'):
        print('enter')
        key('enter')
        
    else:
        pass

while 1:
    try:
        keyboard_input()
    except KeyboardInterrupt:
        sys.exit('STOP')
    except:
        print('Fatal Error')

import os
import tkinter
from tkinter import *
from tkinter import messagebox
from gtts import gTTS
import pyttsx3
import urllib.request
from langdetect import detect
from playsound import playsound

text_VN = 'Chúc bạn một ngày tốt lành'
file_vn = "outputvn.mp3"
url_test = 'http://google.com'
student_inf = 'Họ và tên sinh viên : Lê Hoàng Anh, Mssv : N19DCCN005, Lớp : D19CQCN02-N'
Voice = {'vn': 'none', 'vn_name': 'none', 'en1': 'none', 'en1_name': 'none', 'en2': 'none', 'en2_name': 'none'}
Error_inf = {
    'No_lang': 'Máy Vui Lòng Cài Gói Ngôn Ngữ Tiếng Việt (Nếu Windown Vui Lòng Cài Thêm File VoiceVI.reg Đi Kèm)',
    'vn_gg': 'Máy Tính Vui Lòng Kết Nối Internet',
    'empty_text': 'Vui lòng nhập văn bản'}


def connect_internet():
    try:
        urllib.request.urlopen(url_test)
        return True
    except:
        return False


def speech_gg_vn():
    if not connect_internet():
        messagebox.showinfo('Thông Báo', Error_inf['vn_gg'])
    else:
        TTS = gTTS(boxtxt.get(), lang='vi')
        TTS.save(file_vn)
        playsound(file_vn)
        os.remove(file_vn)


def set_voice(voice_inf):
    for voice in voice_inf:
        '''
        print('Voice :')
        print('- ID : ', voice.id)
        print('- Name : ', voice.name)
        '''
        s = voice.name.lower()
        if (s.find('vietnam') != -1) and (Voice['vn'] == 'none'):
            Voice['vn'] = voice.id
            Voice['vn_name'] = voice.name
        elif (s.find('english') != -1) and (Voice['en1'] == 'none'):
            Voice['en1'] = voice.id
            Voice['en1_name'] = voice.name
        elif (s.find('english') != -1) and (Voice['en2'] == 'none'):
            Voice['en2'] = voice.id
            Voice['en2_name'] = voice.name
        elif (Voice['vn'] != 'none') and (Voice['en1'] != 'none') and (Voice['en2'] != 'none'):
            break


def play_speech():
    speechText.setProperty('rate', 125)
    speechText.runAndWait()


def speech_vn():
    if Voice['vn'] == 'none':
        messagebox.showinfo('Thông Báo', Error_inf['No_lang'])
    else:
        speechText.setProperty('voice', Voice['vn'])
        speechText.say(boxtxt.get())
        play_speech()


def speech_en1():
    if Voice['en1'] == 'none':
        messagebox.showinfo('Thông Báo', Error_inf['No_lang'])
    else:
        speechText.setProperty('voice', Voice['en1'])
        speechText.say(boxtxt.get())
        play_speech()


def speech_en2():
    if Voice['en2'] == 'none':
        messagebox.showinfo('Thông Báo', Error_inf['No_lang'])
    else:
        speechText.setProperty('voice', Voice['en2'])
        speechText.say(boxtxt.get())
        play_speech()


def box_clear(e):
    if boxtxt.get() == text_VN:
        boxtxt.delete(0, END)


def create_new_wd():
    if boxtxt.get() != '':
        new_wd = tkinter.Toplevel(wd)
        new_wd.title('Chọn Giọng')
        new_wd.geometry('500x200')
        if detect(boxtxt.get()) == 'vi':
            lb_Vi = Label(new_wd, text='Tiếng Việt', font=('Arial', 20))
            lb_voice_vn = Label(new_wd, text='Giọng Đọc: ' + Voice['vn_name'])
            butt_Win_Vi = Button(new_wd, text='Phát câu tiếng Việt', command=speech_vn)
            lb_voice_vn_gg = Label(new_wd, text='Giọng Đọc: Chị Google')
            butt_GG_Vi = Button(new_wd, text='Phát câu tiếng Việt qua API Google', command=speech_gg_vn)

            lb_Vi.pack()
            lb_voice_vn.pack()
            butt_Win_Vi.pack()
            lb_voice_vn_gg.pack()
            butt_GG_Vi.pack()

        else:
            lb_En = Label(new_wd, text='Tiếng Anh', font=('Arial', 20))
            lb_voice_en1 = Label(new_wd, text='Giọng Đọc: ' + Voice['en1_name'])
            butt_M_En = Button(new_wd, text='Phát câu tiếng Anh (Giọng 1)', command=speech_en1)
            lb_voice_en2 = Label(new_wd, text='Giọng Đọc: ' + Voice['en2_name'])
            butt_F_En = Button(new_wd, text='Phát câu tiếng Anh (Giọng 2)', command=speech_en2)

            lb_En.pack()
            lb_voice_en1.pack()
            butt_M_En.pack()
            lb_voice_en2.pack()
            butt_F_En.pack()
    else:
        messagebox.showinfo('Thông Báo', Error_inf['empty_text'])


if __name__ == "__main__":
    speechText = pyttsx3.init()
    set_voice(speechText.getProperty('voices'))

    wd = Tk()
    wd.title('Phát Giọng Nói')
    wd.geometry('1100x400')

    lb_man = Label(wd, text='Văn Bản', font=('Arial', 25))
    lb_inf = Label(wd, text=student_inf, font=('Arial', 18), fg='red')
    lb_sj = Label(wd, text='Môn: Hệ Điều Hành - Đề tài 2', font=('Arial', 18), fg='red')
    lb_sp = Label(wd, text='')

    boxtxt = Entry(wd, width=80, font=('Arial', 18))
    boxtxt.insert(0, text_VN)

    butt_check = Button(wd, text='CHẠY', font=('Arial', 18), command=create_new_wd)

    lb_inf.pack()
    lb_sj.pack(ipady=5)
    lb_man.pack(ipady=20)
    boxtxt.pack(ipadx=2, ipady=4)
    lb_sp.pack(ipady=10)
    butt_check.pack()
    boxtxt.bind("<Button-1>", box_clear)

    wd.mainloop()

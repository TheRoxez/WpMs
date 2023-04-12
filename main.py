import tkinter as tk
import webbrowser
import time
import pyautogui


def send_whatsapp_message():
    url = 'https://web.whatsapp.com/'
    #isim girdisi
    name = name_entry.get()
    #mesaj girdisi
    message = message_entry.get()
    #mesaj adet girdisi
    sayi=int(adet.get())
    
    #web uygulamasına gidilmesi ve 12 saniye beklemesi
    webbrowser.open(url, new=0)
    time.sleep(12)
    #internet hızınıza göre bu 12 yi değiştirebilirsiniz

    #Arama textbox konumu
    search_position = [300, 210]
    #Kişi seçme konumu
    select_position = [350, 350]
    #mesaj textbox konumu
    message_position = [815, 1030]
    
    #girdileri ve değişkenleri olaylara atıyoruz
    pyautogui.click(x=search_position[0], y=search_position[1])
    pyautogui.hotkey('CTRL', 'a')
    pyautogui.typewrite(name)
    time.sleep(2)
    pyautogui.click(x=select_position[0], y=select_position[1])
    time.sleep(2)
    pyautogui.click(x=message_position[0], y=message_position[1])
    i = 0

    while i < sayi:
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        i = i + 1


# Arayüz oluşturma
window = tk.Tk()
window.title("WhatsApp Otomatik Mesaj Gönderici")
window.geometry("400x300")

# Kişi Seçimi
name_label = tk.Label(text="Kişi:")
name_label.pack()
name_entry = tk.Entry(width=40)
name_entry.pack()

# Mesaj Girişi
message_label = tk.Label(text="Mesaj:")
message_label.pack()
message_entry = tk.Entry(width=40)
message_entry.pack()

# Mesaj sayısı
adetl = tk.Label(text="Adet:")
adetl.pack()
adet = tk.Entry(width=40)
adet.pack()

# Gönderme Butonu
send_button = tk.Button(text="Gönder", command=send_whatsapp_message)
send_button.pack()

window.mainloop()

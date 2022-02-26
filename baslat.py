import time, sys, os, colorama
import shutup; shutup.please()
from colorama import Fore
from selenium import webdriver

def type(str, wait):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(wait)
  print()

os.system("title TikTok Izleme Botu By @osmancitci")
indentLines = int(round(os.get_terminal_size().lines/2))
print("\n" * indentLines)
print(f"""
{Fore.LIGHTMAGENTA_EX}     
{" "*round(os.get_terminal_size().columns/2-35)}__   __ _   _  _     _               _                              
{" "*round(os.get_terminal_size().columns/2-35)}\ \ / /(_) (_)| |   | |             (_)                             
{" "*round(os.get_terminal_size().columns/2-35)} \ V /  _   _ | | __| |  ___  _ __   _  _   _   ___   _ __          
{" "*round(os.get_terminal_size().columns/2-35)}  \ /  | | | || |/ /| | / _ \| '_ \ | || | | | / _ \ | '__|         
{" "*round(os.get_terminal_size().columns/2-35)}  | |  | |_| ||   < | ||  __/| | | || || |_| || (_) || |    _  _  _
{" "*round(os.get_terminal_size().columns/2-35)}  \_/   \__,_||_|\_\|_| \___||_| |_||_| \__, | \___/ |_|   (_)(_)(_)
{" "*round(os.get_terminal_size().columns/2-35)}                                         __/ |                      
{" "*round(os.get_terminal_size().columns/2-35)}                                        |___/                       \n\n
""")

print(f"{' ' * round(os.get_terminal_size().columns/2-21)}\t{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}]{Fore.LIGHTGREEN_EX} İPUCU: {Fore.LIGHTMAGENTA_EX}Yüklenmiyor mu? Enter tuşuna basın.")
print("\n" * indentLines)

def yazTiktokBot():
    buyukYazi1 = f"""
{Fore.LIGHTMAGENTA_EX}
{" "*round(os.get_terminal_size().columns/2-38)}████████ ██ ██   ██ ████████  ██████  ██   ██     ██████   ██████  ████████
{" "*round(os.get_terminal_size().columns/2-38)}   ██    ██ ██  ██     ██    ██    ██ ██  ██      ██   ██ ██    ██    ██    
{" "*round(os.get_terminal_size().columns/2-38)}   ██    ██ █████      ██    ██    ██ █████       ██████  ██    ██    ██    
{" "*round(os.get_terminal_size().columns/2-38)}   ██    ██ ██  ██     ██    ██    ██ ██  ██      ██   ██ ██    ██    ██    
{" "*round(os.get_terminal_size().columns/2-38)}   ██    ██ ██   ██    ██     ██████  ██   ██     ██████   ██████     ██    
"""
    buyukYazi2 = buyukYazi1.replace('▪', f'{Fore.GREEN}▪{Fore.LIGHTMAGENTA_EX}')
    buyukYazi3 = buyukYazi2.replace('•', f'{Fore.GREEN}•{Fore.LIGHTMAGENTA_EX}')
    buyukYazi4 = buyukYazi3.replace('·', f'{Fore.GREEN}·{Fore.LIGHTMAGENTA_EX}')
    buyukYazi5 = buyukYazi4.replace('.', f'{Fore.GREEN}.{Fore.LIGHTMAGENTA_EX}')
    print(buyukYazi5)

def yazAyarlar():
    ayarlar = f"""
    {Fore.WHITE}
{" "*round(os.get_terminal_size().columns/2-16)}╔═══════════════════════════════╗
{" "*round(os.get_terminal_size().columns/2-16)}║                               ║
{" "*round(os.get_terminal_size().columns/2-16)}║        {Fore.WHITE}[{Fore.LIGHTGREEN_EX}1{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Başla{Fore.WHITE}              ║
{" "*round(os.get_terminal_size().columns/2-16)}║        {Fore.WHITE}[{Fore.LIGHTGREEN_EX}2{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Bilgi{Fore.WHITE}              ║
{" "*round(os.get_terminal_size().columns/2-16)}║        {Fore.WHITE}[{Fore.LIGHTGREEN_EX}3{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Ayarlar{Fore.WHITE}            ║
{" "*round(os.get_terminal_size().columns/2-16)}║        {Fore.WHITE}[{Fore.LIGHTGREEN_EX}4{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Temizle/Yenile{Fore.WHITE}     ║
{" "*round(os.get_terminal_size().columns/2-16)}║        {Fore.WHITE}[{Fore.LIGHTGREEN_EX}5{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Çıkış{Fore.WHITE}              ║
{" "*round(os.get_terminal_size().columns/2-16)}║                               ║
{" "*round(os.get_terminal_size().columns/2-16)}╚═══════════════════════════════╝
    """
    print(ayarlar)

def yazBilgi():
    bilgi = f"""
{Fore.WHITE}
{" "*round(os.get_terminal_size().columns/2-42)}╔═══════════════════════════════════════════════════════════════════════════════════╗
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                                   ║
{" "*round(os.get_terminal_size().columns/2-42)}║        {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Hakkında: {Fore.LIGHTMAGENTA_EX}Tiktok'ta Takipçi, Kalp, İzlenme ve Paylaşım Botudur.{Fore.WHITE}        ║
{" "*round(os.get_terminal_size().columns/2-42)}║        {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Yapımcı: {Fore.LIGHTMAGENTA_EX}OsmanCitci{Fore.WHITE}                                                    ║
{" "*round(os.get_terminal_size().columns/2-42)}║        {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTMAGENTA_EX}https://github.com/osmancitci{Fore.WHITE}                                  ║
{" "*round(os.get_terminal_size().columns/2-42)}║        {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Chrome Driver Yükle: {Fore.LIGHTMAGENTA_EX}https://chromedriver.chromium.org/downloads{Fore.WHITE}       ║
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                                   ║
{" "*round(os.get_terminal_size().columns/2-42)}╚═══════════════════════════════════════════════════════════════════════════════════╝
"""
    print(bilgi)

def temizle():
    os.system("cls")

    yazTiktokBot()

    print(f'{" "*round(os.get_terminal_size().columns/2-14)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Yapımcı: {Fore.LIGHTMAGENTA_EX}OsmanCitci {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]\n{" "*round(os.get_terminal_size().columns/2-30)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTMAGENTA_EX}https://github.com/OsmanCitci/TiktokIzleyici {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]')

    yazAyarlar()

def basla():
    type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Not: {Fore.LIGHTGREEN_EX}Lütfen Gerçek Bir TikTok Bağlantısı Olduğundan Emin Olun, Değilse Daha Sonra Hatalara Neden Olabilir.", wait = 0.01)
    video_url = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Video URL: {Fore.LIGHTMAGENTA_EX}")

    while "tiktok" not in video_url:
        type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Lütfen Geçerli Bir Bağlantı Girin.", 0.01)
        video_url = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Video URL: {Fore.LIGHTMAGENTA_EX}")
        if "tiktok" in video_url:
            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Chrome Web Sürücüsü açılıyor...\n", 0.01)
            break

    anasayfa(video_url)


def anasayfa(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as DriverError:
        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Chrome Sürücüsü İçin Geçersiz Dosya Konumu veya Dosya Konumu Henüz Ayarlanmadı. Çift Eğik Çizgi Kullanmayı Unutmayın. Veya Chrome Sürücü Sürümü Chrome ile Aynı Değil. (Dosya Konumundan Önce Örnek Chrome Sürücü Yolu Metnini Sildiğinizden Emin Olun)\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Satır: 102\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Durdurulan Program.\n", 0.01)
        print(f"{DriverError}{Fore.RESET}\n")
        time.sleep(7)
        exit()
    driver.set_window_size(777, 777)
    driver.get('https://zefoy.com')
    amount = 0

    if driver.title == "502 Sunucu Hatası":
                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}\nSunucuda Hata Var.. Düzeltmeye Çalışıyor.\n")
                while driver.title == "502 Sunucu Hatası":
                    time.sleep(20)
                    driver.refresh()
                    if driver.title != "502 Sunucu Hatası":
                        type(f"{Fore.LIGHTGREEN_EX}\nSorun Düzeltildi. Yeniden Başlıyor.\n", 0.01)
                        break
    else:
        pass
        type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Bot Aktif!{Fore.WHITE}\n", 0.01)


    type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Doğrulamayı Yaptığınız'da \"e\" Tuşuna Basın..", 0.01)
    dogrulama_bitis = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.GREEN}{Fore.LIGHTMAGENTA_EX}")
    if dogrulama_bitis == "e":
        while dogrulama_bitis != True:
            try:
                driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/h5")
                dogrulama_bitis = True
            except:
                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Doğrumayı Bitirmedin.", 0.01)
                dogrulama_bitis = False
                type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Doğrulamayı Yaptığınız'da \"e\" Tuşuna Basın..", 0.01)
                dogrulama_bitis = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.GREEN}{Fore.LIGHTMAGENTA_EX}")
                if dogrulama_bitis == True:
                    break
    
    while dogrulama_bitis == True:
        type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Doğrulama Başarılı, Bot Başlıyor.", 0.01)

        takipler_bekleme = 0
        kalpler_bekleme = 0
        izlenmeler_bekleme = 0
        paylasimlar_bekleme = 0
        Takip_Saniye = 0
        Takip_Dakika = 0
        Kalp_Saniye = 0
        Kalp_Dakika = 0
        Izlenme_Dakika = 0
        Izlenme_Saniye = 0
        Paylasim_Dakika = 0
        Paylasim_Saniye = 0
        Takip_Devam1 = False
        Takip_Devam2 = False
        Kalp_Devam1 = False
        Kalp_Devam2 = False
        Izlenme_Devam1 = False
        Izlenme_Devam2 = False
        Paylasim_Devam1 = False
        Paylasim_Devam2 = False

        while dogrulama_bitis == True:
            if driver.title == "502 Sunucu Hatası":
                type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}]{Fore.LIGHTRED_EX}\nSunucuda Hata Var.. Düzeltmeye Çalışıyor.\n", 0.01)
                while driver.title == "502 Sunucu Hatası":
                    time.sleep(20)
                    driver.refresh()
                    if driver.title != "502 Sunucu Hatası":
                        type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX} Sorun Düzeltildi. Yeniden Başlıyor.\n", 0.01)
                        break
            else:
                type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Bot Aktif.{Fore.WHITE}\n", 0.01)
                pass
            
            try:
                try:
                    
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    takipler_bekleme = 0

                    try:
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid"]/div/form/div/input').send_keys(url)
                        Takip_Devam1 = True
                    except:
                        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Takipçi Gönderme Sayfası Kapalı.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Geçiyor...{Fore.WHITE}\n", 0.01)
                        Takip_Devam1 = False
                        Takip_Saniye = 0
                        Takip_Dakika = 0
                        takipler_bekleme = 0

                    if Takip_Devam1 == True:
                        driver.find_element_by_xpath('//*[@id="sid"]/div/form/div/div/button').click()
                        time.sleep(3)
                        try:
                            driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
                            Takip_Devam2 = True
                        except:
                            type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Takip Daha Hazır Değil. Geçiliyor.\n {Fore.WHITE}", 0.01)
                            Takip_Devam2 = False
                            Takip_Yazi = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/h4").text
                            time.sleep(3)

                            if Takip_Yazi[13] == " ":
                                Takip_Dakika = int(Takip_Yazi[12])
                                Takip_Saniye = Takip_Dakika * 60

                            elif Takip_Yazi[13] != " ":
                                Takip_Dakika = int(Takip_Yazi[12:14])
                                Takip_Saniye = Takip_Dakika * 60

                            if Takip_Yazi[24] == "0":
                                Takip_Saniye += int(Takip_Yazi[25])
                            elif Takip_Yazi[24] != "0":
                                Takip_Saniye += int(Takip_Yazi[24:26])

                            Takip_Saniye += 5
                            takipler_bekleme += Takip_Saniye

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Takip Kalan Süre: {Fore.LIGHTCYAN_EX}{Takip_Dakika}{Fore.LIGHTMAGENTA_EX} Dakika ve {Fore.LIGHTCYAN_EX}{Takip_Saniye%60}{Fore.LIGHTMAGENTA_EX} Saniye.\n", 0.01)

                        if Takip_Devam2 == True:
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}\nTakipçi Gönderildi!\n{Fore.WHITE}\n", 0.01)
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Lütfen Bekleyin...{Fore.WHITE}\n", 0.01)
                            time.sleep(10)
                            Takip_Yazi = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/h4').text

                            try:
                                if Takip_Yazi[13] == " ":
                                    Takip_Dakika = int(Takip_Yazi[12])
                                    Takip_Saniye = Takip_Dakika * 60

                                elif Takip_Yazi[13] != " ":
                                    Takip_Dakika = int(Takip_Yazi[12:14])
                                    Takip_Saniye = Takip_Dakika * 60

                                if Takip_Yazi[24] == "0":
                                    Takip_Saniye += int(Takip_Yazi[25])
                                elif Takip_Yazi[24] != "0":
                                    Takip_Saniye += int(Takip_Yazi[24:26])

                                Takip_Saniye += 5
                                takipler_bekleme += Takip_Saniye
                            except:
                                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Takipte Bir Hata Oluştu. (Geçiliyor){Fore.WHITE}\n", 0.01)
                                Takip_Dakika = 0
                                Takip_Saniye = 0
                                takipler_bekleme = 0


                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Takip Kalan Süre:{Fore.LIGHTCYAN_EX}{Takip_Dakika}{Fore.LIGHTMAGENTA_EX} Dakika ve {Fore.LIGHTCYAN_EX}{Takip_Saniye%60}{Fore.LIGHTMAGENTA_EX} Saniye.{Fore.WHITE}\n", 0.01)

                        else:
                            pass
                    else:
                        pass

                except Exception as Takipler_Hata:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Takipçi Göndermeye Çalışırken Bir Hata Oluştu.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Hata: {Takipler_Hata}{Fore.WHITE}\n", 0.01)
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    Takip_Dakika = 0
                    Takip_Saniye = 0
                    takipler_bekleme = 0


                try:
                    
                    driver.refresh()
                    try:
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/input').send_keys(url)
                        Izlenme_Devam1 = True
                    except:
                        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}İzlenme Gönderme Sayfası Kapalı.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Skipping...{Fore.WHITE}\n", 0.01)
                        Izlenme_Devam1 = False
                        Izlenme_Saniye = 0
                        Izlenme_Dakika = 0
                        izlenmeler_bekleme = 0

                    if Izlenme_Devam1 == True:
                        driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/div/button').click()
                        time.sleep(2)

                        driver.refresh()
                        time.sleep(0.7)
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/input').send_keys(url)
                        driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/div/button').click()
                        time.sleep(3)
                        try:
                            driver.find_element_by_xpath('/html/body/div[4]/div[5]/div/div/div[1]/div/form/button').click()
                            Izlenme_Devam2 = True
                        except:
                            Izlenme_Devam2 = False
                            Izlenme_Yazi = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/h4").text
                            type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}İzlenme Daha Hazır Değil. Geçiliyor.\n {Fore.WHITE}", 0.01)
                            time.sleep(3)

                            if Izlenme_Yazi[13] == " ":
                                Izlenme_Dakika = int(Izlenme_Yazi[12])
                                Izlenme_Saniye = Izlenme_Dakika * 60

                            elif Izlenme_Yazi[13] != " ":
                                Izlenme_Dakika = int(Izlenme_Yazi[12:14])
                                Izlenme_Saniye = Izlenme_Dakika * 60

                            if Izlenme_Yazi[24] == "0":
                                Izlenme_Saniye += int(Izlenme_Yazi[25])
                            elif Izlenme_Yazi[24] != "0":
                                Izlenme_Saniye += int(Izlenme_Yazi[24:26])

                            Izlenme_Saniye += 5
                            izlenmeler_bekleme += Izlenme_Saniye

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}İzlenme Kalan Süre: {Fore.LIGHTCYAN_EX}{Izlenme_Dakika}{Fore.LIGHTMAGENTA_EX} Dakika ve {Fore.LIGHTCYAN_EX}{Izlenme_Saniye%60}{Fore.LIGHTMAGENTA_EX} Saniye.{Fore.WHITE}\n", 0.01)
                            driver.refresh()

                        if Izlenme_Devam2 == True:
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}İzlenme Gönderildi!\n{Fore.WHITE}", 0.01)
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Lütfen Bekleyin...{Fore.WHITE}\n", 0.01)
                            time.sleep(10)

                            Izlenme_Yazi = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/h4").text

                            try:
                                if Izlenme_Yazi[13] == " ":
                                    Izlenme_Dakika = int(Izlenme_Yazi[12])
                                    Izlenme_Saniye = Izlenme_Dakika * 60

                                elif Izlenme_Yazi[13] != " ":
                                    Izlenme_Dakika = int(Izlenme_Yazi[12:14])
                                    Izlenme_Saniye = Izlenme_Dakika * 60

                                if Izlenme_Yazi[24] == "0":
                                    Izlenme_Saniye += int(Izlenme_Yazi[25])
                                elif Izlenme_Yazi[24] != "0":
                                    Izlenme_Saniye += int(Izlenme_Yazi[24:26])

                                Izlenme_Saniye += 5
                                izlenmeler_bekleme += Izlenme_Saniye
                                
                            except:
                                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}İzlenmede Bir Hata Oluştu. (Geçiliyor){Fore.WHITE}\n", 0.01)
                                Izlenme_Dakika = 0
                                Izlenme_Saniye = 0
                                izlenmeler_bekleme = 0

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}İzlenme Kalan Süre: {Fore.LIGHTCYAN_EX}{Izlenme_Dakika}{Fore.LIGHTMAGENTA_EX} Dakika ve {Fore.LIGHTCYAN_EX}{Izlenme_Saniye%60}{Fore.LIGHTMAGENTA_EX} Saniye.{Fore.WHITE}\n", 0.01)

                        else:
                            pass

                    else:
                        pass
                        
                except Exception as Izlenmeler_Hata:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}İzlenme Göndermeye Çalışırken Bir Hata Oluştu.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Hata: {Izlenmeler_Hata}{Fore.WHITE}\n", 0.01)
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    Izlenme_Dakika = 0
                    Izlenme_Saniye = 0
                    izlenmeler_bekleme = 0
                

                try:
                    
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    kalpler_bekleme = 0

                    try:
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/input').send_keys(url)
                        Kalp_Devam1 = True
                    except:
                        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Kalp Gönderme Sayfası Kapalı.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Geçiliyor...{Fore.WHITE}\n", 0.01)
                        Kalp_Devam1 = False
                        Kalp_Saniye = 0
                        Kalp_Dakika = 0
                        kalpler_bekleme = 0

                    if Kalp_Devam1 == True:
                        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/div/button').click()
                        time.sleep(3)
                        try:
                            driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
                            Kalp_Devam2 = True

                        except:
                            type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Kalpler Daha Hazır Değil. Geçiliyor.\n {Fore.WHITE}", 0.01)
                            Kalp_Devam2 = False
                            Kalp_Yazi = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/h4").text
                            time.sleep(3)

                            if Kalp_Yazi[13] == " ":
                                Kalp_Dakika = int(Kalp_Yazi[12])
                                Kalp_Saniye = Kalp_Dakika * 60

                            elif Kalp_Yazi[13] != " ":
                                Kalp_Dakika = int(Kalp_Yazi[12:14])
                                Kalp_Saniye = Kalp_Dakika * 60

                            if Kalp_Yazi[24] == "0":
                                Kalp_Saniye += int(Kalp_Yazi[25])
                            elif Kalp_Yazi[24] != "0":
                                Kalp_Saniye += int(Kalp_Yazi[24:26])

                            Kalp_Saniye += 7
                            kalpler_bekleme += Kalp_Saniye

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Kalp Kalan Süre: {Fore.LIGHTCYAN_EX}{Kalp_Dakika}{Fore.LIGHTMAGENTA_EX} Dakika ve {Fore.LIGHTCYAN_EX}{Kalp_Saniye%60}{Fore.LIGHTMAGENTA_EX} Saniye.{Fore.WHITE}\n", 0.01)

                        if Kalp_Devam2 == True:
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Kalpler Gönderildi!\n{Fore.WHITE}", 0.01)
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Lütfen Bekleyin...{Fore.WHITE}\n", 0.01)
                            time.sleep(10)

                            Kalp_Yazi = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/h4").text

                            try:
                                if Kalp_Yazi[13] == " ":
                                    Kalp_Dakika = int(Kalp_Yazi[12])
                                    Kalp_Saniye = Kalp_Dakika * 60

                                elif Kalp_Yazi[13] != " ":
                                    Kalp_Dakika = int(Kalp_Yazi[12:14])
                                    Kalp_Saniye = Kalp_Dakika * 60

                                if Kalp_Yazi[24] == "0":
                                    Kalp_Saniye += int(Kalp_Yazi[25])
                                elif Kalp_Yazi[24] != "0":
                                    Kalp_Saniye += int(Kalp_Yazi[24:26])

                                Kalp_Saniye += 5
                                kalpler_bekleme += Kalp_Saniye
                            except:
                                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Kalplerde Bir Hata Oluştu. (Geçiliyor){Fore.WHITE}\n", 0.01)
                                Kalp_Dakika = 0
                                Kalp_Saniye = 0
                                kalpler_bekleme = 0

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Kalp Kalan Süre: {Fore.LIGHTCYAN_EX}{Kalp_Dakika}{Fore.LIGHTMAGENTA_EX} Dakika ve {Fore.LIGHTCYAN_EX}{Kalp_Saniye%60}{Fore.LIGHTMAGENTA_EX} Saniye.{Fore.WHITE}\n", 0.01)

                            driver.refresh()
                        else:
                            pass
                    else:
                        pass
                    
                except Exception as Kalpler_Hata:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Kalp Göndermeye Çalışırken Bir Hata Oluştu.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Hata: {Kalpler_Hata}{Fore.WHITE}\n", 0.01)
                    Kalp_Dakika = 0
                    Kalp_Saniye = 0
                    kalpler_bekleme = 0

                try:
                    
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                    try:
                        driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/button').click()
                        driver.find_element_by_xpath('//*[@id="sid7"]/div/form/div/input').send_keys(url)
                        Paylasim_Devam1 = True
                    except:
                        Paylasim_Devam1 = False
                        type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.RED}Paylaşım Gönderme Sayfası Kapalı.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Skipping...\n{Fore.WHITE}", 0.01)
                        Paylasim_Dakika = 0
                        Paylasim_Saniye = 0
                        paylasimlar_bekleme = 0

                    if Paylasim_Devam1 == True:
                        driver.find_element_by_xpath('//*[@id="sid7"]/div/form/div/div/button').click()
                        time.sleep(3)
                        try:
                            driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button').click()
                            Paylasim_Devam2 = True
                        except:
                            Paylasim_Devam2 = False
                            type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Paylaşım Daha Hazır Değil. Geçiliyor.\n {Fore.WHITE}", 0.01)
                            Paylasim_Yazi = driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div/h4').text
                            time.sleep(3)

                            if Paylasim_Yazi[13] == " ":
                                Paylasim_Dakika = int(Paylasim_Yazi[12])
                                Paylasim_Saniye = Paylasim_Dakika * 60

                            elif Paylasim_Yazi[13] != " ":
                                Paylasim_Dakika = int(Paylasim_Yazi[12:14])
                                Paylasim_Saniye = Paylasim_Dakika * 60

                            if Paylasim_Yazi[24] == "0":
                                Paylasim_Saniye += int(Paylasim_Yazi[25])
                            elif Paylasim_Yazi[24] != "0":
                                Paylasim_Saniye += int(Paylasim_Yazi[24:26])

                            Paylasim_Saniye += 5
                            paylasimlar_bekleme += Paylasim_Saniye

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Paylaşım Kalan Süre: {Fore.LIGHTCYAN_EX}{Paylasim_Dakika}{Fore.LIGHTMAGENTA_EX} Dakika ve {Fore.LIGHTCYAN_EX}{Paylasim_Saniye%60}{Fore.LIGHTMAGENTA_EX} Saniye.{Fore.WHITE}\n", 0.01)
                            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()

                        if Paylasim_Devam2 == True:
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Paylaşım Gönderildi!\n{Fore.WHITE}", 0.01)
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Lütfen Bekleyin...{Fore.WHITE}\n", 0.01)
                            time.sleep(10)
                            Paylasim_Yazi = driver.find_element_by_xpath('/html/body/div[4]/div[6]/div/div/h4').text

                            try:
                                if Paylasim_Yazi[13] == " ":
                                    Paylasim_Dakika = int(Paylasim_Yazi[12])
                                    Paylasim_Saniye = Paylasim_Dakika * 60

                                elif Paylasim_Yazi[13] != " ":
                                    Paylasim_Dakika = int(Paylasim_Yazi[12:14])
                                    Paylasim_Saniye = Paylasim_Dakika * 60

                                if Paylasim_Yazi[24] == "0":
                                    Paylasim_Saniye += int(Paylasim_Yazi[25])
                                elif Paylasim_Yazi[24] != "0":
                                    Paylasim_Saniye += int(Paylasim_Yazi[24:26])

                                Paylasim_Saniye += 5
                                paylasimlar_bekleme += Paylasim_Saniye
                            except:
                                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Paylaşımda Bir Hata Oluştu. (Geçiliyor){Fore.WHITE}\n", 0.01)
                                Paylasim_Dakika = 0
                                Paylasim_Saniye = 0
                                paylasimlar_bekleme = 0

                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Paylaşım Kalan Süre: {Fore.LIGHTCYAN_EX}{Paylasim_Dakika}{Fore.LIGHTMAGENTA_EX} Dakika ve {Fore.LIGHTCYAN_EX}{Paylasim_Saniye%60}{Fore.LIGHTMAGENTA_EX} Saniye.{Fore.WHITE}\n", 0.01)

                except Exception as Paylasimlar_Hata:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Paylaşım Göndermeye Çalışırken Bir Hata Oluştu.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Hata: {Paylasimlar_Hata}{Fore.WHITE}\n", 0.01)
                    Paylasim_Dakika = 0
                    Paylasim_Saniye = 0
                    paylasimlar_bekleme = 0
                    driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()

            except Exception as AllError:
                type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Takipçi, Kalp, İzlenme ve Paylaşım Göndermeye Çalışırken Bir Hata Oluştu.\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Muhtemelen Sunucu Arızalı, Sorun Gidermeye Çalışıyor.\n", 0.01)
                if driver.title == "502 Sunucu Hatası":
                    type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Sunucuda Hata Var.. Düzeltmeye Çalışıyor.\n", 0.01)
                    while driver.title == "502 Sunucu Hatası":
                        time.sleep(20)
                        driver.refresh()
                        if driver.title != "502 Sunucu Hatası":
                            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Sorun Çözüldü. Bot Aktif!\n", 0.01)
                            break
                else:
                    type(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Sorunu Çözemedim. Internetinde Sorun Olabilirmi?\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Hata: {AllError}\n\n{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Program Kapatılıyor.{Fore.WHITE}\n", 0.01)
                    time.sleep(7)
                    exit()

            driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
            amount += 1
            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.GREEN}Sonuç : Takip, Kalpler, İzlenme, & Paylaşım {amount} Kere Oldu.{Fore.WHITE}", 0.01)

            UzunBekleme = [takipler_bekleme, kalpler_bekleme, izlenmeler_bekleme, paylasimlar_bekleme]
            UzunBekleme.sort()
            AntiAFKSuresi = int(UzunBekleme[-1]) + 60
            AntiAFKSuresi /= 5

            Takip_Bosluk = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Takip: {Fore.LIGHTCYAN_EX}{Takip_Dakika}d, {takipler_bekleme%60}s ({takipler_bekleme}s){Fore.WHITE}') - 13)
            Kalp_Bosluk = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Kalpler: {Fore.LIGHTCYAN_EX}{Kalp_Dakika}d, {kalpler_bekleme%60}s ({kalpler_bekleme}s){Fore.WHITE}') - 13)
            Izlenme_Bosluk = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}İzlenme: {Fore.LIGHTCYAN_EX}{Izlenme_Dakika}d, {izlenmeler_bekleme%60}s ({izlenmeler_bekleme}s){Fore.WHITE}') - 13)
            Paylasim_Bosluk = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Paylaşım: {Fore.LIGHTCYAN_EX}{Paylasim_Dakika}d, {paylasimlar_bekleme%60}s ({paylasimlar_bekleme}s){Fore.WHITE}') - 13)
            AntiAFK_Bosluk = 85 - (len(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}5x Yenilemeden Önce Saniye: {Fore.LIGHTCYAN_EX}{AntiAFKSuresi}{Fore.WHITE}') - 13)

            print(f"""
{" "*round(os.get_terminal_size().columns/2-42)}╔═════════════════════════════════════════════════════════════════════════╗
{" "*round(os.get_terminal_size().columns/2-42)}║                             {Fore.LIGHTGREEN_EX}Lütfen Bekleyin{Fore.WHITE}                             ║
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                         ║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Takip: {Fore.LIGHTCYAN_EX}{Takip_Dakika}d, {takipler_bekleme%60}s ({takipler_bekleme}s){Fore.WHITE}{Takip_Bosluk*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Kalpler: {Fore.LIGHTCYAN_EX}{Kalp_Dakika}d, {kalpler_bekleme%60}s ({kalpler_bekleme}s){Fore.WHITE}{Kalp_Bosluk*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}İzlenme: {Fore.LIGHTCYAN_EX}{Izlenme_Dakika}d, {izlenmeler_bekleme%60}s ({izlenmeler_bekleme}s){Fore.WHITE}{Izlenme_Bosluk*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Paylaşım: {Fore.LIGHTCYAN_EX}{Paylasim_Dakika}d, {paylasimlar_bekleme%60}s ({paylasimlar_bekleme}s){Fore.WHITE}{Paylasim_Bosluk*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║     {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}5x Yenilemeden Önce Saniye: {Fore.LIGHTCYAN_EX}{AntiAFKSuresi}{Fore.WHITE}{AntiAFK_Bosluk*' '}║
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                         ║
{" "*round(os.get_terminal_size().columns/2-42)}╚═════════════════════════════════════════════════════════════════════════╝
""")
            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Hatırlatma: {Fore.LIGHTMAGENTA_EX}Lütfen Chrome Web Sürücüsündeki Sekmelerle Etkileşim Yapmayın, Kodu Karıştırıp Hata Verebilir..!", 0.01)
            
            type(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Lütfen Bekleyin...{Fore.WHITE}\n", 0.01)
            
            time.sleep(AntiAFKSuresi)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Oturumun Süresinin Dolmasını Önlemek İçin Yenileniyor. {Fore.LIGHTCYAN_EX}(1/5 Bekleyin){Fore.WHITE}\n", 0.01)

            time.sleep(AntiAFKSuresi)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Oturumun Süresinin Dolmasını Önlemek İçin Yenileniyor. {Fore.LIGHTCYAN_EX}(2/5 Bekleyin){Fore.WHITE}\n", 0.01)

            time.sleep(AntiAFKSuresi)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Oturumun Süresinin Dolmasını Önlemek İçin Yenileniyor. {Fore.LIGHTCYAN_EX}(3/5 Bekleyin){Fore.WHITE}\n", 0.01)

            time.sleep(AntiAFKSuresi)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Oturumun Süresinin Dolmasını Önlemek İçin Yenileniyor. {Fore.LIGHTCYAN_EX}(4/5 Bekleyin){Fore.WHITE}\n", 0.01)

            time.sleep(AntiAFKSuresi)
            driver.refresh()
            type(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Oturumun Süresinin Dolmasını Önlemek İçin Yenileniyor. {Fore.LIGHTCYAN_EX}(5/5 Bekleyin){Fore.WHITE}\n", 0.01)

            takipler_bekleme = 0
            kalpler_bekleme = 0
            izlenmeler_bekleme = 0
            paylasimlar_bekleme = 0

            Takip_Saniye = 0
            Takip_Dakika = 0

            Kalp_Saniye = 0
            Kalp_Dakika = 0

            Izlenme_Dakika = 0
            Izlenme_Saniye = 0

            Paylasim_Dakika = 0
            Paylasim_Saniye = 0
            type(f"\n{Fore.LIGHTGREEN_EX}Şimdi Yeniden Başlatılıyor...\n", 0.01)
            time.sleep(34)

colorama.init()
time.sleep(7)
os.system('cls')

yazTiktokBot()
type(f'{" "*round(os.get_terminal_size().columns/2-14)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Yapımcı: {Fore.LIGHTMAGENTA_EX}OsmanCitci {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]\n{" "*round(os.get_terminal_size().columns/2-30)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTMAGENTA_EX}https://github.com/OsmanCitci/TikTokIzlenme {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]', wait = 0.01)
yazAyarlar()

while True:
    secim = input(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.GREEN}Seçim: {Fore.LIGHTMAGENTA_EX}")
    if secim == "1":
        basla()
        break
    elif secim == "2":
        yazBilgi()
    elif secim == "3":
        yazAyarlar()
    elif secim == "4":
        temizle()
    elif secim =="5":
        exit()
        
#gig

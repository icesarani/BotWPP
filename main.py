from selenium import webdriver
import time

browser = webdriver.Chrome("./driver/chromedriver.exe") #llamo al driver de opera

def botWpp():
    '''Funcion principal'''

    browser.get("https://web.whatsapp.com") #abro la pagina de wpp
    time.sleep(5) #pongo a dormir el bot por 5 secs

    espera = True
    while espera:
        print("Esperando...")
        espera = validarQR()
        time.sleep(2)
        if espera == False:
            print("Se autentico el QR...")
            break
    seleccionarChat("compu")
    enviarMensaje("ola putito")

def validarQR():
    '''Obtengo el QR de la pagina, el QR se llama canvas'''

    try:
        element = browser.find_element_by_tag_name("canvas")
    except:
        return False

    return True

def seleccionarChat(nombre : str):
    '''Busco obtengo y abro el chat que se le indica'''

    buscando = True

    while buscando:
        print("Buscando el chat")
        time.sleep(2)
        elements = browser.find_elements_by_tag_name("span") #obtiene los chats (span) que hay en mi wpp
        for element in elements: #paso por todos los chats
            if element.text == nombre:
                print("Encontre el chat")
                buscando = False
                element.click()
                break

def enviarMensaje(mensaje : str):
    '''Envio el mensaje al chattbox agregado'''

    chatbox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]') #me posiciono en la caja de enviar mensajes
    chatbox.send_keys(mensaje) #printeo el mensaje en el chatbox
    time.sleep(2)
    enviar() #le doy a enviar

def enviar():
    '''Clickeo del boton de enviar'''
    element = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')
    element.click()
    print("Mensaje enviado")

botWpp()
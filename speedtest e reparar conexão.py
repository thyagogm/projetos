from PySimpleGUI import PySimpleGUI as sg
from speedtest import Speedtest
import os

tema = sg.theme('DarkBlack1')


def get_speed():
    s = Speedtest()
    s.get_servers()
    s = Speedtest()
    download = s.download()
    s = Speedtest()
    upload = s.upload()
    s = Speedtest()
    melhor_server = s.get_best_server()
    download_speed = round(download / (10 ** 6), 2)
    upload_speed = round(upload / (10 ** 6), 2)
    resultado = [
        [sg.Text('Velocidade de Download: {}Mbps'.format(download_speed))],
        [sg.Text('Velocidade de Upload: {}Mbps'.format(upload_speed))],
        [sg.Text('Latência: {}Ms'.format(melhor_server['latency']))],
        [sg.Text('Servidor: {}'.format(melhor_server['name']))]
    ]
    janela2 = sg.Window('Resultado', resultado, margins=(100, 15))
    return janela2.read()


def reparar_conexao():
    try:
        os.system('route -f')
        os.system('ipconfig /release')
        os.system('ipconfig /renew')
        os.system('nbtstat -R')
        os.system('nbtstat -RR')
        os.system('ipconfig /flushdns')
        os.system('ipconfig /registerdns')
        sg.popup('Reparado com Sucesso')
    except os:
        sg.popup('Erro Desconhecido')


principal = [
    [sg.Button('Verificar Conexão')],
    [sg.Button('Reparar Conexão')]
]
janela = sg.Window('SpeedTest', principal, margins=(100, 15))

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Verificar Conexão':
        get_speed()
    elif eventos == 'Reparar Conexão':
        reparar_conexao()

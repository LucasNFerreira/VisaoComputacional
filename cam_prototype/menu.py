#!/usr/bin/env python
#coding:utf-8
import os
import json
import sys
import camera as cam


MSG_PROMPT = 'Pressione Enter para continuar\n'

#Exibe um menu com as opções do programa para o usuário.
def menu():
    os.system('clear')
    print '------ Visão Computacional - Simple CV -----\n'
    print 'Escolha um filtro'
    print '1 - Invert'
    print '2 - Greyscale'
    print '3 - Sepia'
    print '4 - MorphClose'
    print '5 - Nightvision Effect'
    print '0 - Sair'

def invert():
    cam.start_camera(1)	
    raw_input(MSG_PROMPT)

def greyscale():
    cam.start_camera(2)	
    raw_input(MSG_PROMPT)

def sepia_effect():
    cam.start_camera(3)	
    raw_input(MSG_PROMPT)

def darken_effect():
    cam.start_camera(4)	
    raw_input(MSG_PROMPT)

def nightvision_effect():
    cam.start_camera(5)	
    raw_input(MSG_PROMPT)

def sair():
    exit()

#Cria um dicionário que relaciona cada função.
operacoes = {1 : invert, 2 : greyscale, 3 : sepia_effect, 4 : darken_effect, 5 : nightvision_effect, 0: sair}

def switch(x):
    os.system('clear')
    try:
        operacoes[x]()
        print 'operacao de num ',x,' concluida'
    except Exception as e:
        print 'erro no switch: ', str(e)
        #Imprimindo o tipo da excecao, o nome do arquivo, e a linha do erro
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        raw_input(MSG_PROMPT)

if __name__ == '__main__':
    while True:
        try:
            menu()
            switch(input('\n\nDigite a opcao: \n'))
        except Exception as e:
            #print 'O valor digitado não é um número'
            print 'main error: ', str(e)
            raw_input(MSG_PROMPT)

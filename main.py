# importa bibliotecas
import pyautogui as auto
import time
# tempo que cada comando demora para executar
auto.PAUSE = 2

# abre o programa "vs code"
auto.press('win')
auto.write('vscode')
auto.press('enter')

# espera 10 segundos para abrir o vscode 
time.sleep(5)

# execução do commit
auto.hotkey('ctrl', 'shift', "'")
auto.write('git add .')
auto.press('enter')
auto.write('git commit -m "Repositorio atualizado automaticamente."')

# espera 5 segundos
time.sleep(5)

# finaliza o commit
auto.press('enter')
auto.write('git push')
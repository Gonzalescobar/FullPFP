from FullPFP import ProfilePicture
import colorama
import os
import time
import webbrowser

# Console application colors and functions

TerminalPointer = colorama.Style.BRIGHT+colorama.Fore.LIGHTCYAN_EX+"   $"+"  "+colorama.Style.RESET_ALL
TerminalPointerError = colorama.Style.BRIGHT+colorama.Fore.LIGHTRED_EX+"   $"+"  "+colorama.Style.RESET_ALL
TerminalPointerSucces = colorama.Style.BRIGHT+colorama.Fore.LIGHTGREEN_EX+"   $"+"  "+colorama.Style.RESET_ALL
def clearTer(): os.system('cls' if os.name == 'nt' else 'clear')


def main():
 try:

# Console application banner and instructions

  clearTer()

  print(colorama.Style.BRIGHT  + ''' \n\n\n
       /$$$$$$$$        /$$ /$$       /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
      | $$_____/       | $$| $$      | $$__  $$| $$_____/| $$__  $$
      | $$    /$$   /$$| $$| $$      | $$  \ $$| $$      | $$  \ $$
      | $$$$$| $$  | $$| $$| $$      | $$$$$$$/| $$$$$   | $$$$$$$/
      | $$__/| $$  | $$| $$| $$      | $$____/ | $$__/   | $$____/ 
      | $$   | $$  | $$| $$| $$      | $$      | $$      | $$      
      | $$   |  $$$$$$/| $$| $$      | $$      | $$      | $$      
      |__/    \______/ |__/|__/      |__/      |__/      |__/       \n''')
  time.sleep(0.2)
  print(
'''       __             __  __          __                       
      / /_  __  __   / / / /__  _____/ /_____ _________  ____ _
     / __ \/ / / /  / /_/ / _ \/ ___/ __/ __ `/ ___/ _ \/ __ `/
    / /_/ / /_/ /  / __  /  __/ /__/ /_/ /_/ / /  /  __/ /_/ / 
   /_.___/\__, /  /_/ /_/\___/\___/\__/\__,_/_/   \___/\__,_/  
         /____/  \n                                            
       ''')
  time.sleep(0.2)
  print(colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX +"     You can type 'exit' to exit, or 'help' to get a list of the commands \n\n\n"+ colorama.Style.RESET_ALL )
  input('\033[1A' + TerminalPointer + colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX + 'Press enter to start' +'\033[K')
  
# Console application interface
  
  while True:
   
   try:
    UserInput = input(colorama.Style.BRIGHT + '\033[1A' + TerminalPointer + colorama.Fore.LIGHTCYAN_EX +'FullPFP > ' + colorama.Fore.LIGHTWHITE_EX +'\033[K')
    if UserInput == "exit":
     clearTer()
     exit()
    try:
     webbrowser.open(urlFrom(UserInput))
    except Exception as e:
     input(e)
   except KeyboardInterrupt:
     main()
 except KeyboardInterrupt:
  main()

main()
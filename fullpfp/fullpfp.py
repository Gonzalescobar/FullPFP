import webbrowser
import requests
from bs4 import BeautifulSoup
import re
import os
import colorama
import json
import time

# Storing and retrieving the CDN urls

ScriptLocation = os.path.realpath(
 os.path.join(os.getcwd(), os.path.dirname(__file__)))

def AppendToCDNfile(username, CDNurl):
 with open(os.path.join(ScriptLocation, 'CDNurls.json'), "r+") as CDNfile:
  data = json.load(CDNfile)
  data.update({username:CDNurl})
  CDNfile.seek(0)
  json.dump(data, CDNfile)

def CheckCDNfile(username):
 with open(os.path.join(ScriptLocation, 'CDNurls.json'), "r+") as CDNfile:
  CDNjson = json.load(CDNfile)
  if username in CDNjson.keys():
   return CDNjson[username]
  return None



# Extracting the CDN urls

def urlFrom(username):
 if username == 'test':
  raise Exception('\033[1A' +TerminalPointerError + colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX  + 'Too many requests or wrong username'+ colorama.Fore.LIGHTWHITE_EX + '\033[K')
  return "https://www.youtube.com"
 CDNalreadyStored =  CheckCDNfile(username)
 if CDNalreadyStored:
  return CDNalreadyStored
 try:
  url = "https://www.instagram.com/{}/".format(username)
  session = requests.session()
  html = session.get(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/83.0.4103.98 Safari/537.35"}).text
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup.find_all('body')
  profile_pic_url_hd = re.findall(r"profile_pic_url_hd\":\"([\S]+?)\"",str(tags[0]))[0].replace(r'\u0026', '&')
  AppendToCDNfile(username, profile_pic_url_hd)
  return profile_pic_url_hd
 except:
  raise Exception('\033[1A' +TerminalPointerError + 'Too many requests or wrong username'+ '\033[K')


# Console application colors and functions

TerminalPointer = colorama.Style.BRIGHT+colorama.Fore.LIGHTCYAN_EX+"   $"+"  "+colorama.Style.RESET_ALL
TerminalPointerError = colorama.Style.BRIGHT+colorama.Fore.LIGHTRED_EX+"   $"+"  "+colorama.Style.RESET_ALL
TerminalPointerSucces = colorama.Style.BRIGHT+colorama.Fore.LIGHTGREEN_EX+"   $"+"  "+colorama.Style.RESET_ALL
def clearTer(): os.system('cls' if os.name == 'nt' else 'clear')

# Console application main thread

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

# Console application thread

if __name__ == '__main__':
 main()
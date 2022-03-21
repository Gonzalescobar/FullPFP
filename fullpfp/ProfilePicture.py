import requests
from bs4 import BeautifulSoup
import re
import json

# Storing and retrieving the CDN urls

def AppendToCDNfile(username, CDNurl):
 try:
  with open('CDNurls.json', "r+") as CDNfile:
   data = json.load(CDNfile)
   data.update({username:CDNurl})
   CDNfile.seek(0)
   json.dump(data, CDNfile)
 except:
  with open('CDNurls.json', "w") as CDNfile:
   CDNfile.write('{"hectarea": "https://www.instagra.com/hectareatools"}')
   CDNfile.close()
   AppendToCDNfile(username, CDNurl)

def CheckCDNfile(username):
 try:
  with open('CDNurls.json', "r+") as CDNfile:
   CDNjson = json.load(CDNfile)
   if username in CDNjson.keys():
    return CDNjson[username]
   return None
 except Exception as e:
  with open('CDNurls.json', "w") as CDNfile:
   CDNfile.write('{"hectarea": "https://www.instagra.com/hectareatools"}')
   CDNfile.close()
   CheckCDNfile(username)



# Extracting the CDN urls

def urlFrom(username):
 if username == 'test':
  raise Exception('\033[1A' + 'Too many requests or wrong username' + '\033[K')
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
  raise Exception('\033[1A' + 'Too many requests or wrong username'+ '\033[K')

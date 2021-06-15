from os import system
import os,sys
from time import sleep
from bs4 import BeautifulSoup
import requests
from colorama import Fore
system('clear')
s=0
red='\u001b[31;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
yellow='\u001b[33;1m'
reset='\u001b[0m'
back_red='\u001b[41m'
back_green='\u001b[42m'
back_yellow='\u001b[43m'
back_blue='\u001b[44m'
cookie=input(back_blue+"Nhập Cookie FB:"+reset)
while not cookie:
  exit(red+"Không Nhập Cookie Chạy Kiểu Gì Ba!!")
os.system("clear")
print(green)
print("\t\t\t░█████╗░██████╗░")
print("\t\t\t██╔══██╗██╔══██╗")
print("\t\t\t██║░░╚═╝██████╦╝")
print("\t\t\t██║░░██╗██╔══██╗")
print("\t\t\t╚█████╔╝██████╦╝")
print("\t\t\t░╚════╝░╚═════╝░")

print("\t\t████████╗░█████╗░░█████╗░██╗░░░░░")
print("\t\t╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░")
print("\t\t░░░██║░░░██║░░██║██║░░██║██║░░░░░")
print("\t\t░░░██║░░░██║░░██║██║░░██║██║░░░░░")
print("\t\t░░░██║░░░╚█████╔╝╚█████╔╝███████╗")
print("\t\t░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝")
print (back_yellow+"\t\t\tTOOL NUÔI FB V2"+reset)
print (back_blue+"\t\t\tTELEGRAM:"+reset,green+"@Chi2911ks")
print ("\n")
print (yellow+"1.Thêm Bạn Bè"+reset)
print (green+"2.LikePost"+reset)
print (red+"3.Random Thêm Bạn Bè Và Like")
print (blue+"4.Unfollow")
choose=input(blue+"Nhập Một Số Để Tiếp Tục:")
url="https://mbasic.facebook.com/friends/center/suggestions/?mff_nav=1&ref=wizard"
url_un="https://m.facebook.com/timeline/app_collection/?collection_token=100050011458036%3A2356318349%3A33&_rdr"
url_story="https://mbasic.facebook.com/"
head_fb={
  'Host':'mbasic.facebook.com',
  'user-agent':'Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'cookie':cookie,
}
if choose=="1":
  hl=int(input(back_blue+"Nhập Delay:"+reset))
  while True:
    web =requests.get(url,headers=head_fb)
    soup=BeautifulSoup(web.text,"html.parser")
    death=soup.title
    for đnp in death.children:
      if "Đăng nhập Facebook" in đnp:
        exit (Fore.RED+"Die Cookie")
    lo =soup.find_all("a",href=True)
    for t in lo:
      po=t["href"]
      if "/friends/hovercard/mbasic/?" in po:
        web2=requests.get("https://mbasic.facebook.com/"+po,headers=head_fb,allow_redirects=True)
        soup2=BeautifulSoup(web2.text,"html.parser")
        a=soup2.title
        for us in a.children:
          print (Fore.YELLOW+us)
        tên=soup2.find_all("a",href=True)
        for i in tên:
          tbb=i["href"]
          if "/a/mobile/friends/add_friend.php?"in tbb:
            requests.get("https://mbasic.facebook.com/"+tbb,headers=head_fb,allow_redirects=True)
            s=s+1
            print (Fore.RED+"[",s,"]",Fore.GREEN+"Đã Thêm Bạn Bè")
            for time in range(hl,-1,-1):
              sleep(1)
              print (yellow+"Đợi",time,"Giây",end=" \r")
            
if choose=="2":
  hl=int(input(back_blue+"Nhập Delay:"+reset))
  while True:
    web3=requests.get(url_story,headers=head_fb)
    soup3=BeautifulSoup(web3.text,"html.parser")
    die=soup3.title
    for đnhap in die.children:
      if "Đăng nhập Facebook" in đnhap:
        exit (Fore.RED+"Die Cookie")
    tìm=soup3.find_all("a",href=True)
    for story in tìm:
      bài=story["href"]
      if "/story.php?" in bài:
        web4=requests.get("https://mbasic.facebook.com/"+bài,headers=head_fb,allow_redirects=True)
        soup4=BeautifulSoup(web4.text,"html.parser")
        mh =soup4.title
        for ifh in mh.children:
          print ("",end=" \r")
        tìm_a=soup4.find_all("a",href=True)
        for cg in tìm_a:
          link=cg["href"]
          if "/a/like.php?" in link:
            web5=requests.get("https://mbasic.facebook.com/"+link,headers=head_fb,allow_redirects=True)
            s = s + 1
            print (red+"[ "+str(s)+" ]"+Fore.GREEN+"Đã Like Thành Công Bài Viết:",ifh)
            soup5=BeautifulSoup(web5.text,"html.parser")
            block=soup5.title
            for chặn in block.children:
              if "Tài khoản của bạn hiện bị hạn chế"in chặn:
                exit(Fore.RED+"Bị Block")
            for time in range(hl,-1,-1):
              sleep(1)
              print (yellow+"Đợi",time,"Giây",end=" \r")
if choose=="3":
  hl=int(input("Time:"))
  while True:
    web =requests.get(url,headers=head_fb)
    soup=BeautifulSoup(web.text,"html.parser")
    death=soup.title
    for đnp in death.children:
      if "Đăng nhập Facebook" in đnp:
        exit (Fore.RED+"Die Cookie")
    lo =soup.find_all("a",href=True)
    for t in lo:
      po=t["href"]
      if "/friends/hovercard/mbasic/?" in po:
        web2=requests.get("https://mbasic.facebook.com/"+po,headers=head_fb,allow_redirects=True)
        soup2=BeautifulSoup(web2.text,"html.parser")
        a=soup2.title
        for us in a.children:
          print (Fore.YELLOW+us)
        tên=soup2.find_all("a",href=True)
        for i in tên:
          tbb=i["href"]
          if "/a/mobile/friends/add_friend.php?"in tbb:
            requests.get("https://mbasic.facebook.com/"+tbb,headers=head_fb,allow_redirects=True)
            s=s+1
            print (Fore.RED+"[",s,"]",Fore.GREEN+"Đã Thêm Bạn Bè")
        web3=requests.get(url_story,headers=head_fb)
        soup3=BeautifulSoup(web3.text,"html.parser")
        die=soup3.title
        for đnhap in die.children:
          if "Đăng nhập Facebook" in đnhap:
            exit (Fore.RED+"Die Cookie")
        tìm=soup3.find_all("a",href=True)
        for story in tìm:
          bài=story["href"]
          if "/story.php?" in bài:
            web4=requests.get("https://mbasic.facebook.com/"+bài,headers=head_fb,allow_redirects=True)
            soup4=BeautifulSoup(web4.text,"html.parser")
            mh =soup4.title
            for ifh in mh.children:
              print ("",end=" \r")
            tìm_a=soup4.find_all("a",href=True)
            for cg in tìm_a:
              link=cg["href"]
              if "/a/like.php?" in link:
                web5=requests.get("https://mbasic.facebook.com/"+link,headers=head_fb,allow_redirects=True)
                print (Fore.GREEN+"Đã Like Thành Công Bài Viết:",ifh)
                soup5=BeautifulSoup(web5.text,"html.parser")
                block=soup5.title
                for chặn in block.children:
                  if "Tài khoản của bạn hiện bị hạn chế"in chặn:
                    exit(Fore.RED+"Bị Block")
                for time in range(hl,-1,-1):
                  sleep(1)
                  print (yellow+"Đợi",time,"Giây",end=" \r")    
if choose=="4":
  hl=int(input("Nhập Delay:"))
  while True:
    web=requests.get(url_un,headers=head_fb)
    print (web.text)

import time
import urllib
import sys
import os

os.system('clear')
os.system("toilet -f smblock --filter border:metal '========================================'")
os.system("toilet -f smblock --filter border:metal '~ ~ AnNoY   CreaTionS ~ ~'")
os.system("toilet -f smblock --filter border:metal '========================================'")
time.sleep(4)

os.system('clear')

bar = "\033[1;34;40m\n#########################################################\n"

def name():
        os.system("toilet -f smblock --filter border:metal '~ ~ Mega Run ~ ~'")
        print("\033[1;35;40m--------------------------------,\n")
        print("\033[0;37;46m| Author    : Annoy Creations   |,\n")
        print("\033[0;37;46m| Telegrame : t.me/hackerrdt    |,\n")
        print("\033[0;37;46m| FaceBook  : Network Hacker    |,\n")
        print("\033[1;35;40m--------------------------------,\n")
print(name(),"\n")

try:
    f = open("auth.txt", "r")
    auth = f.read()
    f.close
except:
    wr = str(input("\033[1;36;40mPaste Your Auth here :- "))
    f = open("auth.txt", "w")
    f.write(wr)
    f.close
    f = open("auth.txt", "r")
    auth = f.read()
    f.close

try:
    f = open("url.txt", "r")
    f = open("url.txt", "r")
    url1 = f.read()
    f.close
except:
    wr = str(input("\033[1;36;40mPaste Your URL here :- "))
    f = open("url.txt", "w")
    f.write(wr)
    f.close
    f = open("url.txt", "r")
    url1 = f.read()
    f.close

try:
    import requests


except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests


def main():
    os.system("clear")
    print(name(),"\n")
    header = {"Host": "megarun.dialog.lk",
              "Authorization": auth, "X-Unity-Version": "2018.3.0f2"}
    url = url1
    ss=0
    time.sleep(90)
    while True:
        size = 0
        res = requests.get(url, headers=header)
        resp = str(res)
        if resp == '<Response [204]>':
            print(bar)
            print("\n\033[0;37;42m [#] No Data ... [#]")
            print(bar)
        elif resp == '<Response [200]>':
            print(bar)
            print("\n\033[0;37;42m [#] $ You Won Data $... [#]")
            print(bar)
        else:
            print(bar)
            print("\n\033[0;37;41m [#] Check Again, You may be a Blocked User... [#]")
            print(bar)

        ss+=1
        print("\033[1;34;40m\n",str(ss), "Plz  Wait For Next round",end="")
        for i in range(180):

            pr = i/180*100
            print("\033[0;34;47m\n>>> [#]",str(int(pr)) +"% ",end="")

            time.sleep(0.5)
            sys.stdout.write("\033[F")

    os.system('toilet Mission Complete!!!')
    again()


def again():
    again = input('\033[1;36;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()

#!/usr/bin/python3
import os,pdfplumber,colorama,time,io,threading,chardet
from itertools import product

class Genrator:

    def BrutForce(self,my_str,min,max):
        for i in range(min,max+1):
            for w in product(my_str,repeat=i):
                word = "".join(w)
                yield word

    def Dictionay(self,file_name_or_path):
        f = open(file_name_or_path,"rb")
        pass_list = f.readlines()
        f.close()
        for i in pass_list:
            detection = chardet.detect(i)
            encoding = detection["encoding"]
            try:
                yield i.decode(encoding).replace("\n","")
            except:pass


class Check_Key:

    def pdf_key(self,file_name_or_path,password):
        try:
            with pdfplumber.open(file_name_or_path,password=password) as pdf:
                return True
        except pdfplumber.pdfminer.pdfdocument.PDFPasswordIncorrect:
            return False

class PyCrack:
    def __init__(self):
        self.gen = Genrator()
        self.key = Check_Key()
        #------------------------------colors-----------
        self.red = colorama.Fore.RED
        self.yellow = colorama.Fore.YELLOW
        self.blue = colorama.Fore.BLUE
        self.green = colorama.Fore.GREEN
        self.reset = colorama.Fore.RESET

        self.bright = colorama.Style.BRIGHT
        self.dim = colorama.Style.DIM
        self.normal = colorama.Style.NORMAL
        self.reset_all = colorama.Style.RESET_ALL
        #-----------------------------------------------

        self.intro = ""
    def pass_found(self,target,key,obj_time_time):
        main.clear()
        print(self.intro)
        style = "-"*len(key)
        style2 = "-"*len(target)
        hours,mins,sec = main.stop_watch(obj_time_time)
        time_len = "-"*len(f"{hours}{mins}{sec}")
        show_key = f"""{self.bright}{self.red}
        ,-----------{time_len}---------------,
        |     {self.green}Time:   {self.red}[{self.green}{hours}{self.red}:{self.green}{mins}{self.red}:{self.green}{sec}{self.red}]         |
        '---------------{time_len}-----------'{self.bright}{self.red}
        ,---------------------------------{style}{style2}----------------,
        |   {self.green}Password Found :  {self.blue}Target : {self.red}[{self.green}{target}{self.red}] {self.blue}Password : {self.red}[{self.green}{key}{self.red}]   |
        '---------------------------------{style}{style2}----------------'
        {self.reset_all}
        """
        print(show_key)
    def dic_genrated(self,target,key,obj_time_time):
        main.clear()
        print(self.intro)
        style = "-"*len(key)
        style2 = "-"*len(target)
        hours,mins,sec = main.stop_watch(obj_time_time)
        time_len = "-"*len(f"{hours}{mins}{sec}")
        show_key = f"""{self.bright}{self.red}
        ,-----------{time_len}---------------,
        |     {self.green}Time:   {self.red}[{self.green}{hours}{self.red}:{self.green}{mins}{self.red}:{self.green}{sec}{self.red}]         |
        '---------------{time_len}-----------'{self.bright}{self.red}
        ,--------------------------------------{style}{style2}----------------,
        |   {self.green}Dictionay Genratd :  {self.blue}Target : {self.red}[{self.green}{target}{self.red}] {self.blue}File Seved : {self.red}[{self.green}{key}{self.red}]   |
        '--------------------------------------{style}{style2}----------------'
        {self.reset_all}
        """
        print(show_key)
    def clear(self):
        os.system("clear")
    def stop_watch(self,start_time):
        tt = time.time() - start_time 
        mins= tt // 60
        sec = tt % 60
        hours = mins // 60
        mins = mins % 60 
        return int(hours),int(mins),int(sec)

    def dic_gen_show(self):
        while self.th_stop:
            for i in ["\\","|","/","-"]:
                time.sleep(0.4)
                dot = i*3
                print()
                print(f"\033[A{self.bright}{self.red}Genrating{dot} {self.reset_all}\033[A")
    def trying(self,key,obj_time_time):
        hours,mins,sec = main.stop_watch(obj_time_time)
        key_len = " "*int(20-len(key))
        print()
        print(f"\033[A{self.bright}{self.red}Trying [{self.green}{key}{self.red}]{key_len}[{self.blue}{hours}:{mins}:{sec}{self.red}] [{self.blue}Ctrl+C for Kill{self.red}]{self.reset_all}\033[A")
    def my_start(self):
        main.clear()
        print(self.intro)
        print(f"{self.blue}Select {self.red}[1]{self.blue} BrutForce {self.red}[2]{self.blue} Dictionay {self.red}[0]{self.blue} Exit")
        commands = input(f"{self.bright}{self.red}Py{self.green}@{self.red}Crack~#{self.reset_all} ")
        if commands =="0":
            print(f"{self.bright}{self.green}You have Exited.{self.reset_all}")
            exit()
        #===================================================================================================================================================================================================================================    
        elif commands == "1":
            print(f"{self.blue}Select {self.red}[1]{self.blue} PDF {self.red} [0]{self.blue} Exit{self.reset_all}")
            b_commands = input(f"{self.bright}{self.red}Py{self.green}@{self.red}Crack/BrutForce~#{self.reset_all} ")
            if b_commands == "1":
                b_pdf = input(f"{self.red}Input PDF File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Charectors >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Lenth Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Lenth Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.pdf_key(b_pdf,i) == True:
                        main.pass_found(b_pdf,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press inter to main #{self.reset_all}")
                return
                main.my_start()
                


        elif commands == "2":
            print(f"{self.blue}Select {self.red}[1]{self.blue} PDF {self.red} [0]{self.blue} Exit{self.reset_all}")
            b_commands = input(f"{self.bright}{self.red}Py{self.green}@{self.red}Crack/Dictionay~#{self.reset_all} ")
            if b_commands == "1":
                b_pdf = input(f"{self.red}Input PDF File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_dic = input(f"{self.red}Input Dictionay File Path or Name >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.pdf_key(b_pdf,i) == True:
                        main.pass_found(b_pdf,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press inter to main #{self.reset_all}")
                main.my_start()

            
if __name__ == "__main__":
    while True:
        try:
            main = PyCrack()
            main.my_start()
        except KeyboardInterrupt:
            pass
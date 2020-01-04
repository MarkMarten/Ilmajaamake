from tkinter import *
from tkinter import ttk
import ctypes
import requests
from bs4 import BeautifulSoup


try:
    ## ------------- GET DATA FROM WEBSITE ---------------- ##
    #TARTU
    page_tartu=requests.get("https://www.ilmataat.ee/hetkel/0795") #page
    soup_tartu=BeautifulSoup(page_tartu.content, "html.parser") #supp
    date_tartu=soup_tartu.find("div", class_="date").get_text() #uuendatud
    hetkel_tartu_kraad=soup_tartu.find_all("div", class_="temperature")[0].get_text()
    hetkel_tartu_ilm=soup_tartu.find_all("div", class_="desc")[0].get_text()
    hetkel_tartu_tajutav=soup_tartu.find_all("div",class_="realfeel")[0].get_text()
    hetkel_tartu_tuul=soup_tartu.find_all("span",class_="value")[1].get_text()
    hetkel_tartu_tuulepuhang=soup_tartu.find_all("span",class_="value")[2].get_text()
    hetkel_tartu_pilvisus=soup_tartu.find_all("span",class_="value")[3].get_text()
    hetkel_tartu_sademed=soup_tartu.find_all("span",class_="value")[4].get_text()





    #----------------------
    #VÕRU
    page_võru=requests.get("https://www.ilmataat.ee/hetkel/0919")
    soup_võru=BeautifulSoup(page_võru.content,"html.parser")
    date_võru=soup_võru.find("div",class_="date").get_text()
    hetkel_võru_kraad=soup_võru.find_all("div",class_="temperature")[0].get_text()
    hetkel_võru_ilm=soup_võru.find_all("div", class_="desc")[0].get_text()
    hetkel_võru_tajutav=soup_võru.find_all("div",class_="realfeel")[0].get_text()
    hetkel_võru_tuul=soup_võru.find_all("span",class_="value")[1].get_text()
    hetkel_võru_tuulepuhang=soup_võru.find_all("span",class_="value")[2].get_text()
    hetkel_võru_pilvisus=soup_võru.find_all("span",class_="value")[3].get_text()
    hetkel_võru_sademed=soup_võru.find_all("span",class_="value")[4].get_text()




    ## ---------------- GUI -------------------------- ##
    #Window
    window=Tk()
    window.title("Ilmajaamake")
    window.geometry("390x160")

    #Tabs
    tab_control = ttk.Notebook(window)

    #Tartu
    tartu = ttk.Frame(tab_control)
    tab_control.add(tartu, text='Tartu')

    tartu_uuendatud=Label(tartu,text=date_tartu,width=25,anchor=E ) #uuendatud
    tartu_uuendatud.grid(column=0,row=15)

    tartu_hetkel=Label(tartu, text="Ilm hetkel:",width=20,anchor=W,font="Arial 10",pady=2,padx=2) #hetkel
    tartu_hetkel.grid(column=0,row=1)
    tartu_hetkel1=Label(tartu,text=hetkel_tartu_kraad+"C",font="Arial 10",relief="groove",pady=2,padx=2) #kraad
    tartu_hetkel1.grid(column=0,row=2)
    tartu_hetkel2=Label(tartu,text=hetkel_tartu_ilm,anchor=W,font="Arial 10",relief="groove",pady=2,padx=2) #ilm
    tartu_hetkel2.grid(column=0,row=3)
    tartu_hetkel3=Label(tartu,text=hetkel_tartu_tajutav+"C",anchor=W,font="Arial 10",relief="groove",pady=2,padx=2) #tajutav
    tartu_hetkel3.grid(column=0,row=4)
    tartu_hetkel4=Label(tartu,text="Tuule kiirus: "+hetkel_tartu_tuul,anchor=W,font="Arial 10",relief="groove",pady=2,padx=2)
    tartu_hetkel4.grid(column=1,row=2)
    tartu_hetkel6=Label(tartu,text="Pilvisus: "+hetkel_tartu_pilvisus,anchor=W,font="Arial 10",relief="groove",pady=2,padx=2)
    tartu_hetkel6.grid(column=1,row=3)
    tartu_hetkel7=Label(tartu,text="Sademed: "+hetkel_tartu_sademed,anchor=W,font="Arial 10",relief="groove",pady=2,padx=2)
    tartu_hetkel7.grid(column=1,row=4)


    x=Label(tartu,text=" ")
    x.grid(column=0,row=5)
    by_me=Label(tartu,text="www.ilmataat.ee           By: Marten",anchor=E,width=28)
    by_me.grid(column=1,row=15)





    #Võru
    võru = ttk.Frame(tab_control)
    tab_control.add(võru, text='Võru')

    võru_hetkel=Label(võru,text="Ilm hetkel:",width=20,anchor=W,font="Arial 10",pady=2,padx=8)
    võru_hetkel.grid(column=0,row=1)
    võru_hetkel1=Label(võru,text=hetkel_võru_kraad+"C",font="Arial 10",relief="groove",pady=2,padx=2)
    võru_hetkel1.grid(column=0,row=2)
    võru_hetkel2=Label(võru,text=hetkel_võru_ilm,anchor=W,font="Arial 10",relief="groove",pady=2,padx=2)
    võru_hetkel2.grid(column=0,row=3)
    võru_hetkel3=Label(võru,text=hetkel_võru_tajutav+"C",anchor=W,font="Arial 10",relief="groove",pady=2,padx=2)
    võru_hetkel3.grid(column=0,row=4)
    võru_hetkel4=Label(võru,text="Tuule kiirus: "+hetkel_võru_tuul,anchor=W,font="Arial 10",relief="groove",pady=2,padx=2)
    võru_hetkel4.grid(column=1,row=2)
    võru_hetkel6=Label(võru,text="Pilvisus: "+hetkel_võru_pilvisus,anchor=W,font="Arial 10",relief="groove",pady=2,padx=2)
    võru_hetkel6.grid(column=1,row=3)
    võru_hetkel7=Label(võru,text="Sademed: "+hetkel_võru_sademed,anchor=W,font="Arial 10",relief="groove",pady=2,padx=2)
    võru_hetkel7.grid(column=1,row=4)

    võru_uuendatud=Label(võru,text=date_võru,width=25,anchor=E ) #uuendatud
    võru_uuendatud.grid(column=0,row=15)
    x=Label(võru,text=" ")
    x.grid(column=0,row=5)
    by_me_võru=Label(võru,text="www.ilmataat.ee           By: Marten",anchor=E,width=28)
    by_me_võru.grid(column=1,row=15)


    tab_control.pack(expand=1, fill='both')
    window.mainloop()

except:
    ctypes.windll.user32.MessageBoxW(None, "Puudub internetiühendus või 'www.ilmataat.ee' on hetkel maas.", "Error",0)
    



    
    
    
    
    

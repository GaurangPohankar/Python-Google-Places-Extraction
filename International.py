#!/usr/bin/env python3
import tkinter
from tkinter import ttk
from bs4 import BeautifulSoup
from multiprocessing import Process
import urllib.request
from urllib.parse import quote 
import csv
import time
from getpass import getpass
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common import utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import codecs
import traceback
import re
import mysql.connector
import pymsgbox
from urllib.request import urlopen
import os 
#from progress.bar import Bar


class Begueradj(tkinter.Frame):
    '''
    classdocs
    '''  
    def __init__(self, parent):
        '''
        Constructor
        '''
        tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Google Places Scrapper")       
        self.parent.grid_rowconfigure(1,weight=1)
        self.parent.grid_columnconfigure(1,weight=1)
        self.parent.config(background="lavender")


        # Define the different GUI widgets
        self.dose_label = tkinter.Label(self.parent, text = "Enter Your Query:")
        self.dose_entry = tkinter.Entry(self.parent, width =90)
        self.dose_label.grid(row = 0, column = 0, sticky = tkinter.W)
        self.dose_entry.grid(row = 0, column = 1)

        self.modified_label = tkinter.Label(self.parent, text = "Enter City:")
        self.modified_entry = tkinter.Entry(self.parent, width =90)
        self.modified_label.grid(row = 1, column = 0, sticky = tkinter.W)
        self.modified_entry.grid(row = 1, column = 1)

        self.submit_button = tkinter.Button(self.parent,width=10, text = "Fetch", command = self.update_status)
        self.submit_button.grid(row = 2, column = 3, sticky = tkinter.W)

        self.more_button = tkinter.Button(self.parent, width=10, text = "Add More", command = self.kain)
        self.more_button.grid(row = 1, column = 3, sticky = tkinter.W)
        
        self.exit_button = tkinter.Button(self.parent, width=10, text = "Exit", command = self.parent.quit)
        self.exit_button.grid(row = 0, column = 3)

        
        
        # Set the treeview
        self.tree = ttk.Treeview( self.parent, columns=('Phone','Ratings','website','Address'),height=25)
        self.tree.heading('#0', text='Name')
        self.tree.heading('#1', text='Phone')
        self.tree.heading('#2', text='Ratings')
        #self.tree.heading('#3', text='Googlemaps')
        self.tree.heading('#3', text='website')
        self.tree.heading('#4', text='Address')
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        #self.tree.column('#3', stretch=tkinter.YES)
        self.tree.column('#3', stretch=tkinter.YES)
        self.tree.column('#4', stretch=tkinter.YES)
        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # Initialize the counter
        self.i = 0


    def insert_data(self):
        """
        Insertion method.
        """
        for l in range(10):
            print(l)
            self.treeview.insert('', 'end', text="Item_"+str(self.i), values=(self.dose_entry.get()+" mg", self.modified_entry.get()))
            self.update()
            time.sleep(2)
        # Increment counter
        self.i = self.i + 1

    def kain(self):
        process = Process(target=child_process)
        process.start()
                
    def update_status(self):
        #try:
            #urlopen('http://216.58.192.142', timeout=1)
        #except:
            #pymsgbox.alert('Please Check Your Internet Connection.', 'Alert')
            #exit(-1)
        search = self.dose_entry.get()
        city = self.modified_entry.get()
        
        unique_id = search.replace(' ', '-')
        
        fields = ['SrNo', 'Name','Phone', 'Rating','Website', 'Address','city','GoogleMaps']

        out_file = open(str(unique_id)+'.csv','w',encoding='utf-8')
        csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)
        dict_service = {}
                                

        dict_service['SrNo'] = 'Sr. No.'
        dict_service['Name'] = 'Name'
        dict_service['Phone'] = 'Phone'
        dict_service['Rating'] = 'Rating'
        dict_service['Website'] = 'Website'
        dict_service['Address'] = 'Address'
        dict_service['city'] = 'city'
        dict_service['GoogleMaps'] = 'GoogleMaps'


        with open(str(unique_id)+'.csv', 'a',encoding='utf-8') as csvfile:
             filewriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fields)
             filewriter.writerow(dict_service)
             csvfile.close()
             #Write row to CSV
             csvwriter.writerow(dict_service)
        
        def extrapolate_pagination(driver,ity):
            print("bhau bhai")
            
            try:
                button = driver.find_element_by_xpath("//*[@id='n7lv7yjyC35__section-pagination-button-next']")
                button.click()
            except:
                traceback.print_exc()
            time.sleep(10)
            elements = driver.find_elements_by_class_name("section-result")
            #bar = Bar('Processing', max=len(elements))
            nElement = len(elements)
            for index in range(nElement+1):
                    #bar.next()
                    extrapolate_date(elements,index,driver,city)
                    try:
                            back = driver.find_element_by_xpath("//*[@class='section-back-to-list-button blue-link noprint']")
                            back.click()
                            time.sleep(5)
                            elements = driver.find_elements_by_class_name("section-result")
                            
                    except:
                            print('Finish')
                            quit()
            #bar.finish()
    
        #!/usr/bin/env python
        # -*- coding: utf-8 -*-
        def extrapolate_gmaps(search,city):
                city = city.upper()
                driver = webdriver.Firefox(executable_path='./geckodriver')
                #driver.set_window_size(1120, 550)
                try:
                        driver.get("https://www.google.com/maps/")
                except:
                        driver.save_screenshot('err.png')
                driver.save_screenshot('screenshot.png')
                #assert "Google Maps" in driver.title

                elem = driver.find_element_by_xpath("//*[@id='searchboxinput']")
                #elem.send_keys(search)
                elem.send_keys(search)
                #ristorante torino
                #elem.send_keys("pycon")
                elem.send_keys(Keys.RETURN)
                time.sleep(5)
                #elem.clear()
                elements = driver.find_elements_by_class_name("section-result")

                #bar = Bar('Processing', max=len(elements))
                nElement = len(elements)
                for index in range(nElement+1):
                        #bar.next()
                        extrapolate_date(elements,index,driver,city)
                        back = driver.find_element_by_xpath("//*[@class='section-back-to-list-button blue-link noprint']")
                        back.click()
                        time.sleep(3)
                        elements = driver.find_elements_by_class_name("section-result")
                #bar.finish()

                assert "No results found." not in driver.page_source

        def extrapolate_date(elements,index,driver,city):
                if index == len(elements):
                        extrapolate_pagination(driver,city)
                print("")
                print(index)
                element = elements[index]
                
                try:
                        name = element.find_element_by_class_name('section-result-title').text
                        #print(name)
                        name = name.strip()
                        name = name.replace("\"","\'")
                except:
                        traceback.print_exc()
                        name = ""

                try:
                        ratings = element.find_element_by_class_name('cards-rating-score').text
                        #print(ratings)
                        ratings = ratings.strip()
                        ratings = ratings.replace("\"","\'")
                except:
                        traceback.print_exc()
                        ratings = ""
                        
                element.click()
                time.sleep(3)
                        
                try:
                        info = driver.find_elements_by_class_name("section-info-text")
                except:
                        traceback.print_exc()
                try:
                        address = info[0].text
                        googlemaps= info[1].text
                        website = info[2].text
                        phone = info[3].text
                        website_two = website.replace(' ','')
                        phone_two = phone.replace(' ','')
                        address = address.strip()
                        address = address.replace("\"","\'")

                        if website_two.isdigit():
                            phone_final = website
                            website = ' '
                        else:
                            try:
                                website = website.replace('Open now:','')
                            except:
                                website = website
                                

                        if phone_two.isdigit():
                            phone = phone
                        elif website_two.isdigit():
                            phone = phone_final                            
                        else:
                            phone = ' '
                            
                            
                except:
                        traceback.print_exc()
                        address = ""
                
                try:
                        site = driver.find_element_by_css_selector("a[data-attribution-url]")
                        site = site.get_attribute('data-attribution-url')
                        #print(site)
                        site = site.strip()
                        site = site.replace("\"","\'")
                except:
                        traceback.print_exc()
                        site = ""
                        
                            
                try:
                        self.treeview.insert('', 'end', text=str(self.i)+" : "+str(name), values=(phone,ratings,website,address))
                        self.update()
                except:
                        traceback.print_exc()
                        
                self.i = self.i + 1
                dict_service = {}
                dict_service['SrNo'] = str(self.i)
                try:
                    try:
                        dict_service['Name'] = name
                    except:
                        dict_service['Name'] = 'not found'
                    try:
                        dict_service['Phone'] = phone
                    except:
                        dict_service['Phone'] = 'not found'
                    try:
                        dict_service['Rating'] = ratings
                    except:
                        dict_service['Rating'] = 'not found'
                    try:
                        dict_service['GoogleMaps'] = googlemaps
                    except:
                        dict_service['GoogleMaps'] = 'not found'
                    try:
                        dict_service['Website'] = website
                    except:
                        dict_service['Website'] = 'not found'
                    try:
                        dict_service['Address'] = address
                    except:
                        dict_service['Address'] = 'not found'

                    try:
                        dict_service['city'] = self.modified_entry.get()
                    except:
                        dict_service['city'] = ' '

                    print(dict_service)
                    
                    with open(str(unique_id)+'.csv', 'a',encoding='utf-8') as csvfile:
                        filewriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fields)
                        filewriter.writerow(dict_service)
                    csvfile.close()
                except:
                    traceback.print_exc()
                #driver.close()
        extrapolate_gmaps(search,city)

def main():
    root=tkinter.Tk()
    d=Begueradj(root)
    root.mainloop()

def child_process():
    os.startfile("GoogleGuiServer.exe")
    
if __name__=="__main__":
    main()


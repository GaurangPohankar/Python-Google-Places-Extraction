from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common import utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import codecs
import traceback
import re
from time import sleep
from progress.bar import Bar
import sqlite3.dbapi2 as sqlite3

def extrapolate_pagination(driver,city):
	button = driver.find_element_by_class_name("section-pagination-button-next")
	print("bhau bhai")
	button.click()
	time.sleep(5)
	elements = driver.find_elements_by_class_name("section-result")
	bar = Bar('Processing', max=len(elements))
	nElement = len(elements)
	for index in range(nElement+1):
		bar.next()
		extrapolate_date(elements,index,driver,city)
		try:
			back = driver.find_element_by_xpath("//*[@class='section-back-to-list-button blue-link noprint']")
			back.click()
			time.sleep(5)
			elements = driver.find_elements_by_class_name("section-result")
			time.sleep(10)
		except:
			print('Finish')
			quit()
	bar.finish()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def extrapolate_gmaps(search,city):
	city = city.upper()
	driver = webdriver.Firefox(executable_path='./geckodriver')
	driver.set_window_size(1120, 550)
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
	time.sleep(10)
	bar = Bar('Processing', max=len(elements))
	nElement = len(elements)
	for index in range(nElement+1):
		bar.next()
		extrapolate_date(elements,index,driver,city)
		back = driver.find_element_by_xpath("//*[@class='section-back-to-list-button blue-link noprint']")
		back.click()
		time.sleep(5)
		elements = driver.find_elements_by_class_name("section-result")
		time.sleep(10)
	bar.finish()

	assert "No results found." not in driver.page_source

def extrapolate_date(elements,index,driver,city):
	if index == len(elements):
		extrapolate_pagination(driver,city)
	print("")
	print(index)
	element = elements[index]
	
	try:
		name = element.find_element_by_class_name('section-result-title').text
		print(name)
		name = name.strip()
		name = name.replace("\"","\'")
	except:
		traceback.print_exc()
		name = ""

	try:
		ratings = element.find_element_by_class_name('cards-rating-score').text
		print(ratings)
		ratings = ratings.strip()
		ratings = ratings.replace("\"","\'")
	except:
		traceback.print_exc()
		ratings = ""
	element.click()
	time.sleep(5)
		
	try:
		info = driver.find_elements_by_class_name("section-info-text")
	except:
		traceback.print_exc()
	try:
		address = info[0].text
		print(address)
		print(info[1].text)
		print(info[2].text)
		print(info[3].text)
		address = address.strip()
		address = address.replace("\"","\'")
	except:
		traceback.print_exc()
		address = ""
	
	try:
		site = driver.find_element_by_css_selector("a[data-attribution-url]")
		site = site.get_attribute('data-attribution-url')
		print(site)
		site = site.strip()
		site = site.replace("\"","\'")
	except:
		traceback.print_exc()
		site = ""
	
'''
	try:
		openEnd = driver.find_element_by_xpath("//*[@class='section-info-dropdown-button maps-sprite-pane-info-arrowup noprint']")
		openEnd.click()
		time.sleep(5)
		timeString = driver.find_element_by_xpath("//*[@class='section-info-dropdown-container']")
		timeString = timeString.find_elements_by_tag_name("tr")
		week = ""
		for times in timeString:
			timesName = times.find_element_by_tag_name("th").text
			print(timesName)
			timesValue = times.find_element_by_tag_name("td").text
			timesValue = timesValue.strip()
			print(timesValue)
			day = timesName+" : "+timesValue
			if week == "":
				week = day
			else:
				week = week+" , "+day
		time.sleep(5)
	except:
		traceback.print_exc()
		week = ""

	query = 'insert into negoziante (`name`,`address`,`site`,`phone`,`openEnd`,`city`) values ("%s","%s","%s","%s","%s","%s")'%(name,address,site,phone,week,city)
	# Save (commit) the changes
	c.execute(query)
	conn.commit()
	c.close()
	conn.close()
	'''
	#driver.close()
search = input("search: ")
city = input("city: ")
extrapolate_gmaps(search,city)
user_choice = input('Please click ENTER button to close application')
if not user_choice:
    print ("ABORTED")
    quit()
print("Finish")


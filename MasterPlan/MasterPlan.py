from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient()
db = client.Hockey
teams = db.Teams


url = "http://www.nhl.com/ice/teams.htm?navid=nav-tms-main"
r = requests.get(url)
soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"class":"teamContainer"})

#Gather Team data
for item in g_data:
    print ('--------------WEST-CONF-------------------')
    westConf = item.contents[0]
    print ('**Pacific Div**')
    pacDiv = westConf.find_all("div", {"class":"pacific"})
    pacplaces = pacDiv[0].find_all("span", {"class":"teamPlace"})
    paccommons = pacDiv[0].find_all("span", {"class":"teamCommon"})
    x = 0
    wc_pacplace = {}
    for pacplace in pacplaces:
        #print pacplace.text
        wc_pacplace[x] = pacplace.text
        x = x + 1

    y = 0
    wc_paccommon = {}
    for paccommon in paccommons:
        #print paccommon.text
        wc_paccommon[y] = paccommon.text
        y = y + 1

    print ('**Central Div**')
    cenDiv = westConf.find_all("div", {"class":"central"})
    cenplaces = cenDiv[0].find_all("span", {"class":"teamPlace"})
    cencommons = cenDiv[0].find_all("span", {"class":"teamCommon"})
    wc_cenplace = {}
    i = 0
    for cenplace in cenplaces:
        #print cenplace.text
        wc_cenplace[i] = cenplace.text
        i = i + 1

    wc_cencommon = {}
    j = 0
    for cencommon in cencommons:
        #print cencommon.text
        wc_cencommon[j] = cencommon.text
        j = j + 1

    print ('--------------EAST-CONF-------------------')
    eastConf = item.contents[1]
    print ('**Atlantic Div**')
    atlDiv = eastConf.find_all("div", {"class":"atlantic"})
    atlplaces = atlDiv[0].find_all("span", {"class":"teamPlace"})
    atlcommons = atlDiv[0].find_all("span", {"class":"teamCommon"})
    ec_atlplace = {}
    a = 0
    for atlplace in atlplaces:
        #print atlplace.text
        ec_atlplace[a] = atlplace.text
        a = a + 1

    ec_atlcommon = {}
    b = 0
    for atlcommon in atlcommons:
        #print atlcommon.text
        ec_atlcommon[b] = atlcommon.text
        b = b + 1

    print ('**Metropolitan Div**')
    metDiv = eastConf.find_all("div", {"class":"metropolitan"})
    metplaces = metDiv[0].find_all("span", {"class":"teamPlace"})
    metcommons = metDiv[0].find_all("span", {"class":"teamCommon"})
    ec_metplace = {}
    c = 0
    for metplace in metplaces:
        #print metplace.text
        ec_metplace[c] = metplace.text
        c = c + 1

    ec_metcommon = {}
    d = 0
    for metcommon in metcommons:
        #print metcommon.text
        ec_metcommon[d] = metcommon.text
        d = d + 1

#Insert Western Conference teams into database
for x in range(0,7):
    teampac = {"TeamCity":wc_pacplace[x],
               "TeamName":wc_paccommon[x],
               "Conference":"Western",
               "Division":"Pacific"}

    team_id = teams.insert_one(teampac).inserted_id

    teamcen = {"TeamCity":wc_cenplace[x],
               "TeamName":wc_cencommon[x],
               "Conference":"Western",
               "Division":"Central"}

    team_id = teams.insert_one(teamcen).inserted_id

#Insert Eastern Conference teams into database
for x in range(0,8):
    teamatl = {"TeamCity":ec_atlplace[x],
               "TeamName":ec_atlcommon[x],
               "Conference":"Eastern",
               "Division":"Atlantic"}

    team_id = teams.insert_one(teamatl).inserted_id

    teammet = {"TeamCity":ec_metplace[x],
               "TeamName":ec_metcommon[x],
               "Conference":"Eastern",
               "Division":"Metropolitan"}

    team_id = teams.insert_one(teammet).inserted_id

#Display team data
print ('My wc_pacplace var:  ')
for k, v in wc_pacplace.iteritems():
    print (k,v)
print ('My wc_paccommon var:  ')
for k, v in wc_paccommon.iteritems():
    print (k,v)
print ('My wc_cenplace var:  ')
for k, v in wc_cenplace.iteritems():
    print (k,v)
print ('My wc_cencommon var:  ')
for k, v in wc_cencommon.iteritems():
    print (k,v)

print ('My ec_atlplace var:  ')
for k, v in ec_atlplace.iteritems():
    print (k,v)
print ('My ec_atlcommon var:  ')
for k, v in ec_atlcommon.iteritems():
    print (k,v)
print ('My ec_metplace var:  ')
for k, v in ec_metplace.iteritems():
    print (k,v)
print ('My ec_metcommon var:  ')
for k, v in ec_metcommon.iteritems():
    print (k,v)


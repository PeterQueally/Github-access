from github import Github, BadCredentialsException
import csv
import webbrowser
from itertools import zip_longest


loggedIn = False
while not loggedIn:
    try:
        username = input("Github username: ")
        password = input("Github password: ")
        gAccess = Github(username, password)
        user = gAccess.get_user(login = username)
        loggedIn = true
        
    except BadCredentialsException:
        print("Incorrect username or password!")


print("Generating data!")
# This code gets the top 10 developers in the React repo of facebook and converts it to a csv file.
list1 = []
list2 = []

repository = user.get_repo("react")
line = 0
for contributors in repository.get_stats_contributors():
    if line >= 91:
        list1.append(contributors.author.login)
        list2.append(contributors.total)
    line +=1
d = [list1, list2]
export_data = zip_longest(*d, fillvalue = '')
with open('Data.csv', 'w', newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Developer", "Commits"))
      wr.writerows(export_data)
myfile.close()

webbrowser.open("DisplaySocialGraphInfo.html")
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

list = []
for repository in user.get_repos():
        list.append(repo.language)

dicta = {c: 0 for c in list}
for items in list:
    dicta[items] += 1
totalno = sum([dicta[x] for x in dicta])
for x in dicta:
    if x == "Jupyter Notebook":
        dicta["Jupyter"] = dicta["Jupyter Notebook"]
        del dicta["Jupyter Notebook"]
    if x is None:
        dicta["None"] = dicta[None]
        del dicta[None]
d = [[x for x in dicta], [dicta[x]/totalno for x in dicta]]

export_data = zip_longest(*d, fillvalue = '')
with open('Data2.csv', 'w', newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Language", "Frequency"))
      wr.writerows(export_data)
myfile.close()

webbrowser.open("DisplaySocialGraphInfo2.html")
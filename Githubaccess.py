from github import Github, BadCredentialsException

loggedIn = false;
while not loggedIn:
    try:
        username = input("Github username: ")
        password = input("Github password: ")
        gAccess = Github(username, password)
        user = gAccess.get_user(login = username)
        loggedIn = true
        
    except BadCredentialsException:
        print("Incorrect username or password!")
        
for repository in user.get_repos():
    print("[" + repository.name + "] = repository name")
    print("[" + repository.language + "] = main language used")
    for commits in repository.get_commits():
        print("The commit " + commits.sha + " was created at [" + str(commits.commit.author.date) + "]")
    print("\n")
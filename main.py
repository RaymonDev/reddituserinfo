
import praw #https://praw.readthedocs.io/en/latest/
import datetime
import os

def title():
    os.system("cls")
    print("\n--------------------------------------------------------------------------------")
    print("\n                               *@@@@@@@@@@@@@@@@&.                              ")
    print("\n                        ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        ")
    print("\n                    #@@@@@@@@@@&.               *@@@@@@@@@@@,                   ")
    print("\n                 @@@@@@@@%                            .@@@@@@@@#                ")
    print("\n              #@@@@@@&                                    .@@@@@@@.             ")
    print("\n            &@@@@@@                                          ,@@@@@@*           ")
    print("\n          %@@@@@#                   @@@@@@/                     @@@@@@.         ")
    print("\n         @@@@@%                    @@@@@@@@                       @@@@@@        ")
    print("\n       /@@@@@                       @@@@@@,                        /@@@@@       ")
    print("\n      /@@@@@                                                        .@@@@@      ")
    print("\n      @@@@@                                                          .@@@@@     ")
    print("\n     @@@@@                      @@@@@@@@@@@@@                         %@@@@/    ")
    print("\n    ,@@@@&                      #@@@@@@@@@@@@                          @@@@@    ")
    print("\n    #@@@@/                              @@@@@                          @@@@@    ")
    print("\n    &@@@@,                              @@@@@                          %@@@@.   ")
    print("\n    (@@@@(                              @@@@@                          @@@@@    ")
    print("\n    .@@@@&                              @@@@@                          @@@@@    ")
    print("\n     @@@@@.                             @@@@@                         @@@@@*    ")
    print("\n      @@@@@                             @@@@@                        *@@@@@     ")
    print("\n      ,@@@@@                            @@@@@                       *@@@@@      ")
    print("\n       ,@@@@@,                          @@@@@                      &@@@@@       ")
    print("\n         @@@@@@                 @@@@@@@@@@@@@@@@@@@@@,           .@@@@@%        ")
    print("\n          /@@@@@@               /@@@@@@@@@@@@@@@@@@@&          .@@@@@@          ")
    print("\n            %@@@@@@,                                         #@@@@@@.           ")
    print("\n              *@@@@@@@*                                   &@@@@@@@              ")
    print("\n                 &@@@@@@@@/                           &@@@@@@@@,                ")
    print("\n                    ,@@@@@@@@@@@@/            .#@@@@@@@@@@@@                    ")
    print("\n                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                        ")
    print("\n                                *&@@@@@@@@@@@@@%,                               ")
    print("\n Coded by: RaymonDev")
    print("\n Powered by: PRAW (https://praw.readthedocs.io/en/latest/)")
    print("\n--------------------------------------------------------------------------------")







#authorise the bot, read only mode
reddit = praw.Reddit(
    client_id="YOUR CLIENT ID",
    client_secret="YOUR SECRET CLIENT CODE",
    user_agent="testscript by u/Raymon22",
)

#displays the title
title()

redditorname = input("Type the Redditor username: ") #gets the redditor name from the user
print("\n-----------------------------------------")
print("\n - Complete (or c) = This option displays information about the posts, the subreddits, and the user ")
print("\n - Rapid (or r) = This option displays information about the user and all the subreddits they have posted in")
print("\n-----------------------------------------")
elec = input("\nChoose and option (c/r): ")
print("\n-----------------------------------------")

redditor = reddit.redditor(redditorname) #name of the Redditor that we are looking for

#gets the IDs of the posts of user
submisions = list(redditor.submissions.new(limit=None))
#print(submisions)

idstring = str(submisions) #transform to string


#This fragment of code "cleans" the sting, leaving only the ids
idstring = idstring.lower() #lowes all the string
idstring = idstring.replace("submission", "")
idstring = idstring.replace("(", "")
idstring = idstring.replace(")", "")
idstring = idstring.replace("id=", "")
idstring = idstring.replace('\'', "")
idstring = idstring.replace('[', "")
idstring = idstring.replace(']', "")
idstring = idstring.replace(" ", "")
#print(idstring)


array_id = idstring.split(",") #splits the string and stores that string into an array/list
#print(array_id) #shows the array/list

#process and clear the trophies of the user

trophiestring = str(redditor.trophies())
trophiestring = trophiestring.replace("[", "")
trophiestring = trophiestring.replace("]", "")
trophiestring = trophiestring.replace("Trophy", "")
trophiestring = trophiestring.replace("(", "")
trophiestring = trophiestring.replace(")", "")
trophiestring = trophiestring.replace("name=", "")
trophiestring = trophiestring.replace("\'", "")

if trophiestring == "":
    trophiestring = "No trophies"

#displays the title
title()

#displays the user info
print("\nUser Info: ")
print("\n - Username: " + str(redditorname))
print("\n - Account created the: " + str(datetime.datetime.utcfromtimestamp(redditor.created_utc).strftime('%d-%m-%Y at %H:%M'))) #transforming the utc time to comprensive text
print("\n - Karma of the user: " + str(redditor.link_karma))
print("\n - Comment Karma: " + str(redditor.comment_karma))
print("\n - Is a Reddit employee: " + str(redditor.is_employee))
print("\n - Is a mod: " + str(redditor.is_mod))
print("\n - Trophies: " + str(trophiestring))
print("\n------------------------------------------------")

if elec == "c":

    #for every id in the array previously made (line 88)
    for id in array_id:
        submission = reddit.submission(id=id) #get information of post from id
        print("\n-----------------------------------------------------")
        print("\n* Post Subreddit: " + submission.subreddit_name_prefixed)
        print("\n\t- Title: " + str(submission.title))
        print("\n\t- Description: " + str(submission.selftext))
        print("\n\t- Upvotes: " + str(submission.ups))
        print("\n\t- Downvote: " + str(submission.downs))
        print("\n\t- Time published: " + str(
            datetime.datetime.utcfromtimestamp(submission.created).strftime('%d-%m-%Y at %H:%M')))
        print("\n\t- NSFW: " + str(submission.over_18))
        print("\n\t- Archived: " + str(submission.archived))
        print("\n\t- Url: " + str(submission.url))
        print("\n-----------------------------------------------------")

elif elec == "r":

    for id in array_id:
        submission = reddit.submission(id=id)  # gets infromation about the post
        print(submission.subreddit_name_prefixed)  # shows the subreddits

else:
    print("Wrong letter, try again.") #checks for a wrong letter

input("Press Enter to continue...")
exit()

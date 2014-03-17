#posting latest blog post on FB
import requests
import json
import time
import webbrowser
import feedparser

d = feedparser.parse(r'/Users/aregee/Workspace/myblog/diy/feeds/all.atom.xml')

def getaccesstoken():
    """
    getaccesstoken()->ACCESS_TOKEN
    Presents user with the choice of creating a token or supplying
    one to the script.
    """
    print ("The script needs your ACCESS TOKEN.\n"
           "What would you like to do?\n"
           "1. Generate a new TOKEN.\n"
           "2. Supply one (if you know how to generate it).\n")

    choice = raw_input("Choice (1 or 2) ? :")
    if int(choice) == 2:
        access_token = raw_input("\nEnter the TOKEN string: ")
    else:
        print ("To generate your token the script needs access to your feeds"
               "and publishing\npermissions. Don't worry the script doesn't "
               "store anything or spam your wall!\nGo to the links which will"
               "open in your browser shortly and give the permissions\nto read"
               " your data, once you give that permission another link will "
               "open which \nhas your token, the token is a long string and "
               "looks something like this\nCAACEdEose0.......cBABKNtliuHS7.\n"
               "Copy it and paste it below.")
    print "\nOpening links now..."
    webbrowser.open("https://www.facebook.com/dialog/oauth?"
                    "response_type=token&client_id=145634995501895&"
                    "redirect_uri=http://developers.facebook.com/tools/"
                    "explorer/callback&scope=user_birthday,publish_actions"
                    ",read_stream")


    time.sleep(10)
    webbrowser.open("http://developers.facebook.com/tools/explorer")
    access_token = raw_input("\nEnter the TOKEN string obtained from API "
                             "explorer page: ")
    return access_token



def postFeed(TOKEN):

    url = 'https://graph.facebook.com/me/feed'
    payload = {
        'access_token': TOKEN ,
        'link': d.entries[0].link,
        'description': d.entries[0].title,
        'caption': d['feed']['title']
    }
    r = requests.post(url, payload)

    print "Status : %s Headers: %s " % (r.status_code, r.headers, )

if __name__ == '__main__':
    TOKEN = getaccesstoken()
    postFeed(TOKEN)

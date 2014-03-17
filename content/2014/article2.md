Title: Python Script to post latest blog post on facebook 
Date: 2014-03-17 12:30
Tags: Pelican is awesome, Facebook, pelican
slug: pelican-facebook-post
Author: aregee
Summary: A quick and dirty python script, that post the link to your latest blog post to your facebook feed.

##Problem at Hand
I have migrated my blog to pelican couple of months back and have spent some time with pelican now. I feel safe to say that pelican has been by far the most functional static site generator with a bustling community.
Pelican offers lots of functionalities out of the box , however I missed ability to post the link to my latest blog on social media sites.
Life has been pretty busy and I have been trying to get accustomed to a new job and in all this mess , I had screwed up my pelican configuration and my OpenShift DIY cartridge where I host this blog (Bunch of Static files).

### Python to rescue 

I took a very siple approach , utilizing the graph apis from facebook.
Below is a snippet of code that does the job of posting the link with description, link, caption to your facebook feed.

    :::python
        def postFeed(TOKEN):

            url = 'https://graph.facebook.com/me/feed'
            payload = {
                'access_token': TOKEN ,
                'link': d.entries[0].link,
                'description': d.entries[0].summary,
                'caption': d.entries[0].title
            }
            r = requests.post(url, payload)

            print "Status : %s Headers: %s " % (r.status_code, r.headers, )

        if __name__ == '__main__':
            TOKEN = getaccesstoken()
            postFeed(TOKEN) 

### How to fetch latest post 

This part was no brainer, pelican provides ability to generate atom feed and all I need to do was to check the atom feed on every build for the latest entry.
I used couple of dependencies for this though, like [requests](http://docs.python-requests.org/en/latest/) for making HTTP request to Graph APIs, [feedparser](http://packages.python.org/feedparser/) to parse XML in atom feed.
Both could be installed with pip.

Lets take a look at the code snippet that will explain this part:

    :::python 
        d = feedparser.parse(r'/Users/aregee/Workspace/rahulgaur/output/feeds/all.atom.xml')

        
Here is an example of how my XML feed looks like 

    :::xml
        <feed xmlns="http://www.w3.org/2005/Atom">
        <title>rahulgaur.info</title>
        <link href="http://myblog-rahulgaur.rhcloud.com/" rel="alternate"/>
        <link href="http://myblog-rahulgaur.rhcloud.com/feeds/all.atom.xml" rel="self"/>
        <id>http://myblog-rahulgaur.rhcloud.com/</id>
        <updated>2014-03-17T12:30:00+05:30</updated>
        <entry>
        <title>Python Script to post latest blog post on facebook</title>
        <link href="http://myblog-rahulgaur.rhcloud.com/pelican-facebook-post.html" rel="alternate"/>
        <updated>2014-03-17T12:30:00+05:30</updated>
        <author>
        <name>aregee</name>
        </author>
        <id>
        tag:myblog-rahulgaur.rhcloud.com,2014-03-17:pelican-facebook-post.html
        </id>
        <summary type="html">
        <h2>Problem at Hand</h2> <p>I have migrated my blog to pelican couple of months back and have spent some time with pelican now. I feel safe to say that pelican has been by far the most functional static site generator with a bustling community. Pelican offers lots of functionalities out of the box , however I missed ability to post the link to my latest blog on social media sites. Life has been pretty busy and I have been trying to get accustomed to a new job and in all this mess , I had screwed up my pelican configuration and my OpenShift DIY cartridge where I host this blog (Bunch of Static files).</p>  
        </pre></div>
        </summary>
        <category term="Pelican is awesome"/>
        <category term="Facebook"/>
        <category term="pelican"/>
        </entry>


So, feedparser simplyfies the job and parse the data into the variable *d* .Now what I need to do is to post the latest blog entry to facebook.
I did something like this.
    
    :::python 

        d.entries[0] 
        
Out of all the entries , d.entries[0] will fetch the most recent blog entry.
This is exactly what we need to post of Facebook.


### Complete Code

Below is the complete code, there is another method getaccesstoken.This method invokes the browser at the given URL to and initially this will ask you to provide permission access.Once you have given the permission , the script invokes another URL in your webbrowser.
This page should contain your acces token, copy the token and supply it in the input field on the console.
The script should be able to post your most recent blog entry to your facebook feed.

    :::python 
        #posting latest blog post on FB
        import requests
        import json
        import webbrowser
        import feedparser

        d = feedparser.parse(r'/Users/aregee/Workspace/rahulgaur/output/feeds/all.atom.xml')

        def getaccesstoken():
            """
            getaccesstoken()->ACCESS_TOKEN
            Presents user with the choice of creating a token or supplying
            one to the script which it uses to create post
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
            webbrowser.open("http://developers.facebook.com/tools/explorer")
            access_token = raw_input("\nEnter the TOKEN string obtained from API "
                                     "explorer page: ")
            return access_token



        def postFeed(TOKEN):

            url = 'https://graph.facebook.com/me/feed'
            payload = {
                'access_token': TOKEN ,
                'link': d.entries[0].link,
                'description': d.entries[0].summary,
                'caption': d.entries[0].title
            }
            r = requests.post(url, payload)

            print "Status : %s Headers: %s " % (r.status_code, r.headers, )

        if __name__ == '__main__':
            TOKEN = getaccesstoken()
            postFeed(TOKEN)
            

### Use this script with fabric

Pelican provides the ability to generate fabfile or makefile for automated deployment , I have used fabric to run this script.

I have added the following method to my fabfile.
Now in order to invoke the script after every new build or post addition.

>fab build deploy facebook

    :::python 
       def facebook():
            local('python fb_extn.py') 







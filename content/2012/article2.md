Title: Gearing up to blog !
Date: 2012-11-19 16:48:01
Tags:life
Slug: new-start
Summary:I am visiting my parents in "Guwahati",My dad's currently has a job here.Guwahati does offer serene and scenic *beauties* Natural & "ManMade".Exotic to be honest,but I don't have any friends here and one can't soak in so many pleasing *views* all the time.
I needed something to kill time and get my mind of some *love life* troubles. 
I admit,I have been meaning to build my blog for a while,even tried out with Django, but something was giving me a *feel* that this is not what I need for my blog.I needed something more light wait and fast.



I am visiting my parents in "Guwahati",My dad's currently has a job here.Guwahati does offer serene and scenic *beauties* Natural & "ManMade".Exotic to be honest,but I don't have any friends here and one can't soak in so many pleasing *views* all the time.
I needed something to kill time and get my mind of some *love life* troubles. 
I admit,I have been meaning to build my blog for a while,even tried out with Django, but something was giving me a *feel* that this is not what I need for my blog.I needed something more light wait and fast.Something which would cost me pretty less to mantain.

So here it is **My Birthday Gift** to my self.It's my Birthday and my blog is up and running.It's nearly complete there of tons of shortcoming so you would be seeing some frequent changes .

I am not a designer and I barely know any photoshop skills to design headers.My knowledge of html and css is also kind of bit limited.So,what I did I wrote this thing with [Hyde][] by reading the source of the existing Hyde projects and Goggling out nicks& nacks.


<hr></hr>


###What is Hyde


Hyde is a "static site generator" written in [Python][],similar to [Jekyll][].I have been seeing couple of people I know rewriting their blogs with Hyde.



Hit the link above to know more about Hyde.

[Django]: http://www.djangoproject.com
[Python]: http://www.python.org
[Hyde]: http://hyde.github.com/
[Jekyll]: http://jekyllrb.com/


There are plenty of reasons,but mainly Hyde offered everything I needed at the moment to get a decent site up and running.


- **Less Memory Space **:
 I am hosting this blog on Openshift and I didn't needed a *very Functional* Django based blog.Eventhough with Django ,I could write a webapp and deploy it on the Cloud.Well Django sites take roughly 20mb of the memory on the server.
Hyde Generated sites don't take plenty of the memory on my Cloud Instance and allows me to save my resources so I can stage & scale my other webapps.
So , I didn't need all of the fabulous features that Django has to offer and I didn't wanted Django to eat up my cloud resources unnecessarily.Switiching to Static seems like a valid option .

- **Easier to Maintain **:
Another thing about hyde is , I don't have to be connected to internet & login to admin console like wordpress and similar to edit blog entries.
With Hyde , all I need to do is to create a new file or edit it any time and anywhere as long as I have access to my laptop which is always.
When I have the access to the Internet, all I need to do is to run my deploy script and woha it's done.
I can edit the articles as long as I want and markdown gives plenty of freedom.


- **Easy to take backup ** : 
One more advantage of Hyde is that the site structure is a lot easier to take backups.It's there on the Openshift,deployed with git on my local machine and github.
It's easier to take backup as it's just bunch of static pages at the end of the day ..!


So, that pretty much sums up everything about Hyde and my new blog.
There are very few documentation on developing with hyde so I will try to come up with a post covering development and deployment.
I have deployed this on [OpenShift][] & I would cover that in my post 

[OpenShift]: http://openshift.redhat.com


##Aregee##
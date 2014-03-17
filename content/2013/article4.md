Title: My takeaways from GSoC 2013
Date: 2013-09-27 15:02
Tags: opensource,gsoc,python,sugarlabs,moksaya
Slug: gsoc
Author: Aregee
Summary: I had a great learning experience and I was gald to be a part of GSoC program with SugarLabs.Over the course of four months I learned great new skills and I worked with some very amazing and brilliant people.

Content:
I hard to beleive but for the last four months I had rarely went out , I do had lots of chances to leave home and go out party with friends but I never liked living my computer alone.

Over the course of last four months I became overly attached to my project and to my workSpace.

![Alt workspace]({filename}/images/workspace.jpg)

So, it looks cool but I plan to make a triple head setup with another LED.
I had a pretty nerdy four months , I had lots of cool gadgets to play with eventhough my project [Moksaya][] pretty much consumed me.
Meanwhile I got a raspberrypi , Nexus 4 and whole lot of other toys to play with.This has been possible mostly because of Google and GSoC program , giving me an opportunity to do what I love and getting paid enough to meet my expenses and needs.

Lets talk about Project [Moksaya][]:
-------------------------------------

This year for GSoC , I submitted two proposals one was for GnuMailMan (Under Python Software Foundation) and the second one being for SugarLabs.
I really wanted to learn more about RESTful architecture and development so both of my proposal had a focus on implementing RESTful interface.
 
I got selected for SugarLabs, where my project was to implement a Project sharing website for Sugar Activities.Kids use Sugar , and they build things , they make cool projects so we started with a goal to implement a platform that will allow them to share their projects , interact with other Sugar Users with comments , follow , likes and project forking.
Typical basics of Social collaboration and sharing.Also the website needs to integerate with the Sugar Operating System , so that kids can share their projects from within the Sugar Activities.

Now the question was how to implent this platform.I had some experience with Django as I have been using it for about a year now , so Django was my choice handsdown.
I had started exploring django [tastypie][] and Django Rest [Framework][] , django based frameworks to develop RESTful interface.
It is pretty simple to roll out the RESTful apis with these frameworks specially if you are using Django ORM for data sources.

I had been reading the [book][] RESTful  Web Services since April of this year.It was recomened me by the developers of GnuMailMan.However , when I started with my project I intented to develop the complete site in Django and I wanted to complete this by the mid term evaluation.That was the plan according to my proposal.

Eventually , I had some discussions with my Mentors Claudia and Martin I came to a conclusion that implementing RESTful interface and then consuming the RESTful apis with JavaScript web app and webservices module in Sugar would provide a way to integerate the APIs into Sugar as well.

Initially I had spent couple of days or maybe a week or two using Django to build a site , using lots of django apps like Django Userena , pinax-scocial apps etcs.I was finding it rather complex and not very much flexible.
 
After Martin's suggestion and also discussing the matter with couple of friends , I went for RESTful interface.My only hesitation regarding RESTful interface was that I had next to no experience with JavaScript.I convinced my self , going the RESTful way will surely provide a better learning curve.I will get to learn more about web services , HTTP protocols and it might present an opertunity to learn JavaScript and heroic framework like  [AngularJs][].

I liked django-rest-framework and I will surely use it sometime soon for a different project , but since this was my first attempt and I felt tasypie was more better documented than the prior.I started with tastypie, designing my models , creating related resources.
I had primarily:
  
  * UserModel
  * ProfileModel
  * ProjectModel
  * LikingModel
  * CommentsModel
  * FollowModel


This is how the Resources were structured  in my JSON response for a typical User profile:

     ::::json
            {
           "about_me": "Oh not it won't happen :0",
           "followers": [
               "aregee"
           ],
           "following": [
               "aregee",
               "kirk",
               "jarvis"
           ],
           "id": 3,
           "language": "en",
           "location": "",
           "mugshot": null,
           "privacy": "registered",
           "projects": [
               {
                   "Likes": 1,
                   "comment": [
                       {
                           "entry": "undefined",
                           "resource_uri": "/api/v1/comment/1/",
                           "text": ":P",
                           "user": "vrinda"
                       }
                   ],
                   "desc": "undefined",
                   "history": "project undefined  created by aregee forked by vrinda ",
                   "id": 4,
                   "resource_uri": "/api/v1/projects/4/",
                   "screenshot": "/media/projects/wb3_1.png",
                   "shared_date": "2013-09-20T19:09:43.084615",
                   "src": "/media/projects/feed__1.py",
                   "title": "undefined",
                   "user": "vrinda"
               }
           ],
           "resource_uri": "/api/v1/profile/3/",
           "user": "vrinda"
       }
   


It was pretty simple at the end of the day , did required some ammount of thinking but frameworks like tastypie does pretty much simplify lots of things.
I will discuss and highlight my development process in seprate parts , for the meanwhile you can check out the live deployment of the web app written with AngularJS [here][] .
The backend or the RESTful server is deployed on OpenShift platform.


###AREGEE###


[book]: http://shop.oreilly.com/product/9780596529260.do
[tastypie]: http://tastypieapi.org/
[Framework]: http://django-rest-framework.org/
[Moksaya]: https://github.com/aregee/moksaya
[here]: http://aregee.github.com/Moksaya-web

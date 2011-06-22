Whiskerboard
============

Whiskerboard is a status board for websites, services and APIs, like Amazon's [AWS status page](http://status.aws.amazon.com/).

It is heavily based on [Stashboard](http://www.stashboard.org/). Unlike Stashboard, it uses vanilla Django, so you aren't stuck using Google App Engine.

Have a look at the demo: [http://whiskerboard.ep.io/](http://whiskerboard.ep.io/).

Quick start guide
-----------------

It's dead quick to get a status board up and running using [http://ep.io/](http://ep.io/). 

Create an application on ep.io then run these two commands, replacing `myamazingboard` with the name of your application: 
    
    $ pip install -r requirements.txt
    $ fab app:myamazingboard deploy

You might need to install [pip](http://www.pip-installer.org/en/latest/installing.html). If you haven't got a virtualenv, you'll need to run it as root too.

Now head over to http://myamazingboard.ep.io/admin/ and login with the account you create when you deployed. You'll want to set the name of your board by clicking on "sites". Edit the single entry called "example.com" and enter a name for your board.

Back on the admin home page, click on "services" and add the things you want to report the status of (website, API etc). To change the status of a service add an event for it.



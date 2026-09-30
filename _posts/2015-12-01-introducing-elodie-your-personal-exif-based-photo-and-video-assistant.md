---
layout: post
title: "Introducing Elodie; Your Personal EXIF-based Photo and Video Assistant"
description: "Elodie is an EXIF-based assistant that files your photos and videos into a predictable structure automatically."
category: articles
logo:  skip
tags: [photo-management]
comments: false
share: true
---

<figure>
	<img src="/images/photos/2015-12-01-introducing-elodie-1.jpg" alt="Banfora Falls. Burkina Faso, Africa.">
	<figcaption>Banfora Falls. Burkina Faso, Africa.</figcaption>
</figure>

*Download* [*Elodie, the EXIF-based photo organizer app*](https://getelodie.com) *I made to manage my photos, and easily replicate the workflow in this post. You can also view the* [*open source command-line version*](https://github.com/jmathai/elodie) *on GitHub.*

<figure>
	<img src="/images/photos/2015-12-01-introducing-elodie-2.jpg" alt="Collecting shells on the beach. Pescadero, California.">
	<figcaption>Collecting shells on the beach. Pescadero, California.</figcaption>
</figure>

I previously wrote about [wanting a workflow which brings sanity to my photo and video library](/articles/understanding-my-need-for-an-automated-photo-workflow/). This post explains my first iteration at a solution which supports that workflow.

I was inspired by [Dave Liggat’s blog post](https://liggat.org/a-robust-photo-workflow/) outlining how he approached a very similar problem as mine. I decided to incorporate his ideas and extend them into something which suited my needs.

I wrote the software and named it Elodie which you can find the [source code for on Github](https://github.com/jmathai/elodie). It’s a work in progress :).

#### Form follows function

Elodie sifts through an entire library of unorganized photos and neatly places them into an organized folder structure. For the sake of simplicity we can refer to this process as *“Elodie applying rules”* to a photo.

<figure>
	<img src="/images/photos/2015-12-01-introducing-elodie-3.png" alt="The basic workflow which Elodie enables. Only the first task is manual.">
	<figcaption>The basic workflow which Elodie enables. Only the first task is manual.</figcaption>
</figure>

Plenty of software exists to organize photos into a folder structure by date but I knew I wanted something more sophisticated than that. I decided on encoding the date, location, title and album from EXIF into the folder structure.

Let’s say Elodie applied rules to an unorganized corpus of photos.

```
├── Unorganized Photos│   ├── IMG_9426.JPG│   └── IMG_9432.JPG
```

She would turn it into something more meaningful.

```
├── 2015-07-Jul│   ├── Mountain View│   │   ├── 2015-07-19_17-16-37-img_9426-walking-around-downtown.jpg│   │   └── 2015-07-24_19-06-33-img_9432-taking-the-caltrain.jpg
```

Besides being a more meaningful representation of the photos and videos themselves this structure will prove extremely valuable as we go along.

#### The file system as a real-time reflection of its contents

<figure>
	<img src="/images/photos/2015-12-01-introducing-elodie-4.png" alt="The Elodie mascot: a cartoon girl with her hair in buns, holding a small chalkboard reading Elodie.">
</figure>

It wasn’t long before I began thinking of the file system as a real-time reflection of the files contained within it. If I add location information to the EXIF of photos taken on my dSLR then the file system should be updated to reflect that. Files should be renamed and moved according to their new meta-data.

[Idempotence](https://en.wikipedia.org/wiki/Idempotence) is a term in computer science which states that the same operation can be safely applied over and over again. Idempotent systems are resilient, predictable and elegant.

By making Elodie’s rules idempotent we could achieve synchronization between the folder structure and the files’ meta-data.

I ran 11,000 photos and videos through Elodie’s rules engine and I got back an organized library of photos. I could add meta-data anywhere it didn’t exist or needed to be changed and Elodie would add it to the EXIF and reorganize the photos accordingly.

#### Giving Elodie a facelift

I never intended on creating a UI for Elodie. My intentions were that she remain *“headless”*. But as the usefulness of the software increased it made sense to have a UI which matched the functionality.

In keeping with the intended simplicity of Elodie I wanted an unobtrusive UI. Something tucked away that I didn’t have to think about opening unless I needed to use it.

I wrapped the command line libraries in a taskbar app. An icon sits silently in the taskbar so you can drag photos over it which reveals a dialog. That dialog lets you quickly and easily batch edit the meta-data on photos. Like everything else that’s happened with Elodie the taskbar app has turned out much better than I originally envisioned.

#### Accounting for photos taken in the future

What about photos taken in the future? I needed an easy way to get them flowing into my organized photo and video library. I knew what I didn’t want. No cables. No slow uploads over the Internet. No “auto backup” of my entire camera roll.

<figure>
	<img src="/images/photos/2015-12-01-introducing-elodie-5.jpg" alt="El Capitan at Yosemite, CA">
	<figcaption>El Capitan at Yosemite, CA</figcaption>
</figure>

That rules out the usual suspects for getting photos off a phone. Fortunately with El Capitan I’m able to AirDrop photos from my iPhone to Macbook. My wife can also AirDrop photos to my Macbook.

AirDrop it is.

Any photo I want to add to my library I can simply AirDrop to my laptop. Anyone else can, in fact, AirDrop photos and videos to my laptop and they are organized into my photo library.

Easy. Fast. Automatic. Built-in.

#### Informing Elodie of new photos to process

AirDrop puts files into your *~/Downloads* folder so that’s a good place to start. Let’s have Elodie do her magic any time new photos or videos show up there. But if we can do this for *~/Downloads* we can do it for any other folder too. Pretty cool.

Elodie is sophisticated enough to not process random images or movies that show up in *~/Downloads*. Your screenshots won’t end up in your library.

I’ve been doing this for a few weeks and it works really well. AirDrop works great and I use it 95% of the time but I found myself in situations where I wanted to offload photos while my laptop wasn’t next to me.

Is that even possible? Glad you asked.

#### Using Elodie with Dropbox or Google Drive

I have Elodie watching *~/Downloads* for new photos and videos so I can use AirDrop. I could just as easily have her watch another folder inside *~/Dropbox* or *~/Google Drive*.

That lets me use their respective mobile app to upload photos from my phone to the cloud and my laptop will eventually sync the files down into the additional folder which Elodie is watching. It works really well because it is completely asynchronous.

Further you can select a folder in your Dropbox or Google Drive as the location which Elodie puts your organized photo library. This gives you a simple offsite backup. You can even use their mobile apps to access your photo library. I originally did this with Dropbox and it worked really well.

#### Using Synology CloudSync for a 3rd backup

You can never have too many backups and one of them should absolutely be in your home. Since I’m sync’ed with a cloud service I can use Synology’s CloudSync program to automatically keep an updated local copy of my entire photo library safe within my home.

<figure>
	<img src="/images/photos/2015-12-01-introducing-elodie-6.jpg" alt="Synology NAS (photo credits, CNET)">
	<figcaption>Synology NAS (photo credits, CNET)</figcaption>
</figure>

With no additional work I obtained three geographically distributed copies of my entire photo library which automatically stays up to date.

#### Bringing my photos to life

I’ve been really happy with Elodie so far. The only piece missing is the most rewarding.

How can I enjoy my photos now that I have them organized, backed up and preserved?

In my next post I’ll talk about [how I use Google Photos](/articles/my-automated-photo-workflow-using-google-photos-and-elodie/) along side of Elodie without compromising any of my originally stated goals. It’s pretty amazing so you’ll definitely want to read it.

Make sure you read my other posts in this series.

- [Understanding My Need for an Automated Photo Workflow](/articles/understanding-my-need-for-an-automated-photo-workflow/)
- [My Automated Photo Workflow using Google Photos and Elodie](/articles/my-automated-photo-workflow-using-google-photos-and-elodie/)
- [One Year of Using an Automated Photo Organization and Archiving Workflow](/articles/one-year-of-using-an-automated-photo-organization-and-archiving-workflow/)

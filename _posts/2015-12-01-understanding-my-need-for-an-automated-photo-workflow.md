---
layout: post
title: "Understanding My Need for an Automated Photo Workflow"
description: "Preserve, unify, experience — the three goals behind building a workflow for tens of thousands of photos and videos."
category: articles
logo:  skip
tags: [photo-management]
comments: false
share: true
---

<figure>
	<img src="/images/photos/2015-12-01-need-automated-photo-workflow-1.jpg" alt="Tuolumne Meadows. Yosemite, California.">
	<figcaption>Tuolumne Meadows. Yosemite, California.</figcaption>
</figure>

*Download* [*Elodie, the EXIF-based photo organizer app*](https://getelodie.com) *I made to manage my photos, and easily replicate the workflow in this post. You can also view the* [*open source command-line version*](https://github.com/jmathai/elodie) *on GitHub.*

<figure>
	<img src="/images/photos/2015-12-01-need-automated-photo-workflow-2.jpg" alt="Looking for Methuselah while motorbiking from Vegas to Yosemite through Death Valley.">
	<figcaption>Looking for Methuselah while motorbiking from Vegas to Yosemite through Death Valley.</figcaption>
</figure>

I wanted a better way to archive, unify and experience my photos and videos. Of all the great software that’s available today none of them addressed my needs.

I came up with a solution and I wanted to write about it because I don’t think I’m alone in wanting a workflow that brings sanity to the tens of thousands of photos and videos I have.

#### My goals in order of importance

1. ***Preserve.*** My photo library needs to be future-proof for decades into the future.
2. ***Unify.*** Photos from my wife and my phones need to be combined into a single library.
3. ***Experience.*** The photos and videos need to come to life and help us re-experience the moments when they were taken.

Given the plethora of software I should briefly explain why I continue to have this problem.

#### iPhoto, Aperture, Lightroom and other desktop apps

Most desktop apps rely on an internal database which they use to keep track of photos in your library. They also store files on your hard drive in ways that make most sense to them; not you.

Proprietary databases and file structures fail to future-proof my photo library. It’s difficult to stop using these programs once you’ve invested a lot of time in them.

Preserve? D-
Unify? C
Experience? B+

#### Flickr, 500px, etc.? Sorry.

Online photo services also store information in their own database. It’s not so bad if they give you a programmatic API to manage your library but it still falls short. If you’ve ever tried to move all of your photos from one service to another then you’ve felt this pain. I do not envy the person tasked with that job.

The experience they provide is pretty great since you can share and converse around photos but the lack of preservation is a deal breaker.

Preserve? F+
Unify? B-
Experience? A-

*If you really like Google Photos you’ll want to read through this series because I come back to using it later.*

### Building a Better Mouse Trap

I’ve been doing this long enough to know whatever I end up choosing needs to be simple, feel natural and be rewarding.

So daunting.

<figure>
	<img src="/images/photos/2015-12-01-need-automated-photo-workflow-3.jpg" alt="Breaking apart various NAS devices to get our Trovebox software running on them. (circa 2014)">
	<figcaption>Breaking apart various NAS devices to get our Trovebox software running on them. (circa 2014)</figcaption>
</figure>

#### Let’s start with the basics

I started thinking about what my utopia would look like. I wanted something simple and elegant; not complex or cumbersome. In addition to meeting the goals listed above the workflow needs to do a few things well.

1. Work entirely off the file system and EXIF contained within each photo and video.
2. Provide an easy way to get photos and videos from my wife and my phone into our library.
3. Be fast enough that I didn’t have to wait minutes at a time to add videos which could be up to 1GB in size.

There’s more but it’s good to start with a small list and let your experience of using the software influence how it expands.

#### Why use the file system?

The file system is the lowest common denominator. Everything else we use is built on top of it. Once you start building too much magic on top of the file system is when you start getting into trouble.

Unfortunately, using the file system by itself is very limiting. You can’t access it remotely across your devices, for example. It’s something we’ll have to figure out a solution to but we don’t need to know how yet.

#### Why use EXIF?

EXIF makes every photo in your library portable. If you store information about the photo in EXIF then you keep it with you by simply copying the file somewhere else. This is probably the most important decision from which I expect all sorts of good things to flow. We don’t need to know and understand the benefits of leveraging EXIF. You’ll have to trust my gut on this.

Bonus, videos support EXIF.

Extra bonus, iPhones store time and location information in EXIF of videos. Android users aren’t entirely out of luck because we can always add EXIF where it doesn’t exist.

#### Getting photos and videos off our phones quickly and easily

We take all of our photos on our phones (iPhones, at the moment). Getting those photos off has proven to be pretty tedious. Transferring videos over the Internet is too slow and connecting cables to my laptop was a pain.

AirDrop seems to be a sane candidate but we’ll have to figure out how to make that work for our needs.

### Start small, think big

If you make the right choices up front then the latter work tends to be pretty easy. There’s a lot we don’t know and some of those things are a pretty big deal.

<figure>
	<img src="/images/photos/2015-12-01-need-automated-photo-workflow-4.jpg" alt="Setting up load balancers for Photagious before racking them at Level3 a decade ago. (circa 2004)">
	<figcaption>Setting up load balancers for Photagious before racking them at Level3 a decade ago. (circa 2004)</figcaption>
</figure>

How will my wife and I be able to see all of these photos on our phones and how will we be able to easily search for the photos we want to see?

How will we get all of our existing photos into this library and more importantly how will future photos be added?

We’ll figure all of this out but you’ll need to read my other posts to see how.

Make sure you read my other posts in this series.

- [Introducing Elodie; Your Personal EXIF-based Photo and Video Assistant](/articles/introducing-elodie-your-personal-exif-based-photo-and-video-assistant/)
- [My Automated Photo Workflow using Google Photos and Elodie](/articles/my-automated-photo-workflow-using-google-photos-and-elodie/)
- [One Year of Using an Automated Photo Organization and Archiving Workflow](/articles/one-year-of-using-an-automated-photo-organization-and-archiving-workflow/)

<hr>

[Understanding My Need for an Automated Photo Workflow](/articles/understanding-my-need-for-an-automated-photo-workflow/) was originally published in [Vantage](https://medium.com/vantage) on Medium, where people are continuing the conversation by highlighting and responding to this story.

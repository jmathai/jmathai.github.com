---
layout: post
title: "How To Protect Your Photos From Bit Rot"
description: "Bit rot flips a bit silently, and you only find out when the photo won’t open. How checksums let you detect and repair it across a whole library."
category: articles
logo:  skip
tags: [photo-management]
comments: false
share: true
---

<figure>
	<img src="/images/photos/2016-12-19-bit-rot-1.jpg" alt="Crocodile River, Johannesburg, South Africa">
	<figcaption>Crocodile River, Johannesburg, South Africa</figcaption>
</figure>

*Download* [*Elodie, the EXIF-based photo organizer app*](https://getelodie.com) *I made to manage my photos, and easily replicate the workflow in this post. You can also view the* [*open source command-line version*](https://github.com/jmathai/elodie) *on GitHub.*

Bit rot, or more accurately data rot, is when one of the bits in a file gets flipped. This happens for a multitude of reasons including inadequate insulation and humidity. A single corrupt bit can result in an viewable photo or video.

Of all the failure scenarios, bit rot is one of the more difficult to know about and prevent. The primary reason is because bit rot happens silently. You won’t know about it until after it’s already happened and by then it’s often too late.

Want to feel despair? Do a Google search for how to protect against bit rot.

> It’s all just a matter of risk management. Except bit rot. That shit’s inevitable.
>  — kngspook [via HackerNews](https://news.ycombinator.com/item?id=8103386)

#### What if bit rot wasn’t inevitable?

One way to protect your photos against bit rot is to know all the correct bits for every single photo. The best way to do this is to keep a checksum or fingerprint of every photo in a database. That way you can take a photo, calculate its checksum and compare it what’s stored in the database. If the fingerprints don’t match then you know that the photo has changed.

That’s as far as any of the articles you read will go.

I wanted to find a solution that was easy and required little to no effort on my part. If a photo became corrupt I’d like to be told. Perhaps an email or something.

#### How I built bit rot protection into my photo archive

It turned out that I already had a database with a checksum of every photo and video in my archive. I wrote some software that automatically organizes and archives my entire photo library ([source code](https://github.com/jmathai/elodie)).

> Sound interesting? Get a free chapter from my book, [Photo Archiving for Nerds](https://photoarchivingfornerds.com).

It was really easy to add a command to check every photo in my archive against the checksum database. Here’s what I got when I ran it the first time.

<figure>
	<img src="/images/photos/2016-12-19-bit-rot-2.png" alt="*sigh of relief*">
	<figcaption>*sigh of relief*</figcaption>
</figure>

#### Scheduling an automated daily bit rot check

Checking my photo archive for any bit rot is a simple command. Now I can schedule that command to run every day. Since my photo archive is replicated to 3 different locations I could easily retrieve a known good copy.

It made sense for me to schedule the bit rot check on my Synology NAS at home since 1 of my 3 archives is on it. How you choose to schedule the check is entirely up to you. You can use cron (Linux, MacOS), Automator (MacOS) or Task Scheduler (Windows).

#### Getting notified when bit rot is detected

I scheduled the nightly script to email me if it detects any bit rot to one or more of my photo or video files. If I get this email I can verify the file and replace it from a known good copy from my Laptop or from Google Drive since those are 2 of my 3 backup sources; the Synology being the 1st.

<figure>
	<img src="/images/photos/2016-12-19-bit-rot-3.png" alt="An email I got when bit rot was detected in one of my photos">
	<figcaption>An email I got when bit rot was detected in one of my photos</figcaption>
</figure>

For the time being, I’m perfectly okay getting this email and taking some manual action on the corrupted photo. It shouldn’t happen very often and when it does I am okay taking 5 minutes of my day to do a quick sanity check.

I could automate the script further to look through revisions of the file until it finds a checksum match. But I’ll save that for another blog post.

Make sure you read my other posts in this series.

- [Understanding My Need for an Automated Photo Workflow](/articles/understanding-my-need-for-an-automated-photo-workflow/)
- [Introducing Elodie; Your Personal EXIF-based Photo and Video Assistant](/articles/introducing-elodie-your-personal-exif-based-photo-and-video-assistant/)
- [My Automated Photo Workflow using Google Photos and Elodie](/articles/my-automated-photo-workflow-using-google-photos-and-elodie/)
- [One Year of Using an Automated Photo Organization and Archiving Workflow](/articles/one-year-of-using-an-automated-photo-organization-and-archiving-workflow/)

<hr>

[How To Protect Your Photos From Bit Rot](/articles/how-to-protect-your-photos-from-bit-rot/) was originally published in [Vantage](https://medium.com/vantage) on Medium, where people are continuing the conversation by highlighting and responding to this story.

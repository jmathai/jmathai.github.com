---
layout: post
title: "One Year of Using an Automated Photo Organization and Archiving Workflow"
description: "A year after putting every photo on autopilot: AirDrop it, and it gets de-duplicated, organized, and archived automatically."
category: articles
logo:  skip
tags: [photo-management]
comments: false
share: true
---

<figure>
	<img src="/images/photos/2016-12-13-photo-archiving-one-year-1.jpg" alt="Crater Lake. Crater Lake National Park, Oregon">
	<figcaption>Crater Lake. Crater Lake National Park, Oregon</figcaption>
</figure>

*Download* [*Elodie, the EXIF-based photo organizer app*](https://getelodie.com) *I made to manage my photos, and easily replicate the workflow in this post. You can also view the* [*open source command-line version*](https://github.com/jmathai/elodie) *on GitHub.*

*Since I wrote this, Google Photos and Google Drive have* [*stopped working together*](https://www.blog.google/products/photos/simplifying-google-photos-and-google-drive/)*. I’m now using a* [*Google Photos plugin for Elodie*](https://github.com/jmathai/elodie/tree/master/elodie/plugins/googlephotos) *I wrote to simulate the same functionality which existed prior to this change.*

It’s been a year since I put *all* of my photos on autopilot. All I need to do is AirDrop the photos and videos I want to keep and they’re organized and archived automagically. How, you ask?

- Every media file gets de-duplicated against my entire photo collection.
- The metadata is carefully inspected and geolocation coordinates are turned into city names.
- The media file is deterministically placed in an appropriate folder based on date, location and other EXIF attributes.
- A normalized filename including the date and EXIF title attributes are used when moving the media file to its final destination.
- The source media file resides on my laptop in a folder based on date, location and other EXIF attributes. Here’s an example.

```
├── 2015-07-Jul│   ├── Mountain View│   │   ├── 2015-07-19_17-16-37-img_9426-walking-around-downtown.jpg
```

- One copy of the media file is escorted to my Synology NAS to serve as a local-remote copy using the identical folder hierarchy and file name as my laptop.
- A second copy of the media file is whisked away to Google’s servers to serve as a remote copy using, again, the identical folder hierarchy and file name as my laptop and Synology.
- Google Photos indexes, analyzes, and applies machine learning to the photos and makes them accessible via web and mobile apps.

#### Current Statistics

The size of my photo library is smaller than a lot of people I speak with because I only keep about 25% of the photos and videos I take. The rest are shown the trash can. Here’s a breakdown.

- 13,105 photos
- 142 videos
- 30 audio recordings
- 828 folders
- 228 gigabytes

#### Grading My Workflow

<figure>
	<img src="/images/photos/2016-12-13-photo-archiving-one-year-2.png" alt="A workflow diagram: photos from a phone or camera flow into a Macbook, through Elodie's rules engine, into an organized library mirrored to Google Photos and a Synology. Only the first step is marked manual.">
</figure>

I originally intended on this being an experiment to see if I could archive my photos without using any sort of database besides the filesystem itself.

Answer: yes.
Grade: A+.

The full list of things I learned is too long for a blog post. That’s why I’m writing a book named [*Photo Archiving for Nerds*](https://photoarchivingfornerds.com/).

#### EXIF Is More Powerful Than I Thought

Relying on EXIF was a critical hypothesis I made early on. I knew reading EXIF from JPEGs was doable.

It turns out that EXIF is supported by many RAW formats and while I don’t shoot in RAW it’s nice for when friends send me their RAW files from times we’re together.

Videos were the biggest question mark for me. I wasn’t sure how widely they supported EXIF. I was pleasantly surprised when I found out videos shot on iPhones have date and location EXIF embedded into them.

Turns out audio files, of the m4a persuasion, also support EXIF and iPhones embed them with date and location EXIF as well.

It felt like Christmas over and over again. But why stop while you’re ahead?

I moved on to investigating if I could reliably write EXIF. You know, for times like when you take photos with an SLR and location information is missing. Ultimately, I was able to edit EXIF on photo, video, and audio files.

Basically, every photo in my library has an embedded database with date, location, title, album, and more information.

#### A Few Words On Backups

My goal for backups was simple. It should be statistically impossible to lose a photo. Further, I wanted my backups to retain all of the edits and organization effort I put into the photos I browse while on the train or share with my family.

To make it impossible to lose a photo I needed to make sure there wasn’t any single point of failure. That ruled out relying on a cloud service like Dropbox or Google Drive as my “backup”.

I went with a workflow that kept a copy of each photo on my laptop, on my Synology and in Google Drive. I was safe unless Google Drive deleted my photos at the same time my house was on fire while I was there. Not to mention both my Synology and Google Drive keep multiple versions of each file. Statistically impossible enough for me.

Make sure you read my other posts in this series.

- [Understanding My Need for an Automated Photo Workflow](/articles/understanding-my-need-for-an-automated-photo-workflow/)
- [Introducing Elodie; Your Personal EXIF-based Photo and Video Assistant](/articles/introducing-elodie-your-personal-exif-based-photo-and-video-assistant/)
- [My Automated Photo Workflow using Google Photos and Elodie](/articles/my-automated-photo-workflow-using-google-photos-and-elodie/)

<hr>

[One Year of Using an Automated Photo Organization and Archiving Workflow](/articles/one-year-of-using-an-automated-photo-organization-and-archiving-workflow/) was originally published in [ART + marketing](https://medium.com/art-marketing) on Medium, where people are continuing the conversation by highlighting and responding to this story.

---
layout: post
title: "My Ridiculously Robust Photo Management System (Immich Edition)"
description: "How I added Immich to my already robust photo management system to make it ridiculously robust."
category: articles
logo:  skip
tags: []
image:
  feature: main-photo-workflow-immich.png?1
comments: false
share: true
---

<hr>

TL;DR: Changes to albums, descriptions, location, date/time and favorites through Immich are stored in the photo's EXIF and automatically backed up to my Synology NAS and into Dropbox; no database needed. Below is a video for those who prefer to watch instead of read.

I created a simpler version of the plugin I use that is suitable for those with their own workflows which might differ from mine. It's available at <a href="https://github.com/jmathai/immich-exif">immich-exif</a>.

  <div style="position: relative; padding-bottom: 62.5%; height: 0;" id="inline-embed-container">
  </div>
  <script>window.neetoRecord = window.neetoRecord || { embed: function(){(neetoRecord.q=neetoRecord.q||[]).push(arguments)} };</script>
  <script async
    src="https://lattice.neetorecord.com/javascript/embed.js">
  </script>
  <script>
    neetoRecord.embed({
      type: "inline",
      id: "c1ad81a2-5f96-443b-9f74-83f4065c957e",
      organization: "lattice",
      elementSelector: "#inline-embed-container",
      styles: "position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;", 
    });
  </script>
<hr>

I've been working on my photo management and archiving workflow for over 2 decades. It's changed a lot over that time but usually in bursts. It works really well and I don't have to touch it much.

By far, the most durable aspect of my photo management workflow is that it <strong>only</strong> relies on EXIF to store metadata about photos. No reliance on an external database to keep track of descriptions, favorites or albums. I'm not sure of any other workflow which does this but I think they all should. But we're not here to talk about that. I want to tell you all how I'm using Immich.

I outlined my philosophy for photo management in detail in <a href="https://medium.com/vantage/understanding-my-need-for-an-automated-photo-workflow-a2ff95b46f8f#.dmwyjlc57">another post</a> but I'll summarize them here in order of importance.

<ul>
    <li><strong>Preserve.</strong> My photo library needs to be future-proof for decades into the future.</li>
    <li><strong>Unify.</strong> Photos from my wife and my phones need to be combined into a single library.</li>
    <li><strong>Experience.</strong> The photos and videos need to come to life and help us re-experience the moments when they were taken.</li>
</ul>

I was <a href="https://medium.com/@jmathai/my-automated-photo-workflow-using-google-photos-and-elodie-afb753b8c724">using Google Photos as a read-only viewer</a> of my photos and fell in love with the discovery features. But a <a href="https://blog.google/products-and-platforms/products/photos/simplifying-google-photos-and-google-drive/">change</a> back in 2019 to how Google Photos and Google Drive worked together broke my workflow.

The primary source of my photos is my Synology NAS at home. I organize my photos using a <a href="https://github.com/jmathai/elodie">simple command-line tool, named Elodie, </a> that I wrote over 10 years ago that's grown to 10k lines of code, 1,300 stars and 150 forks. The best way to describe it is that it materializes your photo library onto the file system using only the EXIF. It's my canonical organizer.

I clobbered together a plugin for Elodie that would <a href="https://github.com/jmathai/elodie/tree/master/elodie/plugins/googlephotos">replace the Google Drive + Google Photos capabilities</a> that Google deprecated. This let me continue using Google Photos as a read-only viewer for my photos. But I was growing tired of relying on Google services and especially handing over all of the data embedded in my photos. So I stopped using Google Photos.

I was left with several years of not having a great way to view my photos. I desire a richer experience than the folder-based default experience I have with Synology and Dropbox. I was very optimistic about Synology Photos but it was unfortunately underwhelming. Maybe because my Synolgoy NAS is 10 years old but I also didn't want to upgrade it.

I've been hearing a lot of positive feedback from others about Immich and had been keeping a close eye on it. At the end of 2025, I decided to take a closer look. The aha moment was when I learned about <a href="https://docs.immich.app/guides/external-library/">external libraries</a>. If you're not familiar with them, they're existing folders that you can tell Immich about and it'll add them to your photo library. Most importantly, you can mount them as read-only.

I immediately drew paralells to my prior use of Google Photos. I quickly determined that I could restore what I lost with Google Photos using Immich. But I wondered ... what if I could do more? Been wondering for a few years, actually.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;ve been thinking, for years, about an easier interface to manage my photos using <a href="https://twitter.com/getelodie?ref_src=twsrc%5Etfw">@getelodie</a> (the Github version) than the command line. I haven&#39;t put my finger on it.<br><br>Probably doesn&#39;t have to work on mobile. Probably web. Mobile / desktop apps deteriorate quickly anyways.</p>&mdash; Jaisen (@jmathai) <a href="https://twitter.com/jmathai/status/1587163999900037121?ref_src=twsrc%5Etfw">October 31, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Turns out the answer is yes. I was able to turn Immich from a read-only viewer to a full fledged way to organize my photos while relying only on EXIF. Now, Immich doesn't modify EXIF of photos. Instead, it stores information into its Postgres database. Immich <em>can</em> <a href="https://docs.immich.app/features/xmp-sidecars/">read from and write to XMP sidecar files</a>. But sidecars are too clunky for me. I want <em>everything</em> embeded in the photo file itself. As far as I understand, Immich authors don't want to edit the original photo file. I get their reasoning but I still want to be able to.

What I thought would require a 4 hour session with Claude Code turned into a two week rendevous learning a lot more than I anticipated about how Immich works. External libraries are great but there are some obvious gotchas with how Elodie works. If you add a photo to an album using Elodie then it will update the photo's EXIF and <em>also</em> move the photo into a folder with the name of the album. To Immich, this is interpretted as deleting the original file and creating a new one. This creates all sorts of challenges but I was able to solve it using an <a href="https://en.wikipedia.org/wiki/Eventual_consistency">eventually consistent</a> approach. This means, all of the changes are stored and will eventually materialize.

There were other smaller challenges but I was able to overcome them all with some elbow grease. Immich's API is pretty great and I'm probably just scratching the surface. But for now, I've been spending a lot of time enjoying my photos like I haven't been able to for a while without compromising my core principles for making sure they're around in a couple decades.

A detailed technical explanation is outside the scope of this post but if folks want to know I'll write it up separately. For now, follow <a href="https://github.com/jmathai/elodie/issues/496">GitHub issue 496</a> to track progress and see the code.



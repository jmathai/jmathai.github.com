---
layout: post
title: "UX Nirvana ~ Elegant Pagination with Infinite Scrolling"
description: "Infinite scrolling usually breaks deep links and the back button. How we shipped it with pagination that actually works."
category: articles
logo:  skip
tags: [technology,article]
comments: false
share: true
---

<figure>
	<img src="/images/photos/2014-04-04-infinite-scroll-pagination-1.jpg" alt="Two young children walking across a sandy beach carrying plastic buckets, the ocean and a blue sky behind them.">
</figure>

#### We just pushed the impossible to production; infinite scrolling with pagination that actually works.

Trovebox is a [media management and sharing service for teams and organizations](https://trovebox.com/). [Start your free trial](https://trovebox.com/plans) today.

Two years ago our photo gallery looked much different than it does today. It was a grid of cropped photos with pagination links. The user interface was terrible and the user experience worse.

<figure>
	<img src="/images/photos/2014-04-04-infinite-scroll-pagination-2.jpg" alt="version 1.0 ~ our arcane grid layout with pagination">
	<figcaption>version 1.0 ~ our arcane grid layout with pagination</figcaption>
</figure>

Photo collections often contain tens of thousands of photographs and serve a single purpose; to be visually consumed. Moving your mouse cursor over a link and clicking to see the next twenty-five photos felt arcane. Infinite scrolling began gaining popularity many years ago but brought along new sets of problems. While I believe most users enjoy infinite scrolling there’s a vocal minority who abhor it. Rightfully so, perhaps.

Infinite scrolling tends to break a number of behaviors we’ve become accustomed to on the web; mundane tasks like deep linking to content and using the browser’s back button. Tasks we take for granted until we can no longer do them.

We didn’t have all the answers but knew that a user interface with infinite scrolling would be better than our older paginated one. Our primary goal was making it enjoyable to view as many photos as possible as quickly as possible. Our new gallery adopted a fixed height masonry layout that minimized cropping and automatically loaded more photos as you reached the bottom of the page.

<figure>
	<img src="/images/photos/2014-04-04-infinite-scroll-pagination-3.jpg" alt="version 2.0 ~ our improved masonry layout with infinite scroll">
	<figcaption>version 2.0 ~ our improved masonry layout with infinite scroll</figcaption>
</figure>

The masonry layout required less mental energy to browse photos; leading to a more enjoyable viewing experience.

We realized as you view photos you aren’t thinking about pages or having to click to see more. Our minds have been trained to do that but it‘s a disruptive experience. This is where infinite scroll shines.

When we launched infinite scroll we knew we gave up some nice-to-haves. They weren’t critical for us but were important enough that we created a [couple](https://github.com/photo/frontend/issues/1434) [issues](https://github.com/photo/frontend/issues/1435) to track the progress of their solutions.

Our infinite scrolling interface works so well you’ll find yourself on the twentieth page of photos without realizing it. That’s great news but users have become accustomed to copying a link with the expectation that it will point to what they just saw. Infinite scroll isn’t a reason we should ask our users to change their habits. The problem has many nuances though and the solution isn’t as straightforward once you put yourself in your users’ shoes.

It seemed obvious that we could use [pushstate](https://developer.mozilla.org/en-US/docs/Web/Guide/API/DOM/Manipulating_the_browser_history#Adding_and_modifying_history_entries) to update the browser’s URL bar as the user scrolled through pages of photos. Links copied from the URL bar would load photos starting from the page they were looking at the moment they copied it.

With a mix of [Backbone.js](http://backbonejs.org/#Router) and [Waypoints](http://imakewebthings.com/jquery-waypoints/#about) we were able to quickly get the URL bar updating as the user scrolled through photos. That’s when we realized a limitation of infinite scrolling we hadn’t previously thought of; infinite scrolling tends to work as you scroll down. What if you needed to scroll up to view photos from page 9 when the link started at page 10?

I haven’t seen an implementation of infinite scrolling which handles this and we couldn’t come up with an intuitive way to make it. That led us back to the drawing board to come up with some ideas. At minimum we could let the user know there are prior pages of photos. We quickly realized that’s just as terrible as not indicating it at all.

Shortly after realizing how terrible our idea was it dawned on us that we could include pagination similar to what we had in our older user interface. But only when the gallery was deep linked; starting on pages 2 and higher.

[Here’s an example](https://current.trovebox.com/photos/page-8/list) and a screenshot below where you can see the pagination near the top right.

<figure>
	<img src="/images/photos/2014-04-04-infinite-scroll-pagination-4.jpg" alt="The Trovebox photo gallery in a browser window, a grid of photo thumbnails with an arrow pointing to the numbered pagination controls above it.">
</figure>

Our infinite scroll interface started to show signs of having the best of both worlds. The most common navigation was easier by an order of magnitude and less common navigation was as easy as it’s always been.

While we’re very happy with the results there’s more work to be done. How should the back button work? What about search engine optimization?

We hope to tackle these issues next. But for the time being we believe we’re 90% of the way there. That last 10% will keep us busy.

Footnotes: At Trovebox we not only use a tremendous amount of open source software but we release the majority of our work as open source. You can [follow the project on Github](https://github.com/photo) and [follow me on Twitter](https://twitter.com/jmathai).

Photos in the screenshots were taken by [Duncan Rawlinson](http://duncan.co/).

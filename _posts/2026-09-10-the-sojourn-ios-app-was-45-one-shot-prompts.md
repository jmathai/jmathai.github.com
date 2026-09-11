---
layout: post
title: "The Sojourn iOS App Was 45 One-Shot Prompts"
description: "Sojourn was built as 45 closed GitHub issues, each one a single cold-start prompt. Here's what that process is good at, and where it falls apart."
logo:  skip
tags: [sojourn,ai]
comments: false
share: true
---

<hr>

[Sojourn: Topical Bible Study](https://trysojourn.app) is an app I published without typing a single line of its code.

That part isn't interesting anymore. Plenty of people are writing code with AI. What I think is interesting is the process. Since ChatGPT 3.5, I’ve been a little bit obsessed about LLMs writing code. Not assisting me writing code, doing it all for me. While the process has evolved **a lot**, I’m going to talk about where it’s at now and give an explaination.

### About the app
The app is an iOS app written in Swift. It has a streaming chat interface which parses the incoming text in real time. This is done to eliminate hallucinations of scripture by replacing LLM generated citations with text from an app-bundled database. All scripture references are guaranteed to be correct and users can tap on them to explore surrounding verses and chapters. The UX of the app holds a high bar in terms of performance and usability.

The app talks to a backend written in Python that connects to an LLM provider’s API. The backend exposes a <code>tool</code> for scripture lookups instead of relying on the model to do it itself. Nothing about the user’s chats or identity is stored on the backend. It all lives only within the app itself.

### About the process
I should define what I mean by *one-shot*. It’s a single prompt that’s sufficient to implement an end-to-end feature regardless of complexity. In reality, there may be a couple follow up prompts to tweak something here and there. But mostly, it should be 0 follow up prompts.

### Baseline context
I spent multiple days co-drafting the user experience and features I wanted in the app using Claude Design. The home page of the website embeds the artifact of that work as an iframe - you can see it on the app’s [Sojourn: Topical Bible Study](https://trysojourn.app) page.

This iframe ended up becoming a major input source for when I started creating the actual iOS app. Turns out Claude Code can understand a functional prototype quite deeply. So much so that the user experience of the app is nearly identical to what Claude Design generated. This was a pleasant surprise.

I also created a bunch of markdown content that’s stored in <code>CLAUDE.md</code> and adjacent artifacts which outline product definitions and constraints. For example, privacy is a cornerstone and it explicitly states that the app should never collect personally identifiable analytics.

This baseline context is created once, updated automatically, and guides the following steps.

### <code>/spec</code>
Ever feature starts by me using a skill named <code>/spec</code>. This is where I take my time collaborating with AI to fully define everything about the feature including happy path, failure modes, look &amp; feel, architecture and testing.

Every feature is stored as a GitHub issue. Once I feel the feature is adequately described, I give it the go ahead to create the GitHub issue based on a template in the skill. The issue title is a short summary of the feature and the description is a detailed explanation of it.

### <code>/gh-issue</code>
Implementing a feature is as simple as me using the <code>/gh-issue</code> skill and passing the *issue number* to it. I generally get up and leave the room at this point. The skill does all sorts of cool things like looking up other issues or pull requests if they’re mentioned. Sometimes I’ll have two unimplemented features each with their own GitHub issue and I make sure they reference each other. This way, when implementing the first it knows to look up the second and proceed accordingly.

Once finished, it automatically creates a pull request.

I often kick this off before going to bed and wake up to a new feature in my app.

### Publishing and deploying
I still do this by hand. But it’s still fully automated through scripts like <code>run.sh</code> which runs the app in the simulator, <code>deploy-to-device.sh</code> which installs it directly on my iPhone, and <code>release.sh</code> which publishes it App Store Connect to be published.

Nothing is one-off or done by hand. If I have to do it once, it gets automated into a skill or script. I recently switched laptops and getting up and running was quite smooth once I transferred App Store Connect keys.

For other projects, I have a <code>/gh-pr</code> skill which merges the pull request and deploys it. Works great for web apps but I don’t want every feature to be published to Test Flight or the App Store - so I batch them as I see fit.

### Some examples
A feature I really enjoy is the *home screen widget*. It was 2,466 lines of code across 27 files. This included a new WidgetKit extension, a shared app group, a verse pool, deep links back into the app, and the XcodeGen config to build it. One issue. One prompt. One PR.

<figure>
	<img src="/images/photos/2026-09-10-sojourn-widget.png" alt="The Sojourn home screen widget showing a Psalms 88 passage under the heading DESPAIR">
	<figcaption>The home screen widget - one issue, one prompt, one PR.</figcaption>
</figure>

Another feature I’m testing out is *emailing yourself a conversation*. It was 2,412 lines of code across 21 files, and it spans the client, the backend, and a delivery provider. Also one issue.

<figure>
	<img src="/images/photos/2026-09-10-sojourn-email-conversation.png" alt="The bottom of a Sojourn conversation showing an Email this to me action above the message input">
	<figcaption>Emailing yourself a conversation, tucked in above the message field.</figcaption>
</figure>

Neither of those is a small feature, and neither is a boilerplate feature. What made them work is that the spec had already settled the hard questions.

### How’s it going?
Excellent. The limiting factor is shepherding the user experience of the app. Just because you can add multiple features a day doesn’t mean you should. I take my time [thinking through a feature until it feels right](/articles/latent-product-development/).

So far I’ve created 49 GitHub issues and closed 45 of them in a matter of weeks. That’s 45 features implemented. The 4 open issues are features or bug fixes I haven’t felt are important enough to do yet.

Now that you know how the sausage is made, download [Sojourn: Topical Bible Study](https://apps.apple.com/us/app/trysojourn/id6792011966) and let me know what you think by clicking my email address in the footer.

### Caveats
I happen to have an immense breadth of experience. I've been building things professionally for decades including launching several startups. That’s given me pretty deep expertise across design, development, infrastructure, marketing...you name it. It’s a unique advantage when paired with AI and one I’m grateful for.
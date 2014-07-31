---
layout: page
permalink: /openphoto-trovebox/
logo:             site-logo.png
skipheader: true
title: The Story of OpenPhoto / Trovebox
description: Documenting my 3 year startup journey founding OpenPhoto / Trovebox.
#tags: [Jekyll, theme, themes, responsive, blog, minimalism]
---

<ul class="post-list">
{% for post in site.posts reversed %} 
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>


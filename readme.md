# News Scanner

## Overview

This program is designed to regularly scan the front page of news websites, and detect when something has 
changed, e.g. a new item was added or an existing item was updated. When a change is detected the program writes out a 
message on the command line detailing exactly what changed.

### Tracked News Item Attributes

The news item attributes that are currently tracked are:
  - time of scanning
  - news website
  - headline title
  - headline url
  - topic (if available within article block)

### Added News Items

Each news item is considered unique based upon URL. 
If a scanned news item has a URL that isn't recorded in the database then it is considered an added news item.

### Updated News Items

When a scanned news item has a URL that is already recorded in the database, then it is considered an existing news item.
An existing news item is further considered as an updated news item if any of the following differ to the existing 
database value:
  - headline title
  - topic

#### Scanned News Websites

News websites that are currently scanned are:
  - SBS news (all news items)
  - The Australian (all news items)
  - 9 news (most news items, currently not included are 'takeover' featured article and "You may also like" / recommended news)
  - ABC news (most news items, currently not included are "State & Territory News", "Local News", "News video", 
  "My Topics", and "Best of ABC.NET.AU")

## Getting Started

For setup and run instructions refer to the document [getting started](./docs/getting_started.md)

## Future Development
Tasks for future development include:
  - Update news parser implementations to get uncommon new item components including author, topic and 
  summary content.
  - Add news item file logger as alternate to console logging.
  - Move some configuration into YAML files such as scheduled run frequency.
  - Determine other condition for news item uniqueness than Url, as a front page can contain multiple news items with 
  the same url.
  - Update parsed news item URL to be fully qualified if it doesn't include the website base url upon parsing. 

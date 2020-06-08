# News Scanner

## Overview

This program is designed to regularly scan the front page of news websites, and detect when something has 
changed, e.g. a new item was added or an existing item was updated. When a change is detected the program writes out a 
message on the command line detailing exactly what changed.

The news item components that are currently tracked are:
  - website
  - headline title
  - headline url
  - time of scanning

News websites that are currently scanned are:
  - SBS news (all news items)
  - The Australian (all news items)
  - 9 news (most news items, not 'takeover' featured article, nor "You may also like" / recommended news)
  - ABC news (most news items, not "State & Territory News", nor "Local News", nor "News video", 
  nor "My Topics", nor "Best of ABC.NET.AU")

## Getting Started

For setup and run instructions refer to the document [getting started](./docs/getting_started.md)

## Future Development
Future development would next focus on:
  - Implementing a more detailed news parser interface to get uncommon new item components including author, topic and 
  summary content
  - Implementing more specialised news parser interface implementations for each target news website to capture all 
  news items
  - Adding news item file logger as alternate to console logging
  - Moving some configuration into YAML files such as scheduled run frequency

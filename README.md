# TikTok Misinformation Feed Experiment

This project automates two simulated TikTok users scrolling through the feed to analyze how misinformation is presented based on user interaction patterns.

## Features

- **Control Bot**: Scrolls passively through TikTok feed (no likes/interactions).
- **Experimental Bot**: Scrolls with varied watch durations and simulated likes.
- **Parallel Execution**: Runs both bots simultaneously using isolated browser contexts.
- **Logging**: Supports simple timestamped logging of user actions.

## Setup

```bash
pip install -r requirements.txt
playwright install

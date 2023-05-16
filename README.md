# Discord Media Upload Bot

This bot is designed to organize your files and upload them to your Discord server. It is capable of creating new channels in the specified category and uploading files from local subfolders. It also supports a configurable limit on the number of files uploaded from each folder.

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Usage](#usage)

## Features

- Scans and uploads files from local directories.
- Creates new channels as necessary.
- Allows a user-defined limit on the number of files uploaded from each folder.
- Provides logs with embeds about file uploads and new channels.
- Files can be deleted after upload (optional).

## Getting Started

### Prerequisites

1. Python 3.7 or later
2. discord.py library
3. A Discord bot token

### Installation

1. Clone the repo: `git clone [https://github.com/your-username/discord-upload-bot.git](https://github.com/KazuInTheStu/Discord-Mass-Upload-Bot.git)`
2. Install necessary Python packages: `pip install -r requirements.txt`
3. Enter your Discord bot token in `bot.run('insert-bot-token-here')`

## Usage

- Command: `#upload <category-id> [number-of-files]`

This command uploads a certain number of files (optional parameter) from each subfolder to the specified category.

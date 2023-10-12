# Telegram Media Mass Downloader

This project allows users to search for and download media (images and videos) from Telegram chats (be it private chats, groups, or channels) using the Telethon Python library. Enhanced with a range of filtering options, it offers versatility in specifying which media to download. In addition to downloading, it provides the option to update image metadata to reflect the sending time of the image.

## Getting Started

### Prerequisites

- Python 3.x
- `pip` for installing dependencies
- Telegram API credentials (`api_id` and `api_hash`)

### Obtaining Telegram API Credentials

Before using the tool, you need to obtain API credentials from Telegram:

1. Visit [Telegram's My Apps](https://my.telegram.org/auth) and log in with your Telegram account.
2. Click on `API Development tools`.
3. Fill in the necessary application details to register a new application.
4. Once registered, you'll receive the `api_id` and `api_hash` credentials. Ensure these are kept confidential and not shared.

### First-time Authentication

Upon your first use of the software, you will be prompted to provide the api_id, api_hash, and your phone number (for Telegram authentication). This process helps in establishing a secure connection to your Telegram account. Once authenticated, you won't need to provide these details on subsequent uses. All sensitive data, like the api_id and api_hash, will be encrypted and stored securely.

### Installation

1. Clone this repository:

   ```
   git clone https://github.com/MohammadMokhalled/Telegram-Media-Mass-Downloader.git
   cd Telegram-Media-Mass-Downloader
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

   **Note**: The main dependencies are `telethon` for Telegram API access and `cryptography` for encrypting sensitive data. If you're planning to adjust image metadata, `piexif` is also essential.

### Usage

1. **Search for Chats**: Before downloading media, you may wish to search for a chat ID by name or partial name:

   ```
   python cli_handler.py search
   ```

   Follow the prompts to input a search term and view the resulting chats.

2. **Download Media**: Utilize the chat ID obtained from the search command to download media:

   ```
   python cli_handler.py download <CHAT_ID> [OPTIONS]
   ```

   Options:
   - `--images`: Enable downloading of images.
   - `--videos`: Enable downloading of videos.
   - `--set-timestamp`: Update the image's metadata timestamp to reflect the sending time.
   - `--start-date YYYY-MM-DD`: Filter media beginning from this date.
   - `--end-date YYYY-MM-DD`: Filter media up until this date.
   - `--self-only`: Download media sent by yourself only.
   - `--others-only`: Download media sent by others only.
   - `--min-size SIZE_IN_BYTES`: Filter media files by minimum size.
   - `--max-size SIZE_IN_BYTES`: Filter media files by maximum size.
   - `-o OUTPUT_DIRECTORY` or `--output OUTPUT_DIRECTORY`: Determine the output directory for downloaded media.

### Security

Sensitive data such as the Telegram `api_id` and `api_hash` are encrypted and stored securely. An encryption key is generated during the initial run and saved locally. Be cautious not to disclose or expose this key or the encrypted data file.

## About the Project

This project was conceived to provide an effortless and secure method to download media from Telegram. Thanks to its enhanced filtering options, users can precisely dictate which media they wish to download. Whether the goal is to archive images or videos from a specific chat, filter by date, or just obtain a local copy of media, the Telegram Media Mass Downloader is poised to assist.

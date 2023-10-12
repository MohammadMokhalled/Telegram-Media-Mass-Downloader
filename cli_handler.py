# cli_handler.py

import os
import argparse
from telethon import TelegramClient
from encryption import load_encrypted, save_encrypted
from downloader import download_media_from_chat
from searcher import search_chats
from encryption import ENCRYPTED_FILE

def main():
    parser = argparse.ArgumentParser(description="Telegram Media Downloader")

    # Define possible commands
    subparsers = parser.add_subparsers(dest="command")

    # Search command
    search_parser = subparsers.add_parser('search', help='Search for chats based on a name or partial name.')

    # Download command
    download_parser = subparsers.add_parser('download', help='Download media from a specific chat.')
    download_parser.add_argument('group_id', type=int, help='ID of the chat from which to download media.')
    download_parser.add_argument('--images', action='store_true', help='Enable downloading images.')
    download_parser.add_argument('--videos', action='store_true', help='Enable downloading videos.')
    download_parser.add_argument('--set-timestamp', action='store_true', help='Change image timestamp to sending time.')
    download_parser.add_argument('-o', '--output', default='telegram_media', help='Specify the output directory for downloaded media.')
    download_parser.add_argument('--start-date', type=str, help='Filter messages from this date (format: YYYY-MM-DD).')
    download_parser.add_argument('--end-date', type=str, help='Filter messages up to this date (format: YYYY-MM-DD).')
    download_parser.add_argument('--self', action='store_true', help='Download only media sent by yourself.')
    download_parser.add_argument('--others', action='store_true', help='Download only media sent by others.')
    download_parser.add_argument('--min-size', type=int, help='Minimum file size in bytes.')
    download_parser.add_argument('--max-size', type=int, help='Maximum file size in bytes.')

    # Parse arguments
    args = parser.parse_args()

    # Connect to Telegram
    if not os.path.exists(ENCRYPTED_FILE):
        api_id = input("Enter your API ID: ")
        api_hash = input("Enter your API Hash: ")
        save_encrypted(api_id, api_hash)
    else:
        api_id, api_hash = load_encrypted()

    with TelegramClient('anon', api_id, api_hash, entity_cache_limit=50000) as client:
        if args.command == "search":
            search_term = input("Enter the name or partial name of the chat: ")
            search_chats(client, search_term.lower())

        elif args.command == "download":
            download_media_from_chat(client, args.group_id, args.images, args.videos, args.set_timestamp, args.output, args.start_date, args.end_date, args.self, args.others, args.min_size, args.max_size)

if __name__ == '__main__':
    main()

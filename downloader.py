# downloader.py

import os
import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto, MessageMediaDocument
import piexif

OUTPUT_DIRECTORY = "telegram_media"

def set_image_timestamp(image_path, timestamp):
    """Set the image's timestamp metadata to the given timestamp."""
    exif_dict = piexif.load(image_path)
    formatted_time = timestamp.strftime("%Y:%m:%d %H:%M:%S").encode("utf-8")
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = formatted_time
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = formatted_time
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, image_path)

def download_media_from_chat(client, chat_id, download_images=True, download_videos=True, set_image_timestamp_flag=False, output_directory=OUTPUT_DIRECTORY, start_date=None, end_date=None, self_only=False, others_only=False, min_size=None, max_size=None):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    total_messages = client.get_messages(chat_id, limit=1).total  # Get total message count for percentage calculation
    processed_messages = 0

    end_date_temp = datetime.datetime.now().date() + datetime.timedelta(days=1)
    if end_date: 
        end_date_temp = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    for message in client.iter_messages(chat_id, offset_date = end_date_temp, limit=1000):  # Set your desired limit

        older_message = False
        # Handle Date Filtering
        if start_date and message.date.date() < datetime.datetime.strptime(start_date, "%Y-%m-%d").date():
            older_message = True

        if older_message == False:
            # Handle sender filtering
            if self_only and message.sender_id != client.get_me().id:
                continue
            if others_only and message.sender_id == client.get_me().id:
                continue

            file_path = None

            if download_images and isinstance(message.media, MessageMediaPhoto):
                filename = f"{message.date}_{chat_id}_{message.id}.jpg".replace(":", "-")
                file_path = os.path.join(OUTPUT_DIRECTORY, filename)
                if not os.path.exists(file_path):
                    client.download_media(message=message, file=file_path)
                if set_image_timestamp_flag and file_path:
                    set_image_timestamp(file_path, message.date)

            elif download_videos and isinstance(message.media, MessageMediaDocument):
                for attr in message.media.document.attributes:
                    if isinstance(attr, DocumentAttributeFilename):
                        if attr.file_name.lower().endswith(('.mp4', '.mkv', '.webm', '.mov')):
                            file_name = f"{message.date}_{chat_id}_{message.id}".replace(":", "-")
                            ext = os.path.splitext(attr.file_name)[-1]
                            file_path = os.path.join(OUTPUT_DIRECTORY, file_name + ext)
                            if not os.path.exists(file_path):
                                client.download_media(message=message, file=file_path)
                            break

        # Update the processed message count
        processed_messages += 1

        # Calculate and print the completion percentage
        percentage = (processed_messages / total_messages) * 100
        print(f"\rCompleted: {percentage:.2f}%", end="", flush=True)

    # Print a newline at the end to ensure the next printed content starts on a new line
    print()
    print("Download complete.")


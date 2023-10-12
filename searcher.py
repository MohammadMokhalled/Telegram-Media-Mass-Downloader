# searcher.py

from telethon.tl.types import Channel, User, Chat

def search_chats(client, search_term):
    matching_dialogs = []
    
    for dialog in client.iter_dialogs():
        match_by_name = search_term.lower() in dialog.name.lower()
        match_by_username = hasattr(dialog.entity, 'username') and dialog.entity.username and search_term.lower() in dialog.entity.username.lower()
        
        if match_by_name or match_by_username:
            matching_dialogs.append(dialog)

    if not matching_dialogs:
        print("No matching chats found.")
        return None

    for index, dialog in enumerate(matching_dialogs, 1):
        chat_type = "Unknown"
        if isinstance(dialog.entity, User):
            chat_type = "Private"
        elif isinstance(dialog.entity, Chat):
            chat_type = "Group"
        elif isinstance(dialog.entity, Channel):
            if dialog.entity.megagroup:
                chat_type = "Megagroup (Supergroup)"
            else:
                chat_type = "Channel"
        print(f"{index}. {dialog.name} (ID: {dialog.id}, Type: {chat_type}, Username: @{dialog.entity.username if hasattr(dialog.entity, 'username') and dialog.entity.username else 'N/A'})")

    return None

import requests
def reply(message='테스트', msg_id:int, guild_id:int, cha_id:int, bot_token):
    headers = {"authorization": f"Bot {bot_token}"}

    data = {
        "content": message,
        "nonce": "테스트",
        "embed": {
            "title": "테스트",
            "color": 0x0000FF
         },
        "tts": True,
        "message_reference": {
        "guild_id": guild_id,
        "channel_id": cha_id,
        "message_id": msgid
        },
        "allowed_mentions": {
            "parse": [],
            "replied_user": True
        }
    }

    return requests.post(f'https://discord.com/api/v8/channels/{cha_id}/messages', json=data, headers=headers).text

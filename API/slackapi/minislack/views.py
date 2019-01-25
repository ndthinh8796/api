import requests
from django.shortcuts import render


def index(request):
    channel_url = 'https://slack.com/api/users.conversations?token=xoxp-452524853910-452531064822-533500849926-4eb3cea535afed08434c384ef5236dae&types=public_channel%2C%20private_channel'
    channel_response = requests.get(channel_url).json()
    all_conversations = {}
    for channel in channel_response['channels']:
        id = channel['id']
        conversation_url = 'https://slack.com/api/conversations.history?token=xoxp-452524853910-452531064822-533500849926-4eb3cea535afed08434c384ef5236dae&channel={}'.format(id)
        conversation_response = requests.get(conversation_url).json()
        messages = []
        for conversation in conversation_response['messages']:
            message = conversation['text']
            if message.startswith('<!channel>'):
                messages.append(message.replace('<!channel>', ''))
        if messages:
            all_conversations[channel['name_normalized']] = messages
    return render(request,
                  'minislack/index.html',
                  {'all_conversations': all_conversations},
                  )

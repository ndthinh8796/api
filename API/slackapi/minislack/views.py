import requests
from django.shortcuts import render
from .models import Conversation


def index(request):
    legacy_token = 'xoxp-452524853910-452531064822-533011344403-ed164819e81bc463eabf73cc931aab29'
    id = get_general_id(legacy_token)
    get_messages(legacy_token, id)
    messages = Conversation.objects.all()
    return render(request,
                  'minislack/index.html',
                  {'messages': messages},
                  )


def get_general_id(token):
    channel_url = 'https://slack.com/api/users.conversations?token={}&types=public_channel%2C%20private_channel'.format(token)
    channel_response = requests.get(channel_url).json()
    for channel in channel_response['channels']:
        if channel['is_general']:
            return channel['id']


def get_messages(token, channel_id):
    conversation_url = 'https://slack.com/api/conversations.history?token={}&channel={}'.format(token, channel_id)
    conversation_response = requests.get(conversation_url).json()
    for conversation in conversation_response['messages']:
        message = conversation['text']
        if message.startswith('<!channel>'):
            message = message.replace('<!channel>', '')
            if message:
                user_name = get_user_name(token, conversation['user'])
                convo = Conversation(user=user_name,
                                     text=message)
                convo.save()


def get_user_name(token, user_id):
    user_url = 'https://slack.com/api/users.info?token={}&user={}'.format(token, user_id)
    user_response = requests.get(user_url).json()
    return user_response['user']['name']

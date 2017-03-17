import itchat
import requests

key = 'f5b3555ca42545e18b54e497eb3eec10'# api key of tuling robot
def get_response(msg = 'hello'):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    dic = {
        'key': key,
        'info': msg,
        'userid': 'wechat-robot'}
    try: # if it cannot find a proper response, then it will return None
        r = requests.post(apiUrl, data=dic).json()
        return r['text']

    except:
        return

@itchat.msg_register(itchat.content.TEXT) # get the permission of Wechat

def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload = True)
itchat.run()

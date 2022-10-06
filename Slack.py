import json
import requests

slack_token = "xoxb-4086374154501-4112819128598-Pseql8OaRiVd6WJKZmfLPqBW"

slack_channel = "testepy"

slack_user_name = "Teste Py"


def post_message_to_slack(text: object, blocks: object = None) -> object:
    return requests.post('https://slack.com/api/chat.postMessage',
                         dict(token=slack_token, channel=slack_channel, text=text, username=slack_user_name,
                              blocks=json.dumps(blocks) if blocks else None)).json()
slack_info: str = 'Olá, segue Farol De Transferências De Ruptura'

def codigo_etl(slack_info=None):
    try:
        codigo_etl()

        assert isinstance(slack_info, object)
        post_message_to_slack(slack_info)
    except:
        'Encontramos problemas ao atualizar os dados:'


post_message_to_slack(slack_info)
print("Farol Enviado Com Sucesso")

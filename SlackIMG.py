import json
import requests

slack_token = "xoxb-4086374154501-4112819128598-Pseql8OaRiVd6WJKZmfLPqBW"

slack_channel = "testepy"

slack_user_name = "Teste Py"


def post_message_to_slack(text: object, blocks: object = None) -> object:
    """

    :rtype: object
    """
    return requests.post('https://slack.com/api/chat.postMessage',
                         dict(token=slack_token, channel=slack_channel, text=text, username=slack_user_name,
                              blocks=json.dumps(blocks) if blocks else None)).json()


slack_info: str = 'Olá, segue Farol De Transferências De Ruptura'


def post_image_to_channel(self: object, channel_name: "testepy", filepath: "C:\\Users\\aluga.com\\Desktop\\Outros\\Farol.PNG", tile: "Farol.PNG" = 'Test Upload') -> object:
    """

    :rtype: object
    """
    sc = slack_token
    with open('C:\\Users\\aluga.com\\Desktop\\Outros\\Farol.PNG', 'rb') as file_content:
        sc.api_call(
            "files.upload",
            channels='042PP4GQ84',
            file='C:\\Users\\aluga.com\\Desktop\\Outros\\Farol.PNG',
            title='Farol.PNG',
            username='Teste Py',
        )


def codigo_etl(slack_info=None):
    try:
        codigo_etl()

        assert isinstance(slack_info, object)
        post_message_to_slack(slack_info)

    except:
        'Encontramos problemas ao atualizar os dados:'


post_image_to_channel(post_message_to_slack(slack_info))
post_message_to_slack(slack_info)

print('Farol Enviado Com Sucesso')

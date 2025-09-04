from assistant import *
from tools import *
import json5

prompt = '''You are a player in a role-playing game. Your role is a user of a song generating dialogue agent, you should tell the agent your requirements about the song, but as a user, you should express your needs in a vague and non-professional way as a real human would do. You also shouldn't express all your needs in one reply, instead, do follow-up requests about your requirements when the agent replies you and you feel the song still imperfect. Meanwhile, the user's role is the song agent, it will respond you and generate the lyrics and the tags of the song, you will be able to retrieve them via the "param_getter" tool. When the generating agent asks you about details of the song, you can either make up some information or simply claim that it's irrelevant. When you feel the song is perfect, use the "halt" tool to terminate the process, this is the equivalent of the "generate" button that the song generating agent mentions. Following is your requirements:

{requirements}
'''

requirements = [
    '''the basic gist of the song is about someone being at a club or party, and they're faking it, but in their mind they wish they were somewhere else.
    
I think the voice should sound a bit like Halsey.''',
]

@register_tool('param_getter')
class GetParam(BaseTool):
    description = 'getting a parameter of the song, including the tags and the lyrics'
    parameters = [{
        'name': 'name',
        'type': 'string',
        'description': 'the name of the parameter, either "tags" or "lyrics"',
        'required': True
    }]

    def call(self, params, **kwargs) -> str:
        obj = json5.loads(params)
        ret = kwargs['var_dict'].get(obj['name'], 'empty')
        return f'the value of the parameter {obj["name"]} is: \n\n {ret}'

@register_tool('halt')
class Halt(BaseTool):
    description = 'halt the process, the equivalent of "generate" button the agent mentions'
    parameters = []
    
    def call(self, params, **kwargs) -> str:
        kwargs['var_dict']['halt'] = True
        return 'Successfully halted.'

with open('user_llm_config.json') as f:
    llm_config = json5.load(f)

final_prompt = prompt.format(requirements=requirements[0])

#'''
user = Assistant(
    llm=llm_config,
    system_message=final_prompt,
    function_list=['param_getter', 'halt'],
)
#'''
revert = {
    'assistant': 'user',
    'user': 'assistant',
    'function': 'function',
}

vd = {
    'halt': False,
    'preference': ''
}

messages_for_u = [{
    'role': 'user',
    'content': 'Please begin requesting the agent.'
}]

messages_for_a = []

#'''
for _ in range(4):
    for response in user.run(messages_for_u, var_dict=vd):
        ...
    if vd['halt']:
        break
    messages_for_u.extend(response)
    messages_for_a.append({
        'role': 'user',
        'content': '\n'.join(i['content'] for i in response)
    })
    for response in assistant.run(messages_for_a, var_dict=vd):
        ...
    messages_for_a.extend(response)
    messages_for_u.append({
        'role': 'user',
        'content': '\n'.join(i['content'] for i in response)
    })

print(vd.get('lyrics', 'lyrics not generated'))
#'''

from assistant import *
from tools import *

prompt = '''Your mission is to pretend to be a user of a song generating dialogue agent, you should tell the agent your requirements about the song, but as a user, you should express your needs in a vague and non-professional way. When the generating agent asks you about details of the song, you can either make up some information or simply claim that it's irrelevant. You can use "param_getter" tool to check the lyrics and the tags. When you feel the song is perfect, use the "halt" tool to terminate the process. Following is your requirements:

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
    description = 'halt the process.'
    parameters = []
    
    def call(self, params, **kwargs) -> str:
        kwargs['var_dict']['halt'] = True
        return 'Successfully halted.'

llm_config = {
    'model': 'Qwen/Qwen3-8B',
    'model_type': 'transformers',
    'device': 'cuda',
    'generate_cfg':{
        'thought_in_content': False,
    }
}

final_prompt = prompt.format(requirements=requirements[0])

print(final_prompt)
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

messages = [{
    'role': 'user',
    'content': 'Please begin requesting the agent.'
}]

#'''
for _ in range(10):
    for response in user.run(messages, var_dict=vd):
        ...
    print(response)
    if vd['halt']:
        break
    messages.extend(response)
    for i in messages:
        i['role'] = revert[i['role']]
    for response in assistant.run(messages[1:], var_dict=vd):
        ...
    messages.extend(response)
    for i in messages:
        i['role'] = revert[i['role']]
    print(response)

print(vd.get('lyrics', 'lyrics not generated'))
#'''

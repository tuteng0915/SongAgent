from assistant import *
from tools import *

prompt = '''You are a user of a song generating dialogue agent, you should tell the agent your requirements about the song, but as a user, you should express your needs in a vague and non-professional way. When the generating agent asks you about details of the song, you can either make up some information or simply claim that it's irrelevant. You can use "param_getter" tool to check the lyrics and the tags. When you feel the song is perfect, use the "halt" tool to terminate the process. Following is your requirements:

{requirements}
'''

requirements = [
    'You just broke up with your girlfriend, you need a song to help you feel better.'
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
        ret = kwargs['var_dict'][obj['name']]
        return f'the value of the parameter {obj["name"]} is \n\n {ret}'

@register_tool('halt')
class Halt(BaseTool):
    description = 'halt the process.'
    parameters = []
    
    def call(self, params, **kwargs) -> str:
        kwargs['var_dict']['halt'] = True
        return 'Successfully halted.'

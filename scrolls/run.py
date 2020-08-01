import openai
import os
import json
from collections import namedtuple
import sys


SCROLLS_DIR = os.path.dirname(os.path.realpath(__file__))


def run(name):
    prefix = SCROLLS_DIR+os.path.sep+name
    kwargs = {}
    prompt = open(prefix+'.txt', "r").read()
    if os.path.isfile(prefix+'.json'):
        kwargs_file = open(prefix+'.json', "r").read()
        kwargs = json.loads(kwargs_file)

    response = openai.Completion.create(
            engine="davinci", prompt=prompt, **kwargs)
    return response.choices[0].text



if __name__ == "__main__":
    import sys
    print(run(sys.argv[1]))

class run_callable:
    def __call__(self, name):
        return run(name)


sys.modules[__name__] = run_callable()


import os
import glob

import env

def format(content):

    '''
    format the provided generic file for the specific `user`
    '''

    return content.format(username=env.USERNAME, projectdir=env.PROJECTDIR,
                          venvdir=env.VENVDIR, workers=env.WORKERS)

def build(content, filename):

    '''
    generate config file for specific `user` after the template
    is processed in format function
    '''

    filename = '.'.join(token for token in filename.split('.') if token != 'template')
    with open(f'./scripts/{filename}', 'w+') as config:
        config.write(content)

for template in glob.glob('./templates/*.template'):
    with open(template, 'r') as content:
        filename = os.path.basename(template)
        build(format(content.read()), filename)


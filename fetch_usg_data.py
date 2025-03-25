import iatikit
iatikit.download.data()
import os, shutil
relevant_usg_publishers = [
    'dfc',
    'dhs',
    'doc',
    'dod',
    'doe',
    'doi',
    'doj',
    'dol',
    'dot',
    'epa',
    'ftc',
    'hhs',
    'iaf',
    'millenniumchallenge',
    'peace',
    'state',
    'treasury',
    'usadf',
    'usaid',
    'usda',
    'ustda'
]
for publisher in relevant_usg_publishers:
    shutil.copytree(f'__iatikitcache__/registry/data/{publisher}', f'output/data/{publisher}')
    shutil.copytree(f'__iatikitcache__/registry/metadata/{publisher}', f'output/metadata/{publisher}')
    shutil.copyfile(f'__iatikitcache__/registry/metadata/{publisher}.json', f'output/metadata/{publisher}.json')
shutil.copyfile('__iatikitcache__/registry/metadata.json', 'output/metadata/metadata.json')

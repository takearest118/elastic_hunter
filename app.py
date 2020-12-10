# -*- coding: utf-8 -*-


import json
from datetime import datetime
from pprint import pprint

from elasticsearch import Elasticsearch
import click


ES_URL = 'https://search-dev-lab981-5wuk4tks57oddtcqm2qddbssqq.ap-northeast-2.es.amazonaws.com'
INDEX = 'lab981-admin-*'
# INDEX = 'lab981-admin-2020.06.01'
FROM = 0
CHUNK = 1000

@click.command()
@click.option('--host', '-h', type=click.STRING, required=True, default=ES_URL, help='host of elasticsearch(include port number)')
@click.option('--index', '-i', type=click.STRING, required=True, default=INDEX, help='index name')
@click.option('--output', '-o', type=click.STRING, required=True, help='ouput filename')
@click.option('--verbose', '-v', is_flag=True, help='verbose message')
def export(host, index, output, verbose):
    print('Elastic Hunter')
    sdt = datetime.now()
    es = Elasticsearch(host)
    res = es.count(index=index)
    count = res['count']
    print('host name: {}'.format(host))
    print('index name: {}'.format(index))
    print('count of document on index: {}'.format(count))
    if verbose:
        pprint(es)
        pprint(es.info())
    with open(output, 'w') as fp:
        for i in range(FROM, count, CHUNK):
            res = es.search(index=index, body={}, from_=i, size=CHUNK)
            pprint(res) if verbose else None
            docs = res['hits']['hits']
            for i in docs:
                fp.write('%s\n' % json.dumps(i['_source']))
    es.close()
    fdt = datetime.now()
    print('elaspsed time: {}'.format(fdt-sdt))
    print("Done")


if __name__=='__main__':
    export()

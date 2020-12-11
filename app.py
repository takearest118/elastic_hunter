# -*- coding: utf-8 -*-


import time
import json
from datetime import datetime
from pprint import pprint

from elasticsearch import Elasticsearch
import click


ES_URL = 'localhost'
FROM = 0
CHUNK = 1000


@click.group()
def cli():
    pass


@click.command(help='export json format from elasticsearch')
@click.option('--host', '-h', type=click.STRING, required=True, default=ES_URL, help='host of elasticsearch(include port number)')
@click.option('--index', '-i', type=click.STRING, required=True, help='index name')
@click.option('--file', '-f', type=click.STRING, required=True, help='ouput filename')
@click.option('--verbose', '-v', is_flag=True, help='verbose message')
def exporter(host, index, file, verbose):
    print('Elastic Hunter')
    start_dt = datetime.now()
    es = Elasticsearch(host)
    res = es.count(index=index)
    count = res['count']
    print('host name: {}'.format(host))
    print('index name: {}'.format(index))
    print('count of document on index: {}'.format(count))
    if verbose:
        pprint(es)
        pprint(es.info())
    with open(file, 'w') as fp:
        for i in range(FROM, count, CHUNK):
            res = es.search(index=index, body={}, from_=i, size=CHUNK)
            pprint(res) if verbose else None
            docs = res['hits']['hits']
            for i in docs:
                fp.write('%s\n' % json.dumps(i['_source']))
    es.close()
    finish_dt = datetime.now()
    print('elaspsed time: {}'.format(finish_dt-start_dt))
    print("Done")


@click.command(help='import json format into elasticsearch')
@click.option('--host', '-h', type=click.STRING, required=True, default=ES_URL, help='host of elasticsearch(include port number)')
@click.option('--index', '-i', type=click.STRING, required=True, help='index name')
@click.option('--file', '-f', type=click.STRING, required=True, help='input filename')
@click.option('--verbose', '-v', is_flag=True, help='verbose message')
def importer(host, index, file, verbose):
    print('Elastic Hunter')
    start_dt = datetime.now()
    es = Elasticsearch(host)
    print('host name: {}'.format(host))
    print('index name: {}'.format(index))
    if verbose:
        pprint(es)
        pprint(es.info())
    with open(file, 'r') as fp:
        for line in fp.readlines():
            body = json.loads(line)
            res = es.index(index=index, body=body)
            if verbose:
                pprint(body)
                pprint(res)
    time.sleep(5)
    res = es.count(index=index)
    count = res['count']
    print('count of document on index: {}'.format(count))
    es.close()
    finish_dt = datetime.now()
    print('elaspsed time: {}'.format(finish_dt-start_dt))
    print("Done")


cli.add_command(exporter)
cli.add_command(importer)


if __name__=='__main__':
    cli()


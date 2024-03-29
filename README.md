# elastic_hunter [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/takearest118/elastic_hunter)

<img align="right" width="200" src="https://www.monsterhunter.com/world-iceborne/assets/img/common/top/monster_bg.jpg">

You can export and import json files in Elasticsearch, manage data in elasticsearch by json format. Enjoy your data hunting.

## requirements
- Python 3.5+
- elasticsearch
- click

## help

```
% python3 app.py --help
Usage: app.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  exporter  export json format from elasticsearch
  importer  import json format into elasticsearch
  scroll-exporter  export json format from elasticsearch by scroll api (for...

```

### exporter command

```
% python3 app.py exporter --help
Usage: app.py exporter [OPTIONS]

  export json format from elasticsearch

Options:
  -h, --host TEXT   host of elasticsearch(include port number)  [required]
  -i, --index TEXT  index name  [required]
  -f, --file TEXT   ouput filename  [required]
  -v, --verbose     verbose message
  --help            Show this message and exit.

```

sample usage
> python3 app.py exporter -h localhost -i test-index -f test.json

### importer command

```
% python3 app.py importer --help
Usage: app.py importer [OPTIONS]

  import json format into elasticsearch

Options:
  -h, --host TEXT   host of elasticsearch(include port number)  [required]
  -i, --index TEXT  index name  [required]
  -f, --file TEXT   input filename  [required]
  -v, --verbose     verbose message
  --help            Show this message and exit.

```

sample usage
> python3 app.py importer -h localhost -i test-index -f test.json

### scroll exporter command

```
% python app.py scroll-exporter --help
Usage: app.py scroll-exporter [OPTIONS]

  export json format from elasticsearch by scroll api (for large index)

Options:
  -h, --host TEXT   host of elasticsearch(include port number)  [required]
  -i, --index TEXT  index name  [required]
  -f, --file TEXT   ouput filename
  -v, --verbose     verbose message
  --help            Show this message and exit.

```

sample usage
> python3 app.py scroll-exporter -h localhost -i test-index -f test.json

## json file format

```
{"monster_id": 1, "name": "elastic_hunter", "count": 13, "timestamp": "2020-12-09T21:20:26"}
{"monster_id": 2, "name": "python", "count": 3, "timestamp": "2020-12-10T21:20:26"}
{"monster_id": 3, "name": "sanic", "count": 11, "timestamp": "2020-12-11T21:20:26"}
{"monster_id": 4, "name": "konhee", "count": 7, "timestamp": "2020-12-12T00:20:26"}
{"monster_id": 5, "name": "nargacuga", "count": 17, "timestamp": "2020-12-13T21:20:26"}
{"monster_id": 6, "name": "nergigante", "count": 21, "timestamp": "2020-12-21T21:20:26"}
{"monster_id": 7, "name": "safijiiva", "count": 109, "timestamp": "2020-12-21T21:20:26"}
{"monster_id": 8, "name": "fatalis", "count": 137, "timestamp": "2020-12-31T23:20:11"}

...
...

```

## License

[GNU General Public License v2.0](./LICENSE)


Elasticsearch:

Elasticsearch is a highly scalable open-source full-text search and analytics engine. It allows you to store, search, and analyze big volumes of data quickly and in near real time.

Cluster:A cluster is a collection of one or more nodes (servers) that together holds your entire data and provides federated indexing and search capabilities across all nodes.

Node:A node is a single server that is part of your cluster, stores your data, and participates in the cluster’s indexing and search capabilities.

Index: An index is a collection of documents that have somewhat similar characteristics. 

Type: is a logical partition of index

Document:  A document is a basic unit of information that can be indexed.

Shards:  An index can potentially store a large amount of data that can exceed the hardware limits of a single node.To solve this problem, Elasticsearch provides the ability to subdivide your index into multiple pieces called shards. 
**Sharding is important for two primary reasons:
It allows you to horizontally split/scale your content volume
It allows you to distribute and parallelize operations across shards (potentially on multiple nodes) thus increasing performance/throughput

Replica:
Elasticsearch allows you to make one or more copies of your index’s shards called replica. 
**Replication is important for two primary reasons:
It provides high availability in case a shard/node fails.
It allows you to scale out your search volume/throughput since searches can be executed on all replicas in parallel.

Installation: https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html

   1  echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
    2  sudo apt-get update
    3  sudo apt-get install elasticsearch
    4  apt-get install elasticsearch
    5  add-apt-repository ppa:openjdk-r/ppa --yes
    6  apt-get install openjdk-8-jre openjdk-8-jre-headless openjdk-8-jdk --yes
    7  apt-get install elasticsearch
    8  vi /etc/elasticsearch/elasticsearch.yml
    9  sudo systemctl start elasticsearch
   10  sudo systemctl enable elasticsearch

sudo systemctl restart elasticsearch
/etc/elasticsearch/elasticsearch.yml -- configuration 

path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch
discovery.zen.ping.unicast.hosts: ["publicip", "esmaster-0", "esmaster-1"]
http.host: 0.0.0.0

Set custom port:

http.port: 9200
transport.tcp.port: 9300



List all index:
GET /_cat/indices?v
Create an Index:
PUT http://elasticsearch:port/indexname
{
        "settings": {
                "index": {
                        "number_of_shards": 3,
                        "number_of_replicas": 2
                }
        },

        "mappings": {
                "node_details": {
                        "properties": {
                                "timestamp": {
                                        "type": "date",
                                        "format": "epoch_millis||epoch_second"
                                }
                        }
                }
        }

}

Delete an index:
DELETE http://elasticsearch:port/indexname

Add/push data into an index:
POST http://elasticsearch:port/indexname/_doc/$today

Loading sample dataset:
accounts.json
{
    "account_number": 0,
    "balance": 16623,
    "firstname": "Bradshaw",
    "lastname": "Mckenzie",
    "age": 29,
    "gender": "F",
    "address": "244 Columbus Place",
    "employer": "Euron",
    "email": "bradshawmckenzie@euron.com",
    "city": "Hobucken",
    "state": "CO"
}

curl -H "Content-Type: application/json" -XPOST "localhost:9200/bank/_doc/_bulk?pretty&refresh" --data-binary "@accounts.json"
curl "localhost:9200/_cat/indices?v"

Search data:
GET /bank/_search

awscurl -XPUT "ESURL/mdsp-az-jenkins" --secret_key $AWS_SECRET_ACCESS_KEY --session_token $AWS_SECURITY_TOKEN --access_key $AWS_ACCESS_KEY_ID --service es -d'
{
        "settings": {
                "index": {
                        "number_of_shards": 3,
                        "number_of_replicas": 2
                }
        },
        "mappings": {
                "node_details": {
                        "properties": {
                                "timestamp": {
                                        "type": "date",
                                        "format": "epoch_millis||epoch_second"
                                },
                                "@envname":{
                                                "type":"keyword"
                                },
                                "node_status":{
                                                "type":"integer"
                                },
                                "user":{
                                                "type":"integer"
                                },
                                "activesp":{
                                                "type":"integer"
                                }
                        }
                }
        }
}'


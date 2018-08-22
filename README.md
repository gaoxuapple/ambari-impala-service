An Ambari Service for Impala
====

## Support Version
- Impala 2.6 +
- Hadoop 2.6 +

## Install Impala two ways:

### 1. To download the Impala service folder, run below    

```
VERSION=`hdp-select status hadoop-client | sed 's/hadoop-client - \([0-9]\.[0-9]\).*/\1/'`
sudo git clone https://github.com/gaoxuapple/ambari-impala-service.git /var/lib/ambari-server/resources/stacks/HDP/$VERSION/services/IMPALA
```

### 2. MPACK 
```
ambari-server install-mpack --mpack=ambari-impala-mpack-2.6.0-0816.tar.gz -v
```

## local repository
Make your local repository.Download software from https://cloudera.proxy.ustclug.org/cdh5/redhat/7/x86_64/cdh/5

software list as below:
```
avro-doc-1.7.6+cdh5.15.0+140-1.cdh5.15.0.p0.52.el7.noarch.rpm
avro-libs-1.7.6+cdh5.15.0+140-1.cdh5.15.0.p0.52.el7.noarch.rpm
avro-tools-1.7.6+cdh5.15.0+140-1.cdh5.15.0.p0.52.el7.noarch.rpm
bigtop-jsvc-0.6.0+cdh5.15.0+925-1.cdh5.15.0.p0.52.el7.x86_64.rpm
bigtop-jsvc-debuginfo-0.6.0+cdh5.15.0+925-1.cdh5.15.0.p0.52.el7.x86_64.rpm
bigtop-utils-0.7.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.noarch.rpm
hbase-1.2.0+cdh5.15.0+461-1.cdh5.15.0.p0.52.el7.x86_64.rpm
hbase-doc-1.2.0+cdh5.15.0+461-1.cdh5.15.0.p0.52.el7.x86_64.rpm
hbase-master-1.2.0+cdh5.15.0+461-1.cdh5.15.0.p0.52.el7.x86_64.rpm
hbase-regionserver-1.2.0+cdh5.15.0+461-1.cdh5.15.0.p0.52.el7.x86_64.rpm
hbase-rest-1.2.0+cdh5.15.0+461-1.cdh5.15.0.p0.52.el7.x86_64.rpm
hbase-thrift-1.2.0+cdh5.15.0+461-1.cdh5.15.0.p0.52.el7.x86_64.rpm
hive-1.1.0+cdh5.15.0+1373-1.cdh5.15.0.p0.52.el7.noarch.rpm
hive-hbase-1.1.0+cdh5.15.0+1373-1.cdh5.15.0.p0.52.el7.noarch.rpm
hive-hcatalog-1.1.0+cdh5.15.0+1373-1.cdh5.15.0.p0.52.el7.noarch.rpm
hive-jdbc-1.1.0+cdh5.15.0+1373-1.cdh5.15.0.p0.52.el7.noarch.rpm
hive-metastore-1.1.0+cdh5.15.0+1373-1.cdh5.15.0.p0.52.el7.noarch.rpm
hive-server-1.1.0+cdh5.15.0+1373-1.cdh5.15.0.p0.52.el7.noarch.rpm
hive-server2-1.1.0+cdh5.15.0+1373-1.cdh5.15.0.p0.52.el7.noarch.rpm
hive-webhcat-1.1.0+cdh5.15.0+1373-1.cdh5.15.0.p0.52.el7.noarch.rpm
hive-webhcat-server-1.1.0+cdh5.15.0+1373-1.cdh5.15.0.p0.52.el7.noarch.rpm
impala-2.12.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.x86_64.rpm
impala-catalog-2.12.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.x86_64.rpm
impala-debuginfo-2.12.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.x86_64.rpm
impala-server-2.12.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.x86_64.rpm
impala-shell-2.12.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.x86_64.rpm
impala-state-store-2.12.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.x86_64.rpm
impala-udf-devel-2.12.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.x86_64.rpm
parquet-1.5.0+cdh5.15.0+196-1.cdh5.15.0.p0.52.el7.noarch.rpm
parquet-format-2.1.0+cdh5.15.0+20-1.cdh5.15.0.p0.52.el7.noarch.rpm
sentry-1.5.1+cdh5.15.0+444-1.cdh5.15.0.p0.52.el7.noarch.rpm
sentry-hdfs-plugin-1.5.1+cdh5.15.0+444-1.cdh5.15.0.p0.52.el7.noarch.rpm
sentry-store-1.5.1+cdh5.15.0+444-1.cdh5.15.0.p0.52.el7.noarch.rpm
solr-4.10.3+cdh5.15.0+524-1.cdh5.15.0.p0.52.el7.noarch.rpm
solr-crunch-1.0.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.noarch.rpm
solr-doc-4.10.3+cdh5.15.0+524-1.cdh5.15.0.p0.52.el7.noarch.rpm
solr-mapreduce-1.0.0+cdh5.15.0+0-1.cdh5.15.0.p0.52.el7.noarch.rpm
solr-server-4.10.3+cdh5.15.0+524-1.cdh5.15.0.p0.52.el7.noarch.rpm
```

## Restart Ambari  
sudo service ambari-server restart


## HDFS config
we need add below config to /etc/hadoop/conf/core-site.xml
```
<property>
    <name>dfs.client.read.shortcircuit</name> 
   <value>true</value>
</property>

<property>
    <name>dfs.client.read.shortcircuit.skip.checksum</name>
        <value>false</value>
</property>

<property> 
    <name>dfs.datanode.hdfs-blocks-metadata.enabled</name> 
    <value>true</value>
</property>
```
we need add below config to /etc/hadoop/conf/hdfs-site.xml
```
<property>
    <name>dfs.datanode.hdfs-blocks-metadata.enabled</name> 
    <value>true</value>
</property>
<property> 
    <name>dfs.block.local-path-access.user</name> 
    <value>impala</value>
</property>
<property>
    <name>dfs.client.file-block-storage-locations.timeout.millis</name>
    <value>60000</value>
</property>
```
add config info through webui

![Image](../master/screenshots/core-site.png?raw=true)
![Image](../master/screenshots/hdfs-site.png?raw=true)

restart hadoop and restart impala

## SUMMARY
![Image](../master/screenshots/summary.png?raw=true)

## NOTICE
- make sure your hive server normally
- hdfs and hive conf file is sync to /etc/impala/conf

## Some error note:
- NoSuchMethodError:setCaching
![Image](../master/screenshots/impala-error.png?raw=true)
Impala rely on Cloudrea Hbase Jar ,please use relevant jar.
Download relevant jar from https://repository.cloudera.com/artifactory/cloudera-repos/org/apache/hbase/

Jar list as below:
```
hbase-annotations-1.2.0-cdh5.15.0.jar
hbase-client-1.2.0-cdh5.15.0.jar
hbase-common-1.2.0-cdh5.15.0.jar
hbase-examples-1.2.0-cdh5.15.0.jar
hbase-external-blockcache-1.2.0-cdh5.15.0.jar
hbase-hadoop2-compat-1.2.0-cdh5.15.0.jar
hbase-hadoop-compat-1.2.0-cdh5.15.0.jar
hbase-it-1.2.0-cdh5.15.0.jar
hbase-prefix-tree-1.2.0-cdh5.15.0.jar
hbase-procedure-1.2.0-cdh5.15.0.jar
hbase-protocol-1.2.0-cdh5.15.0.jar
hbase-resource-bundle-1.2.0-cdh5.15.0.jar
hbase-rest-1.2.0-cdh5.15.0.jar
hbase-rsgroup-1.2.0-cdh5.15.0.jar
hbase-server-1.2.0-cdh5.15.0.jar
hbase-shell-1.2.0-cdh5.15.0.jar
hbase-spark-1.2.0-cdh5.15.0.jar
hbase-thrift-1.2.0-cdh5.15.0.jar
```

Get into /usr/lib/impala/lib/ folder.
Delete invalid soft connections:
```
rm -rf hbase-annotations.jar
rm -rf hbase-client.jar
rm -rf hbase-common.jar
rm -rf hbase-protocol.jar
rm -rf hive-cli.jar
rm -rf hive-hcatalog-core.jar
rm -rf hive-hcatalog-server-extensions.jar
```

Regenerate soft connections:
```
ln -s hbase-annotations-1.2.0-cdh5.15.0.jar hbase-annotations.jar
ln -s hbase-client-1.2.0-cdh5.15.0.jar hbase-client.jar
ln -s hbase-common-1.2.0-cdh5.15.0.jar hbase-common.jar
ln -s hbase-examples-1.2.0-cdh5.15.0.jar hbase-examples.jar
ln -s hbase-external-blockcache-1.2.0-cdh5.15.0.jar hbase-external-blockcache.jar
ln -s hbase-hadoop2-compat-1.2.0-cdh5.15.0.jar hbase-hadoop2-compat.jar
ln -s hbase-hadoop-compat-1.2.0-cdh5.15.0.jar hbase-hadoop-compat.jar
ln -s hbase-it-1.2.0-cdh5.15.0.jar hbase-it.jar
ln -s hbase-prefix-tree-1.2.0-cdh5.15.0.jar hbase-prefix-tree.jar
ln -s hbase-procedure-1.2.0-cdh5.15.0.jar hbase-procedure.jar
ln -s hbase-protocol-1.2.0-cdh5.15.0.jar hbase-protocol.jar
ln -s hbase-resource-bundle-1.2.0-cdh5.15.0.jar hbase-resource-bundle.jar
ln -s hbase-rest-1.2.0-cdh5.15.0.jar hbase-rest.jar
ln -s hbase-rsgroup-1.2.0-cdh5.15.0.jar hbase-rsgroup.jar
ln -s hbase-server-1.2.0-cdh5.15.0.jar hbase-server.jar
ln -s hbase-shell-1.2.0-cdh5.15.0.jar hbase-shell.jar
ln -s hbase-spark-1.2.0-cdh5.15.0.jar hbase-spark.jar
ln -s hbase-thrift-1.2.0-cdh5.15.0.jar hbase-thrift.jar

ln -s /usr/hdp/2.6.5.0-292/hadoop-mapreduce/hadoop-archives.jar hadoop-archives.jar
ln -s /usr/hdp/2.6.5.0-292/hive-hcatalog/share/hcatalog/hive-hcatalog-core.jar hive-hcatalog-core.jar
ln -s /usr/hdp/2.6.5.0-292/hive-hcatalog/share/hcatalog/hive-hcatalog-server-extensions.jar hive-hcatalog-server-extensions.jar
ln -s /usr/hdp/2.6.5.0-292/hive/lib/hive-cli.jar hive-cli.jar
```


## Impala-shell test:
- Test whether impala is available.
![Image](../master/screenshots/impala-shell.png?raw=true)







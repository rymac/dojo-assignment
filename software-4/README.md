```
$ git clone http://github.com/Netflix/SimianArmy.git
$ wc -l `find SimianArmy/src/main -type f` | sort -n -r | head -10
   23287 total
     987 SimianArmy/src/main/java/com/netflix/simianarmy/client/aws/AWSClient.java
     608 SimianArmy/src/main/java/com/netflix/simianarmy/basic/janitor/BasicJanitorMonkeyContext.java
     557 SimianArmy/src/main/java/com/netflix/simianarmy/aws/AWSResource.java
     535 SimianArmy/src/main/java/com/netflix/simianarmy/aws/janitor/crawler/edda/EddaImageJanitorCrawler.java
     492 SimianArmy/src/main/java/com/netflix/simianarmy/basic/BasicSimianArmyContext.java
     486 SimianArmy/src/main/java/com/netflix/simianarmy/janitor/AbstractJanitor.java
     455 SimianArmy/src/main/java/com/netflix/simianarmy/basic/chaos/BasicChaosMonkey.java
     392 SimianArmy/src/main/java/com/netflix/simianarmy/aws/janitor/RDSJanitorResourceTracker.java
     385 SimianArmy/src/main/java/com/netflix/simianarmy/Resource.java
$ wc -l `find SimianArmy/src/main -type f` | sort -n -r | head -10 | grep -i chaos
     455 SimianArmy/src/main/java/com/netflix/simianarmy/basic/chaos/BasicChaosMonkey.java
```

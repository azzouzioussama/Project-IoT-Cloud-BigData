# Guide de Configuration du Projet 

Ce guide couvre l'installation de RabbitMQ, Hadoop et Kafka sur Ubuntu. Suivez ces étapes pour configurer votre environnement de développement.

## Installation de RabbitMQ

1. **Mettre à jour les paquets** :
  - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/67404e5d-4ab9-49d9-95f8-8295c71d9aa6)


2. **Installer RabbitMQ** :
  - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/1debc304-ccee-4755-9b00-6ad4001cc9db)


3. **Démarrer le service RabbitMQ** :
  - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/ea441f5c-f6d7-4cb0-8a7f-abaf149eed35)


4. **Vérifier le statut du service RabbitMQ** :
  - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/7697fec9-05b1-40c6-8120-4edc07b6718e)


## Installation de Hadoop

1. **Mettre à jour le système** :
  - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/dd557692-573b-430f-88ea-3c1618932e28)


2. **Télécharger et extraire Hadoop** :
  - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/2a1e6439-33a0-4486-93ad-391b10a14899)


3. **Configurer les variables d'environnement** :
   - Ajoutez les variables d'environnement nécessaires dans votre fichier `~/.bashrc` ou `~/.zshrc`, en fonction de votre shell.
   - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/c5486954-99b0-4016-9316-60f14adc1109)
   - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/525c9e38-4a30-4579-8c44-99d725e9787f)



4. **Configurer Hadoop** :
   - Modifiez les fichiers de configuration de Hadoop situés dans `$HADOOP_HOME/etc/hadoop/` pour les adapter à votre configuration.

5. **Démarrer les services Hadoop** :
   - Démarrez les services Hadoop à l'aide des commandes fournies.
   - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/9636aabc-c36c-44fd-bc40-1e6ba1c9409a)


6. **Vérifier l'installation** :
   - Accédez à l'interface web de Hadoop à `http://localhost:9870` pour le gestionnaire de nœuds HDFS et `http://localhost:8088` pour le gestionnaire de ressources YARN afin de confirmer son bon fonctionnement.

## Installation de Kafka

1. **Prérequis** :
   - Assurez-vous que Java 8 ou supérieur est installé sur votre machine.
   - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/ea3e1fab-ec7d-4ef1-b014-4c5c3fc16b97)


2. **Téléchargement de Kafka** :
   - Téléchargez la dernière version de Kafka depuis le site web Apache Kafka.
   - https://kafka.apache.org/downloads
   - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/a2e76ab3-47c8-4224-83cd-becf22d72707)
   - Assurez-vous de remplacer <version> par le numéro de version réel. Par exemple:
   - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/9d4011b2-c2d2-4f41-9983-4555115ef917)


3. **Démarrage de Zookeeper** :
   - Kafka nécessite Zookeeper. Démarrez Zookeeper à l'aide de la commande fournie dans le guide.
   - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/8dd73577-0700-40ea-9bf5-6c1844a7caca)


4. **Démarrage du serveur Kafka** :
   - Ouvrez un autre terminal et démarrez le serveur Kafka avec la commande fournie.
   - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/5ea347df-2315-4d3c-9f64-ca3e5648ec87)
   - ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/d1aeaf5a-909d-4fca-8bff-4cc5fb9437e9)

# Installation Guides

## Installation de Cassandra

1. **Mise à jour du système** : Commencez par mettre à jour le cache de votre gestionnaire de paquets et les paquets de votre système.
2. **Installation de Java** : Apache Cassandra nécessite Java pour fonctionner. Installez OpenJDK avec la commande appropriée ou vérifiez la version de Java installée si déjà présente.
3. **Téléchargement de Cassandra** : Utilisez `curl` pour télécharger la dernière version de Cassandra.
4. **Vérification de l'intégrité** : Vérifiez l'intégrité du téléchargement avec les commandes appropriées pour le fichier SHA256.
5. **Extraction et démarrage** : Extrayez l'archive Cassandra et démarrez le serveur en accédant au répertoire de Cassandra.

## Installation de MongoDB

1. **Mise à jour des packages systèmes** : Vérifiez et mettez à jour les packages systèmes.
2. **Installation des packages requis** : Installez certains packages nécessaires pour MongoDB.
3. **Ajout de la clé GPG et du référentiel MongoDB** : Pour vérifier l'authenticité et ajouter le référentiel MongoDB, suivez les étapes indiquées.
4. **Installation de MongoDB** : Installez MongoDB, qui comprend le shell du serveur et d'autres outils essentiels.
5. **Démarrage du service MongoDB** : Démarrez le service MongoDB et vérifiez son statut.
6. **Vérification de l'installation** : Vérifiez la version installée de MongoDB pour confirmer sa correcte installation.

## Installation de Spark

1. **Préparation de l'installation** : Mettez à jour la liste des paquets et assurez-vous que Java est correctement installée.
2. **Téléchargement et extraction de Spark** : Utilisez le site web d'Apache Spark pour télécharger Spark et extrayez-le dans le répertoire de votre choix.
3. **Configuration des variables d'environnement** : Configurez les variables d'environnement pour Apache Spark en éditant le fichier `.bashrc`.
4. **Vérification de l'installation** : Lancez le shell Spark pour vérifier que Spark est correctement installé et configuré.

Remplacez les placeholders (par exemple, les chemins ou les commandes spécifiques) par les valeurs réelles applicables à votre installation. Suivez les instructions détaillées et la documentation officielle pour des informations à jour.


Remplacez les espaces réservés (par exemple, `<version>`) par les valeurs réelles pertinentes pour votre installation. Veillez à suivre les liens vers la documentation officielle pour obtenir les instructions les plus à jour et détaillées.

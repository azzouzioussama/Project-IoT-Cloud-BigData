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
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/161ecf3d-9243-48eb-a7c4-e41c4d7661d7)

2. **Installation de Java** : Apache Cassandra nécessite Java pour fonctionner. Installez OpenJDK avec la commande appropriée ou vérifiez la version de Java installée si déjà présente.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/e6c3e756-3476-43b1-a515-9d514f5d1d7d)
  -  Si Java est déjà installé : Vous pouvez vérifier la version de Java installée en utilisant :
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/1cd35bc4-f85e-4b69-a052-b1c666401f8d)


3. **Téléchargement de Cassandra** : Utilisez `curl` pour télécharger la dernière version de Cassandra.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/8bbb58f9-39c3-4ffc-9a7c-1ba7aadf0555)

4. **Vérification de l'intégrité** : Vérifiez l'intégrité du téléchargement avec les commandes appropriées pour le fichier SHA256.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/5bd6d951-91bd-4493-b85d-2254ab082ba2)
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/dc758af4-c524-4220-8e02-f62783066c5e)


5. **Extraction et démarrage** : Extrayez l'archive Cassandra et démarrez le serveur en accédant au répertoire de Cassandra.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/b47c60b7-c751-4aea-ac7c-89aaf1afe5ab)
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/2f448fdf-d1f3-4708-86ee-fd17775ac9af)


## Installation de MongoDB

1. **Mise à jour des packages systèmes** : Vérifiez et mettez à jour les packages systèmes.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/8cbe13cb-9f53-4cbd-b3a4-dafb3be30f0d)

2. **Installation des packages requis** : Installez certains packages nécessaires pour MongoDB.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/263b37dc-ab6e-42b4-8887-a482523954c9)
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/f0dfea0e-2f66-4bc5-8584-a98bbeb88e0b)


3. **Ajout de la clé GPG et du référentiel MongoDB** : Pour vérifier l'authenticité et ajouter le référentiel MongoDB, suivez les étapes indiquées.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/f7d4cc2e-4b2d-42ee-ba43-988f705c9ea0)
  -  Ensuite ajouter le référentiel de mongodb car il n’est pas disponible dans le référentiel système par défaut :
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/fcfedd6f-a8a2-4af8-9127-e95415a21211)
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/ec659816-f42f-49fb-94fe-ba47038d0280)
  -  Mettre à nouveau le système à jour :
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/043239c2-4146-44a6-afc3-6b9ca231f164)


4. **Installation de MongoDB** : Installez MongoDB, qui comprend le shell du serveur et d'autres outils essentiels.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/96d6956f-2e85-4f15-a179-e4d40d83b625)

5. **Démarrage du service MongoDB** : Démarrez le service MongoDB et vérifiez son statut.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/2e2a3ee9-6470-4fed-91a0-f3b26f09b326)
  -  On voit que le service est activé
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/48e7e986-337d-486a-bf98-3510df2625f4)


6. **Vérification de l'installation** : Vérifiez la version installée de MongoDB pour confirmer sa correcte installation.
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/947daa9d-cfdb-4ffd-9625-6fc699090df0)
  -  ![image](https://github.com/azzouzioussama/Project-IoT-Cloud-BigData/assets/78319392/aaf32e1b-47e8-406c-8231-28907e6e0a30)



## Installation de Spark

1. **Préparation de l'installation** : Mettez à jour la liste des paquets et assurez-vous que Java est correctement installée.
  -  
2. **Téléchargement et extraction de Spark** : Utilisez le site web d'Apache Spark pour télécharger Spark et extrayez-le dans le répertoire de votre choix.
  -  
3. **Configuration des variables d'environnement** : Configurez les variables d'environnement pour Apache Spark en éditant le fichier `.bashrc`.
  -  
4. **Vérification de l'installation** : Lancez le shell Spark pour vérifier que Spark est correctement installé et configuré.
  -  

Remplacez les placeholders (par exemple, les chemins ou les commandes spécifiques) par les valeurs réelles applicables à votre installation. Suivez les instructions détaillées et la documentation officielle pour des informations à jour.


Remplacez les espaces réservés (par exemple, `<version>`) par les valeurs réelles pertinentes pour votre installation. Veillez à suivre les liens vers la documentation officielle pour obtenir les instructions les plus à jour et détaillées.

# amyplant-security

## I- Face detection from scratch
#### Database + augmentation
Le but c’est de créer une bdd et annoter des bounding boxes autour du visage sur les image avec la librairie labelme

- Collect Images Using OpenCV = capture images from webcam ==> me mettre out of the screen, cacher les mains visage, en bas en haut
- Annotate Images with LabelMe, create labels = we will draw a bounding box around our head using a library called label me
```
probleme avec labelme : 
$ pip uninstall opencv-python
$ pip install opencv-python-headless
```
- Load Image into TensorFlow Data Pipeline (on a transformé nos images en numpy array)
- Split data : train, test, val (training ⇒ to train, validation partition ⇒ permet d’adapter larchitecture etc, testing ⇒ says how a model has perform)

Une centaine d'image n’est pas assez pour train un modèle de DL donc va faire de l’augmentation. take our dataset, apply random cropping apply random lightness …. nous permet d’avoir 30x le nombre de data de base. nous permet de passer de 100 à 3000 images, ce qui devrait suffire ⇒ augmente pas seulement les images, crée les annotations en meme temps, la bounding box change en meme temps : albumentation.

- Apply image augmentation on images and labels using albumentations = une centaine d’images n’est pas assez pour train un modèle de DL donc on va faire de l’augmentation. take our dataset, apply random cropping apply random lightness …. nous permet d’avoir 30x le nombre de data de base. nous permet de passer de 100 à 3000 images, ce qui devrait suffire
- Load augmented images and labels to tensorflow dataset ==> now we are going to load our images intro a tensorflow dataset. Our training images are going to be inside of a variable called train_image.  randomly crop and adjust our dataset to go from a small dataset to something way larger 30times bigger
- Create final dataset with images and labels
- [basics of bounding boxes](https://medium.com/analytics-vidhya/basics-of-bounding-boxes-94e583b5e16c)

#### Create my own DL model

Là l'objectif c'est de build and train the deep learning model based on the dataset we created = object detection has two parts :  
- classification (=determine what the object is), We are going to use a vgg16 base architecture, and add on our final predictions layers)
- finding the coordinates for the bounding box (=regression problem).  trying to estimate the coordinates of the bounding box : top left, bottom right

- train our model : classification model : tries to classify what type of object is (a face)
- regression model : trying to estimate the coordinates of the bounding box : top left, bottom right
- find the losses : binary cross entropy + localisation loss ==> Keras sequential method expects one input and one output and one loss function. We are going to use the functional api for this model, this will allow us to have two different loss functions and combine them in the end, one for the classification model, and one for the regression model. Combine in localization lost and we will write this function ourselves
- vgg16 is a classification model for images, pretrained on ton of datas already so we can use it inside of our model and add in our final two layers which are going to be our classification model and our regression model to be able to give us a bounding boxes

## II- Gender and age

```

```

## III- Recognition

## IV- Flask App

.wsgi : /var/www/FlaskApp flaskapp.wsgi
__init__.py : /var/www/FlaskApp/FlaskApp __init__.py
create virtual environnement
venv : /var/www/FlaskApp/FlaskApp/venv
.conf : etc/apache2/sites-available/FlaskApp.conf


## V- Deployement

python 3.10.12
Ubuntu 20.04

#### transfer files to VPS ssh
```
scp file root@ip_adress:/var/www/
scp -r directory root@ip_adress:/var/www/
```

#### Déployer une app Flask sur un VPS Ubuntu 
[How To Install the Apache Web Server on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-22-04#step-3-checking-your-web-server)
[How To Deploy a Flask Application on an Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
[mec qui applique le tuto corrige erreurs](https://www.youtube.com/watch?v=7j6Oq9S5V_k&t=700s)
```
tail -f /var/log/apache2/error.log
```

#### sockets to transfer camera frames
But : avoir les frames de la caméra sur le site. Idées : faire tourner le code en local et envoyer que le résultat à imprimer sur le site, create an IP caméra, Use an ipcamera protocol such as RTMP to create a stream, sockets
socket = établir une connexion entre deux machines et transmettre de l’information
- protocole tcp : avec une connexion, on doit etablir une connexion pr pouvoir parler entre les deux, et de manière ordonnée
- un socket de datagramme udp : non connecté, non fiable, plus rapide
```
#### ouvrir le port 9001 sur le VPS
netstat -na | grep :9001 # voir s’il est utilisé
sudo ufw allow 9001
netstat -lntu # lister tous les ports ouverts
```
[tuto](https://www.youtube.com/watch?v=MfIwhxBQAp0)
[tuto autre](https://www.youtube.com/watch?v=Lbfe3-v7yE0)

#### id mdp pour rentrer sur le site
htpasswd -c /etc/apache2/.htpasswd amy
cat /etc/apache2/.htpasswd ⇒ hash version of our password
[tuto add id mdp admin](https://tonyteaches.tech/basic-authentication/)

#### fond bleu foncé

#### Nom de domaine 
Point a Domain to VPS Using the A Record
https://www.hostinger.com/tutorials/dns/how-to-point-domain-to-vps
https://www.youtube.com/watch?v=QcNBLSSn8Vg
DNS de type A, qui pointe vers notre adresse IP 


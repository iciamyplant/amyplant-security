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
Créer le premier site :
/img = on range les images du site
/dossier css = on a range les feuilles de style
/dossier js = pour les animations
index.hmtl = page principale de notre site web, première page sur laquelle les utilisateurs arrivent
```

## III- Recognition

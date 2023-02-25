from fastai.vision.all import *

'SET UP DATA'
#Read dataset and split the data into training & validation
#CIFAR-10 dataset: 60,000 images, each belonging to one of 10 categories
path = untar_data(URLs.CIFAR) #Downloads url and unzips to folder destination

#'DataBlock' class from the FastAI: container for us to build "smart" dataset called "dataloader"
#'Dataloader' contains the 60k images seperated into training & validation + their class
#'Dataloader' specified a pipeline for the model to receive data
#ImageDataLoaders() establish dataloader by passing the path to the dataset and the proportion of the dataset we wish to dedicate to the validation set.
#validation dataset is used to check whether we are actually learning how to classify images / just overfitting
data = ImageDataLoaders.from_folder(path=path, valid_pct=0.2) #0.2 -> 20% of 60k used for validation set


'VALIDATING THE DATASET'
#validate  data to ensure that we have complete dataset
print("Training Set Size = " + str(len(data.train_ds)))
print("Validiation Set Size = " + str(len(data.valid_ds)))
print("Total Dataset Size = " + str(len(data.train_ds) + len(data.valid_ds)))

#Training Set Size = 48000
#Validiation Set Size = 12000
#Total Dataset Size = 60000

#We can also validate dataset by checking a random batch to view the images with their respective labels
data.show_batch(figsize=(10,10)) #10x10 inches


'MODEL SETUP (TRANSFER LEARNING)'
#here, we used a pretrained ResNet-34 (more advanced model) as our base architecture then retraining it to classify our data
learn = cnn_learner(data, resnet34, metrics=accuracy)


'TRAINING'
#determine learning rate, find out how changing our learning rate effects the loss initially
learn.lr_find() #provides the minimum learning rate (divided by 10) and the point of steepest descent

base_lr = 0.15 #determine learning rate from graph above
learn.freeze() #freeze the lower layers, modify top to 'custom fit' the ResNet-34 to the dataset but prevent any weights in the lower layers from being modified until we unfreeze, allowing us to change the final fully connected layers

#train our fully connected layers, This method takes in how many epochs we want to train & learning rate
learn.fit_one_cycle(1, base_lr, pct_start=0.99) #After 1 epoch, we unfreeze the lower layers so that ALL layers can now have their weights updated according to the loss function.
base_lr /= 2
learn.unfreeze()
learn.fit_one_cycle(3, base_lr, pct_start=0.3) #We can then train for another 3 epochs and evaluate the results.
#pct_start=0.3 -> for 30% epoch lr will rise, then slowly decrease last 70%

#Save model weights so we can use or pretrain from it later
learn.save('trained-lr-default')


'EVALUATION'
#view some sample predicitons with our newly trained model
learn.show_results() #Top text is the actual class, bottom text is the predicted class

#Confusion matrix
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()

#produce a set of images that fastai considers 'top losses'
interp.plot_top_losses(8, figsize=(15,11))

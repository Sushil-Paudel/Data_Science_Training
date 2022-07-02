
Tensorflow 2.0 Snippets for VS Code

vscode build-passing build-passing
email release
Type prefix tfk: in Python file to get start with this extension! ( tfk presents tensorflow keras)

This extension includes some snippets to develop a model in your VS Code editor. It requires the minimum version of tensorflow is 2.0. The inside keras package will be used in this extension. For more information, please go to Key Features .

ctrl

Support
While being free and open source, if you find it useful, please consider star us on the repository tensorflow2snippets .

Getting started
The extension requires some usefull packages, such as tensorflow tensorflow-datasets tf-nightly.

pip install tensorflow tf-nightly 
pip install tensorflow-datasets

The visualization tool and some auxiliary tools are also important for you to train a deep learning model.

pip install matplotlib numpy

Key Features
tfk:dataset Field
We write some snippets to help you load the data set easily. But first you must import tensorflow_datasets.

import tensorflow_datasets as tfds

# Image Classification data set
tfk:dataset:mnist 
tfk:dataset:fmnist
tfk:dataset:cifar10 
tfk:dataset:cifar100 
tfk:dataset:imagenet2012
tfk:dataset:celeb_a 


# Object_detection data set
tfk:dataset:coco
tfk:dataset:voc2007

# Structured data set
tfk:dataset:iris

# Generative data set
tfk:dataset:cycle_gan

# Summarization data set
tfk:dataset:scientific_papers

# Text Classification data set
tfk:dataset:scicite

# Language Translate data set
tfk:dataset:flores

# Movies data set
tfk:dataset:moving_mnist

tfk:ctrl Field
This field can help you control the procedure flow more convenience. They generate function like model.fit(...) or class like class model(tf.keras.Model).

tfk:ctrl:model
tfk:ctrl:fit
tfk:ctrl:evaluate
tfk:ctrl:compile
tfk:ctrl:callback
tfk:ctrl:saveModel
tfk:ctrl:loadModel

tfk:code Field
This field can generate a runnable .py file. It can used to set the code frame. All of the codes are derived from tensorflow official guide. We express our appreciation for tensorflow developers and the author of the official document.

tfk:code:mnist:simple # Simple code for img classification
tfk:code:mnist:full # More complex code for img classification
tfk:code:oxford # Code for img segmentation
tfk:code:translate # Code for NLP-translate
tfk:code:word_embeddings # Code for NLP-word embeddings

code

How to Contribute
This project welcomes contributions and suggestions.

Fork our repository and you can submit the snippet you like.

Bug Report or Problem
If you find some bugs or have some problems on this extension. Please create your issue.

Contributors
Kaiyan Chang

License
email
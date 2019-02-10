# Computer vision and machine learning framework for processing and analysis of medical image.
A super flexible framework based on py-torch for Convolutional Neural Network that is easy to customize for custom dataset. This framework is based on both pythonic and object oriented design. It consist of following major features:
1. Customizable pytorch universal trainer module that takes in model and has:
  - Saving and resuming best model while training
  - Extend torchtrainer.py to add custom functionality.
  - Able to work on multiple GPUs, load model trained on multiple GPU.
  - Automatically detects all GPUs and use all if specified.
2. Customizable dataloader that handles on-the-fly data loading. It comes in handy when we need to load a single loader for one patches of just one image. 
  -Extend datagen.py to add custom data load functionality.
3. Centralized configuration - All parameters are centralized in on file runs.py.
4. Consist of working implementation of u-net. A popular CNN architecture that gives state-of-the-art results for biomedical image segmentation.
5. Metrics like precision, recall, f1 and accuracy is super easy to work with with ScoreAccumulator.py which can accumulate scores from both numpy array and pytorch tensors.
6. Centralized class Image.py for loading /processing image, their mask, ground truth and many more.
7. Nice utility auto_split.py to divide any dataset to non-overlapping train, validation and test set.
8. nviz.py for vizualizing loss, precision-recall curve, accuracy and many more. It reads from a csv-file generated by the torchtrainer.py and works in background at the end of every epoch. Thus, does not intervene with the training speed.


# Dependencies
$pip install -r ature/assets/requirements.txt

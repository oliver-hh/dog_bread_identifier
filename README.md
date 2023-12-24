# Dog Breed Identifier

This is the first project of the Udacity Nanodegree program "AI Programming with Python".

It is about a predefined class for classifying dogs and other animals and objects.
The aim is to develop statistics based on this for classifying given and own images.

The following functionalities have been implemented:
1. Process command line arguments
2. Create pet label dictionary
3. Execute image classification
4. Classify images as dog, not-a-dog, etc.
5. Calculate statistics
6. Print results

## Enhancements/deviations from the orginal code

### Predefined class ```classifier.py```
The predefined source code produced warnings as the parameter ```pretrained``` is deprecated.
It has been replaced by the recommended parameter ```weights```.

Before:
```python
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)
```

After:
```python
resnet18 = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
alexnet = models.alexnet(weights=models.AlexNet_Weights.DEFAULT)
vgg16 = models.vgg16(weights=models.VGG16_Weights.DEFAULT)
```

### Print Functions
It seems that there was a misunderstanding on my end when it came to the print functions
that check each step of the development. I realized them by myself and put them into the
file ```print_functions_for_lab_checks_oliver.py```. In the current version of ```check_images.py```
the Udacity-version ```print_functions_for_lab_checks.py``` has been imported. If you are
interested in my implemtation replace the original import statement to use my implementation.

### Additional Command Line Argument
To avoid that all checks for the intermediate steps produce command line output some 
more arguments have been added as switches (```default=false```) so that the desired
output can be controlled via the command line:

Overview of all command line arguments including the before mentioned

| Parameter                   | Description                                        | Default      |
| --------------------------- | -------------------------------------------------- | ------------ |
| --dir                       | path to the folder of pet images                   | pet_images/  |
| --arch                      | CNN architecture: resnet, alexnet, or vgg          | vgg          |
| --dogfile                   | path to the folder of pet images                   | dognames.txt |
| --show-args                 | show command line arguments                        | False        |
| --show-pet-labels           | show pet labels from file names                    | False        |
| --show-image-classification | show image classification from ```classifier.py``` | False        |
| --show-is-a-dog             | show whether images are dogs                       | False        |
| --show-statistics           | show statistics                                    | False        |

## Batch prpcessing

```bash
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg     --dogfile dognames.txt > vgg_pet-images.txt
```
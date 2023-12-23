# Image Classifier

```bash
source ../../venvs/play/bin/activate
```

## TODO 5: Stats

| Key                  | Value |
| -------------------- | ----- |
| n_images             | 40    |
| n_correct_dogs       | 30    |
| n_dog_images         | 30    |
| n_correct_notdogs    | 10    |
| n_notdogs_images     | 10    |
| n_correct_breed      | 28    |
| n_label_matches      | 35    |
| pct_correct_dogs     | 100.0 |
| pct_correct_notdogs  | 100.0 |
| pct_correct_breed    | 93.33 |
| pct_label_matches    | 87.5  |

## TODO 6: Print Results

Batch prpcessing

```bash
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet  --dogfile dognames.txt > alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > vgg_pet-images.txt
```
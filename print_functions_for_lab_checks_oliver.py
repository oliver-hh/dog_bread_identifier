def check_command_line_arguments(args):
    """Check that the command line arguments are valid

    Args:
        args: Arguments provided from the command line
    """
    print('Command line arguments')
    print('----------------------')
    for arg in vars(args):
        print(f'{arg:<25}: {getattr(args, arg)}')
    print()

def check_creating_pet_image_labels(pet_labels):
    """Check that pet labels have been created correctly

    Args:
        pet_labels (): pet labels to check
    """
    print('Show pet labels')
    print('---------------')
    print(f'Number of labels: {len(pet_labels)}, first 10 labels:')
    for i, (key, value) in enumerate(pet_labels.items()):
        if i == 10:
            break
        print(f"{i+1:2d} file: {key:<40}   label: {','.join(value):<30}")
    print()

def check_classifying_images(results):
    """Check classifying images

    Args:
        results: classifiers to check
    """
    print('Show image classification')
    print('-------------------------')
    for key, value in sorted(results.items(), key=lambda item: item[0].lower()):
        print(f'{key:<38} {value[0]:<28} {value[1]:<65}  {value[2]}')
    print()

def check_classifying_labels_as_dogs(results):
    """Check is-a-dog classification

    Args:
        results: classifiers to check
    """
    print('Show is-a-dog classification')
    print('----------------------------')
    for key, value in sorted(results.items(), key=lambda item: item[0].lower()):
        print(f'{key:<38} {value[0]:<28} {value[1]:<65}  {value[2]}{value[3]}{value[4]}')

    # CSV for Excel
    # print(f'File|Pet label|Classification label|Is match|Pet label is dog|Classifier label is dog')
    # for key, value in sorted(results.items(), key=lambda item: item[0].lower()):
    #     print(f'{key}|{value[0]}|{value[1]}|{value[2]}|{value[3]}|{value[4]}')

    print()

def check_calculating_results(results, results_stats):
    """Check statistics

    Args:
        results : classification result
        results_stats: statistics 
    """
    n_images = len(results)
    n_correct_dogs = sum(1 for x in results.values() if x[3] == 1 and x[4] == 1)
    n_dogs_img = sum(1 for x in results.values() if x[3] == 1)
    n_correct_notdogs = sum(1 for x in results.values() if x[3] == 0 and x[4] == 0)
    n_notdogs_img = sum(1 for x in results.values() if x[3] == 0)
    n_correct_breed = sum(1 for x in results.values() if x[2] == 1 and x[3] == 1)
    pct_correct_dogs = round(n_correct_dogs/n_dogs_img * 100, 2) if n_dogs_img > 0 else 0
    pct_correct_notdogs = round(n_correct_notdogs/n_notdogs_img * 100, 2) if n_notdogs_img > 0 else 0
    pct_correct_breed = round(n_correct_breed/n_dogs_img * 100, 2) if n_dogs_img > 0 else 0

    print('Show statistics with expected/actual value')
    print('------------------------------------------')
    print(f'n_images            : {n_images}/{results_stats["n_images"]}')
    print(f'n_dogs_img        : {n_dogs_img}/{results_stats["n_dogs_img"]}')
    print(f'n_notdogs_img    : {n_notdogs_img}/{results_stats["n_notdogs_img"]}')
    print(f'pct_correct_dogs    : {pct_correct_dogs}/{results_stats["pct_correct_dogs"]}')
    print(f'pct_correct_notdogs : {pct_correct_notdogs}/{results_stats["pct_correct_notdogs"]}')
    print(f'pct_correct_breed   : {pct_correct_breed}/{results_stats["pct_correct_breed"]}')
    print()

    # print('| Key                  | Value |')
    # print('| -------------------- | ----- |')
    # for key, value in results_stats.items():
    #     print(f'| {key:<20} | {value:>5} |')

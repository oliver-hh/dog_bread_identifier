#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
# PROGRAMMER:   Oliver Brandt
# DATE CREATED: 10.12.2023
# REVISED DATE:
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Note that the true identity of the pet (or object) in the image is
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time

# Imports print functions that check the lab
from print_functions_for_lab_checks import (
    check_command_line_arguments,
    check_classifying_images,
    check_creating_pet_image_labels,
    check_classifying_labels_as_dogs,
    check_calculating_results
)

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# def check_command_line_arguments(args):
#     """Check that the command line arguments are valid

#     Args:
#         args: Arguments provided from the command line
#     """
#     print('Command line arguments')
#     print('----------------------')
#     for arg in vars(args):
#         print(f'{arg:<25}: {getattr(args, arg)}')
#     print()

# def check_creating_pet_image_labels(pet_labels):
#     """Check that pet labels have been created correctly

#     Args:
#         pet_labels (): pet labels to check
#     """
#     print('Show pet labels')
#     print('---------------')
#     print(f'Number of labels: {len(pet_labels)}, first 10 labels:')
#     for i, (key, value) in enumerate(pet_labels.items()):
#         if i == 10:
#             break
#         print(f"{i+1:2d} file: {key:<40}   label: {','.join(value):<30}")
#     print()

# def check_classifying_images(results):
#     """Check classifying images

#     Args:
#         results: classifiers to check
#     """
#     print('Show image classification')
#     print('-------------------------')
#     for key, value in sorted(results.items(), key=lambda item: item[0].lower()):
#         print(f'{key:<38} {value[0]:<28} {value[1]:<65}  {value[2]}')
#     print()

# def check_classifying_labels_as_dogs(results):
#     """Check is-a-dog classification

#     Args:
#         results: classifiers to check
#     """
#     print('Show is-a-dog classification')
#     print('----------------------------')
#     for key, value in sorted(results.items(), key=lambda item: item[0].lower()):
#         print(f'{key:<38} {value[0]:<28} {value[1]:<65}  {value[2]}{value[3]}{value[4]}')

#     # CSV for Excel
#     # print(f'File|Pet label|Classification label|Is match|Pet label is dog|Classifier label is dog')
#     # for key, value in sorted(results.items(), key=lambda item: item[0].lower()):
#     #     print(f'{key}|{value[0]}|{value[1]}|{value[2]}|{value[3]}|{value[4]}')

#     print()

# def check_calculating_results(results, results_stats):
#     """Check statistics

#     Args:
#         results : classification result
#         results_stats: statistics 
#     """
#     n_images = len(results)
#     n_correct_dogs = sum(1 for x in results.values() if x[3] == 1 and x[4] == 1)
#     n_dog_images = sum(1 for x in results.values() if x[3] == 1)
#     n_correct_notdogs = sum(1 for x in results.values() if x[3] == 0 and x[4] == 0)
#     n_notdogs_images = sum(1 for x in results.values() if x[3] == 0)
#     n_correct_breed = sum(1 for x in results.values() if x[2] == 1 and x[3] == 1)
#     pct_correct_dogs = round(n_correct_dogs/n_dog_images * 100, 2) if n_dog_images > 0 else 0
#     pct_correct_notdogs = round(n_correct_notdogs/n_notdogs_images * 100, 2) if n_notdogs_images > 0 else 0
#     pct_correct_breed = round(n_correct_breed/n_dog_images * 100, 2) if n_dog_images > 0 else 0

#     print('Show statistics with expected/actual value')
#     print('------------------------------------------')
#     print(f'n_images            : {n_images}/{results_stats["n_images"]}')
#     print(f'n_dog_images        : {n_dog_images}/{results_stats["n_dog_images"]}')
#     print(f'n_notdogs_images    : {n_notdogs_images}/{results_stats["n_notdogs_images"]}')
#     print(f'pct_correct_dogs    : {pct_correct_dogs}/{results_stats["pct_correct_dogs"]}')
#     print(f'pct_correct_notdogs : {pct_correct_notdogs}/{results_stats["pct_correct_notdogs"]}')
#     print(f'pct_correct_breed   : {pct_correct_breed}/{results_stats["pct_correct_breed"]}')
#     print()

#     # print('| Key                  | Value |')
#     # print('| -------------------- | ----- |')
#     # for key, value in results_stats.items():
#     #     print(f'| {key:<20} | {value:>5} |')

# Main program function defined below
def main():

    # Measures total program runtime by collecting start time
    start_time = time()

    # Define get_input_args function within the file get_input_args.py
    # This function retrieves 3 Command Line Arugments from user as input from
    # the user running the program from a terminal window. This function returns
    # the collection of these command line arguments from the function call as
    # the variable in_arg
    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg
    if in_arg.show_args:
        check_command_line_arguments(in_arg)

    # Define get_pet_labels function within the file get_pet_labels.py
    # Once the get_pet_labels function has been defined replace 'None'
    # in the function call with in_arg.dir  Once you have done the replacements
    # your function call should look like this:
    #             get_pet_labels(in_arg.dir)
    # This function creates the results dictionary that contains the results,
    # this dictionary is returned from the function call as the variable results
    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results
    if in_arg.show_pet_labels:
        check_creating_pet_image_labels(results)

    # Define classify_images function within the file classiy_images.py
    # Once the classify_images function has been defined replace first 'None'
    # in the function call with in_arg.dir and replace the last 'None' in the
    # function call with in_arg.arch  Once you have done the replacements your
    # function call should look like this:
    #             classify_images(in_arg.dir, results, in_arg.arch)
    # Creates Classifier Labels with classifier function, Compares Labels,
    # and adds these results to the results dictionary - results
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results
    if in_arg.show_image_classification:
        check_classifying_images(results)

    # Define adjust_results4_isadog function within the file adjust_results4_isadog.py
    # Once the adjust_results4_isadog function has been defined replace 'None'
    # in the function call with in_arg.dogfile  Once you have done the
    # replacements your function call should look like this:
    #          adjust_results4_isadog(results, in_arg.dogfile)
    # Adjusts the results dictionary to determine if classifier correctly
    # classified images as 'a dog' or 'not a dog'. This demonstrates if
    # model can correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    if in_arg.show_is_a_dog:
        check_classifying_labels_as_dogs(results)

    # Define calculates_results_stats function within the file calculates_results_stats.py
    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts & percentages). This
    # dictionary is returned from the function call as the variable results_stats
    # Calculates results of run and puts statistics in the Results Statistics
    # Dictionary - called results_stats
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    if in_arg.show_statistics:
        check_calculating_results(results, results_stats)

    # Define print_results function within the file print_results.py
    # Once the print_results function has been defined replace 'None'
    # in the function call with in_arg.arch  Once you have done the
    # replacements your function call should look like this:
    #      print_results(results, results_stats, in_arg.arch, True, True)
    # Prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested)
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time()

    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time #calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()

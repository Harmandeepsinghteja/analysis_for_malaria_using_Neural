# import the necessary packages
import os
# initialize the path to the *original* input directory of images
ORIG_INPUT_DATASET = "/mnt/c/large_datasets/archive/cell_images/"
# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
BASE_PATH = "analysis_for_malaria_using_Neural"


# derive the training, validation, and testing directories
TRAIN_PATH = os.path.sep.join([ORIG_INPUT_DATASET, "training"])
VAL_PATH = os.path.sep.join([ORIG_INPUT_DATASET, "validation"])
TEST_PATH = os.path.sep.join([ORIG_INPUT_DATASET, "testing"])
# define the amount of data that will be used training
TRAIN_SPLIT = 0.8
# the amount of validation data will be a percentage of the
# *training* data
VAL_SPLIT = 0.1
""""
This script perform the data unloading steps. The zip file is unzipped, as a json file.

functions:
    *unzip_file - unzip the zip file and export it
    *main - the main function to run the script

"""

# TODO Clean up code

import os
import subprocess
import zipfile

# from utils.logger import logger
from loguru import logger

data_files = ["train_labels.csv", "train_data.csv"]
COMMAND = [
    "kaggle",
    "competitions",
    "download",
    "-c",
    "amex-default-prediction",
    "-f",
    "FILE",
    "-p",
    "data/raw/amex-default-prediction",
]
DATA_DIR = "data/raw/amex-default-prediction/"


def downlaod_file(cmd, unzipped_file_path, data_dir):
    """_summary_

    Parameters
    ----------
    cmd : _type_
        _description_
    unzipped_file : _type_
        _description_
    data_dir : _type_
        _description_
    """
    subprocess.run(cmd, check=True, text=True)
    # Unzipping and delete the zipped file to free storage
    with zipfile.ZipFile(unzipped_file_path, "r") as zip_ref:
        zip_ref.extractall(data_dir)
    if os.path.exists(unzipped_file_path):
        os.remove(unzipped_file_path)


def main():
    """_summary_"""
    logger.info("Commencing the data unzipping process")
    try:
        for file in data_files:
            logger.info(f"Downloading {file} in {DATA_DIR}")
            COMMAND[6] = file
            unzipfile_path = DATA_DIR + file + ".zip"
            downlaod_file(COMMAND, unzipfile_path, DATA_DIR)
            logger.info(f" {file} downloaded succesful")
        logger.success("files downloaded succesful")

    except Exception as error:
        logger.error(f"failed due to {error}")
        logger.exception("Data unloading was unsuccesfully")


if __name__ == "__main__":
    main()

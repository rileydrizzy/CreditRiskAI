"""Dataset Download Module

This module provides functionality to download and unzip data files for 
the Amex Default Prediction Kaggle competition. It utilizes the Kaggle API to retrieve 
the required data files in ZIP format and extracts them into a specified data directory.

Functions:
    download_file(cmd, unzipped_file_path, data_dir):
        Downloads and extracts a data file from Kaggle.

    main():
        Main function to execute the script for downloading and unzipping data.

Usage:
    Ensure that the Kaggle API is properly configured on your system for successful data retrieval.

    
"""

import os
import subprocess
import zipfile

from utils.logger import logger


DATA_DIR = "data/raw/amex-default-prediction/"
# kaggle/input/amex-default-prediction/raw

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
    DATA_DIR,
]


def downlaod_file(cmd, unzipped_file_path, data_dir):
    """Download and unzip the data file from Kaggle.

    Parameters
    ----------
    cmd : list
        Command to download the data file.
    unzipped_file_path : str
        Path to the downloaded and unzipped file.
    data_dir : str
        Directory where the data will be stored.
    """

    subprocess.run(cmd, check=True, text=True)

    # Unzipping and delete the zipped file to free storage
    with zipfile.ZipFile(unzipped_file_path, "r") as zippped_file:
        zippped_file.extractall(data_dir)
    if os.path.exists(unzipped_file_path):
        os.remove(unzipped_file_path)


def main():
    """
    Main function to run the script for downloading and unzipping data.
    """
    logger.info("Commencing the data downloading and unzipping process")
    try:
        for file in data_files:
            logger.info(f"Downloading {file} in {DATA_DIR}")

            # Swap
            COMMAND[6] = file
            zip_file_path = os.path.join(DATA_DIR, file + ".zip")
            downlaod_file(COMMAND, zip_file_path, DATA_DIR)
            logger.info(f" {file} downloaded succesful")
        logger.success("All files downloaded succesful")

    except Exception as error:
        logger.exception(f"Data unloading was unsuccessful, due to {error}")


if __name__ == "__main__":
    main()

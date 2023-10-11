"""_summary_
"""

import opendatasets as opd
from loguru import logger
#from utils.logger import logger

url = 'https://www.kaggle.com/competitions/amex-default-prediction/data'
dir = 'data'

def main():
    logger.info("Commencing the data unzipping process.")
    try:
        opd.download(dataset_id_or_url=url, data_dir= dir)
        logger.info('Data downloaded succesful')
    except Exception as error:
        logger.error("Failed to download")


if __name__ == '__main__':
    main()

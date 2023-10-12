"""_summary_
"""

import subprocess
from loguru import logger
#from utils.logger import logger

def main():
    logger.info("Commencing the data unzipping process.")
    try:
        cmd_3= ['kaggle' ,'competitions' ,'download' ,'-c','amex-default-prediction',
        '-f','sample_submission.csv',]
        result = subprocess.run(cmd_3, check= True, capture_output=True, text= True )
        # TODO write logger code and remaining file code, unzip file, and delete zip file
        logger.info('Data downloaded succesful')
    except Exception as error:
        logger.error(f"Failed to download as {error}")


if __name__ == '__main__':
    main()

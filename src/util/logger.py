import logging
from src.util.config_util import GlobalConfig

file_handler = logging.FileHandler(GlobalConfig.get_log_filename())
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger = logging.getLogger("smart_home")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
#deactivate the output by console

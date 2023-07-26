import logging

logger = logging.getLogger("my_logger")
logging.basicConfig()

logger.error("これはエラーメッセージです")
logger.warning("これは警告メッセージです")
logger.log(logging.CRITICAL, "これは重大なメッセージです")

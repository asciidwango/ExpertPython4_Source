from datetime import timedelta, datetime
import time
import logging.config
import logging.handlers

import freezegun

logging.config.fileConfig("logging.conf")

logger = logging.getLogger(__name__)


def main():
    with freezegun.freeze_time() as frozen:
        while True:
            frozen.tick(timedelta(hours=1))
            time.sleep(0.1)
            logger.info(f"何かが{datetime.now()}に発生しました")


if __name__ == "__main__":
    main()

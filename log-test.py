#!/usr/bin/env python
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG,
    filename="file.log"
    )

logger = logging.getLogger(__name__)
def application():
    logger.debug("This is a debug log")
    logger.debug("This is a debug log")
    logger.debug("This is a debug log")
    logger.debug("This is a debug log")

if __name__ == "__main__":
    try:
     application()
    except KeyboardInterrupt:
        pass

from loguru import logger
import sys
import pathlib as pl

LEVEL = 'DEBUG'
logs_dir = pl.Path('./logs').resolve()

logs_dir.mkdir(parents=True, exist_ok=True)
logger.remove()

try:
    logger.add(sys.stdout, level=LEVEL)
    logger.add('./logs/log.txt', level=LEVEL, rotation="00:00", compression='bz2')
except Exception as e:
    logger.exception(e)

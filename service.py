import pathlib as pl
import subprocess as sp
import sys

from logger import logger

svc_name = 'WinAPS'
main_dir = pl.Path(sys.argv[0]).parent.resolve()


def install():
    logger.debug("Installing service...")
    p = sp.Popen(['bin/nssm.exe', 'install', svc_name, str(main_dir / 'winaps.exe')])
    p.communicate()
    logger.debug("done.")


def start():
    logger.debug("Starting service...")
    p = sp.Popen(['sc', 'start', svc_name])
    p.communicate()
    logger.debug("done.")


def install_start():
    install()
    start()
    logger.info("Service installed and started.")

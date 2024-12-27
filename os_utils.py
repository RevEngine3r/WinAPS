import pathlib as pl
import subprocess as sp
import struct
from logger import logger


def is_64_bit() -> bool:
    return struct.calcsize("P") == 8


# PSTools: PsExec
psexec_exe = str(pl.Path(f'bin/PsExec{"64" * is_64_bit()}.exe').resolve())


def psexec(cmd: list[str], detach: bool = False, session_id: int = None) -> sp.Popen:
    psexec_args = [psexec_exe, '-accepteula', '-nobanner']
    if detach:
        psexec_args.append('-d')
    if session_id is not None:
        psexec_args.extend(['-i', str(session_id)])
    cmd[0] = str(pl.Path(cmd[0] + '.exe').resolve())
    return popen(psexec_args + cmd)


def popen(cmd: list[str]) -> sp.Popen:
    cmd = list(map(str, cmd))
    logger.debug(f'{cmd=}')
    return sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)

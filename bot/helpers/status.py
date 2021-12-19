import platform

import psutil
from youtube_dl.version import __version__ as youtube_dl_version
from bot.helpers import human_readable_size
import pyrogram


def system_status() -> str:
    disk_size = psutil.disk_usage('.')
    total = human_readable_size(disk_size.total)
    used = human_readable_size(disk_size.used)
    # free = human_readable_size(disk_size.free)
    disk_usage_p = disk_size.percent
    ram = psutil.virtual_memory()
    ram_total = human_readable_size(ram[0])
    ram_cache = human_readable_size(ram[8])
    ram_used = human_readable_size(ram[3])
    ram_usage_p = ram[2]
    cpu_usage_p = psutil.cpu_percent()
    system_os = platform.system()
    release = platform.release()
    version = platform.version()
    architecture = platform.architecture()
    python_version = platform.python_version()
    pyrogram_version = pyrogram.__version__

    resource = f'**Disk: {used} ({disk_usage_p}%) of {total}**\n' \
               f'**CPU:** `{cpu_usage_p}%`\n' \
               f'**RAM: {ram_used} ({ram_usage_p}%) of {ram_total}**\n' \
               f'**Cache:** `{ram_cache}`\n' \
               f'**Operating system:** `{system_os}`\n' \
               f'**Release:** `{release}`\n' \
               f'**Architecture:** `{" ".join(architecture)}`\n' \
               f'**Release version:** `{version}`' \
               f'**Python version: ** `{python_version}`' \
               f'**Pyrogram version:** `{pyrogram_version}' \
               f'**youtube-dl version:** `{youtube_dl_version}'

    return resource

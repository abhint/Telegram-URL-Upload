import psutil
import platform
from bot.helpers import human_readable_size


def system_status():
    disk_size = psutil.disk_usage('/')
    total = human_readable_size(disk_size.total)
    used = human_readable_size(disk_size.used)
    free = human_readable_size(disk_size.free)
    ram = psutil.virtual_memory()
    ram_total = human_readable_size(ram[0])
    ram_cache = human_readable_size(ram[8])
    ram_used = human_readable_size(ram[3])
    ram_usage_p = ram[2]
    cpu_usage_p = psutil.cpu_percent()
    os = platform.system()
    release = platform.release()
    resource = f'**Total:**  `{total}`\n'\
               f'**Used:**  `{used}`\n'\
               f'**Free:**  `{free}`\n'\
               f'**CPU:** `{cpu_usage_p}%`\n'\
               f'**{ram_used} ({ram_usage_p}%) of {ram_total}**\n'\
               f'**Cache:** `{ram_cache}`\n'\
               f'**Operating system:** `{os}`\n' \
               f'**Release:** `{release}`'
    return resource

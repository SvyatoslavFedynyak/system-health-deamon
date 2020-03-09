import psutil
import json


def CPU_currentTimes():
    raw = psutil.cpu_times(True)
    raw_result = []
    cpu_dict = {}
    for idx, cpu in enumerate(raw):
        cpu_dict['CPU'] = str(idx)
        cpu_dict['user'] = str(cpu.user)
        cpu_dict['system'] = str(cpu.system)
        cpu_dict['nice'] = str(cpu.nice)
        cpu_dict['idle'] = str(cpu.idle)
        cpu_dict['iowait'] = str(cpu.iowait)
        cpu_dict['irq'] = str(cpu.irq)
        cpu_dict['softirq'] = str(cpu.softirq)
        cpu_dict['steal'] = str(cpu.steal)
        cpu_dict['guest'] = str(cpu.guest)
        cpu_dict['guest_nice'] = str(cpu.guest_nice)
        raw_result.append(cpu_dict.copy())
    return json.dumps(raw_result, indent='\t')

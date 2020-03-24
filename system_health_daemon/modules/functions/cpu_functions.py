import psutil
import json
import datetime


def CPU_currentTimes():
    '''Return current CPU time values'''
    raw = psutil.cpu_times(True)
    raw_result = {}
    cpu_dict = {}
    raw_result['name'] = 'CPU_currentTimes'
    raw_result['datetime'] = str(datetime.datetime.now())
    raw_result['data'] = []
    for idx, cpu in enumerate(raw):
        cpu_dict = cpu._asdict()
        cpu_dict['CPU'] = idx
        raw_result['data'].append(cpu_dict.copy())
    return json.dumps(raw_result, indent='\t')
'''
def CPU_timePercentage():
    ''''''Return CPU time percentage values''''''
    raw = psutil.cpu_times_percent(True)
    raw_result = {}
    cpu_dict = {}
    raw_result['name'] = 'CPU_timePercentage'
    raw_result['datetime'] = str(datetime.datetime.now())
    raw_result['data'] = []
    for idx, cpu in enumerate(raw):
        cpu_dict = cpu._asdict()
        cpu_dict['CPU'] = idx
        raw_result['data'].append(cpu_dict.copy())
    return json.dumps(raw_result, indent='\t')
'''
def CPU_stats():
    '''Return CPU time percentage values'''
    freq = psutil.cpu_freq(True)
    stat = psutil.cpu_stats()
    phys_cpu = psutil.cpu_count(False)
    log_cpu = psutil.cpu_count()
    raw_result = {}
    raw_result['name'] = 'CPU_stats'
    raw_result['datetime'] = str(datetime.datetime.now())
    raw_result['data'] = []
    stat_dict = {}
    stat_dict['log_cpus'] = log_cpu
    stat_dict['phys_cpus'] = phys_cpu
    stat_dict = {**stat_dict, **stat._asdict()}
    freq_cpu_arr = []
    freq_dict = {}
    for idx, cpu in enumerate(freq):
        freq_dict['CPU'] = idx
        freq_dict['max'] = cpu.max
        freq_dict['min'] = cpu.min
        freq_cpu_arr.append(freq_dict.copy())
    stat_dict['frequncies'] = freq_cpu_arr
    raw_result['data'].append(stat_dict.copy())
    return json.dumps(raw_result, indent='\t')
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
        cpu_dict = raw[idx]._asdict()
        raw_result['data'].append(cpu_dict.copy())
    return json.dumps(raw_result, indent='\t')



import json

def CPU_composer(json_data):
    '''Compose report from json CPU data'''
    parsed_data = json.loads(json_data)
    report = ''
    report += 'CPU report\nDate: {0}\n'.format(parsed_data['datetime'])

    # Process CPU_currentTimes data
    data = parsed_data['function_reports'][0]['data'][0]
    for metric in data:
        report += '{0}: {1}\n'.format(metric, data[metric])
        
    return report
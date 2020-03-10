# system-health-daemon
Linux daemon, written on python that works with system health

## Content

- [system-health-daemon](#system-health-daemon)
  - [Content](#content)
  - [Reports specification](#reports-specification)
    - [Function report](#function-report)
    - [Worker report](#worker-report)
    - [Daemon report](#daemon-report)
  - [Daemon requirements (due to PEP 3143):](#daemon-requirements-due-to-pep-3143)
  - [Primary architecture](#primary-architecture)

## Reports specification

Application operates 3 types of json reports:

- [Function report](#function-report)
- [Worker report](#worker-report)
- [Daemon report](#daemon-report)

### Function report

Structure:
```json
{
    "name": "$function_name",
    "datetime" : "$compose_datetime",
    [
        {
            some data...
        },
        {
            ...
        },
        ...
    ]
}
```

### Worker report

Structure:
```json
{
    "name": "$worker_name",
    "datetime" : "$compose_datetime",
    [
        {
            some data...
        },
        {
            ...
        },
        ...
    ]
}
```

### Daemon report

Structure:
```json
{
    "name": "$worker_name",
    "datetime" : "$compose_datetime",
    [
        {
            some data...
        },
        {
            ...
        },
        ...
    ]
}
```

## Daemon requirements (due to PEP 3143):

- Close all open file descriptors.
- Change current working directory.
- Reset the file access creation mask.
- Run in the background.
- Disassociate from process group.
- Ignore terminal I/O signals.
- Disassociate from control terminal.
- Don’t reacquire a control terminal.

Correctly handle the following circumstances:

- Started by System V init/systemd process.
- Daemon termination by SIGTERM signal.
- Children generate SIGCLD signal.



## Primary architecture

![Primary architecture](https://github.com/SvyatoslavFedynyak/system-health-deamon/blob/master/images/deamon-arch.jpg)

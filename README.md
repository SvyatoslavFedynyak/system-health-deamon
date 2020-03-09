# system-health-daemon
Linux daemon, written on python that works with system health

## Content

- [Daemon requirements](#daemon requirements)
- [Reports specification](#Reports specification)

### Reports specification

Application operates 3 types of json reports:

- [function's report](#function's report)
- [worker's report](#worker's report)
- [daemon's report](#daemon's report)

#### function's report

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

#### worker's report

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

#### daemon's report

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

### daemon requirements (due to PEP 3143):

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

![Primary architecture](https://github.com/SvyatoslavFedynyak/system-health-daemon/blob/master/images/daemon-arch.jpg)

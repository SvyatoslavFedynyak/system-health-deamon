# system-health-deamon
Linux deamon, written on python that works with system health

Deamon requirements (due to PRP 3143):

- Close all open file descriptors.
- Change current working directory.
- Reset the file access creation mask.
- Run in the background.
- Disassociate from process group.
- Ignore terminal I/O signals.
- Disassociate from control terminal.
- Don’t reacquire a control terminal.
- Correctly handle the following circumstances:
* Started by System V init process.
* Daemon termination by SIGTERM signal.
* Children generate SIGCLD signal.



## Primary architecture

![Primary architecture](https://github.com/SvyatoslavFedynyak/system-health-deamon/blob/master/images/deamon-arch.jpg)

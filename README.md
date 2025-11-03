# INFINITE - Powerful rootkit detection tool in Linux.

<img src="https://i.postimg.cc/g2yxCFsZ/INFINITE.png" alt="imgur" width=600/>


> *"The terror of updated rootkits."* 

**INFINITE** Tool designed for the detection of Userland / LKM rootkits.
---

## Install
Commands:
```
git clone https://github.com/cphx70/INFINITE
cd INFINITE
python INFINITE.py
```

## FEATURES

### Detect Userland Rootkit

For the detection of Userland rootkits, INFINITE looks for detections using various tools, such as:
- LDD
- STRACE
- PS AUX
- NETSTAT

<p align="center">
<img src="https://i.postimg.cc/63qT47Xz/USERLAND.png">
</p align="center">


### Detect LKMs rootkit

For the detection of LKM rootkits, INFINITE uses tools, monitors directories and files, and executes creative detection mechanisms with the help of the user.

Within all of this, we will explain its mechanisms and functioning.

##### Privilege Escalation

INFINITE has developed a mechanism that works with the help of the user; it is responsible for providing an explanation and instruction to the user to proceed with executing a command, and depending on what the user sees, it may indicate a possible LKM Rootkit.

The command executed is as follows: - MAGIC=mtz bash

Although it can be changed to: kill -59 0 or others.

<p align="center">
<img src="https://i.postimg.cc/KcKrdjg6/PRIVES.png">
</p align="center">

#### DMESG

INFINITE relies on DMESG to observe information about module loads, kernel symbols, syscalls, and ioctls.

Thanks to this, INFINITE is able to provide the user with the maximum possible information to achieve the detection of an LKM Rootkit.

<p align="center">
<img src="https://i.postimg.cc/sD7PgLK2/IOCTL-output.png">
</p align="center">

<p align="center">
<img src="https://i.postimg.cc/BvYHzfZc/syscalls-dmesg.png">
</p align="center">

#### /PROC/MODULES

Also, the tool takes care of looking at /proc/modules to see information about loaded modules.

Although it is not very effective, if an LKM Rootkit does not apply its hooks properly or fails at something, this could be a detection factor.

<p align="center">
<img src="https://i.postimg.cc/B6RDq5KW/MODULES-CHARGED.png">
</p align="center">

#### TOUCHED_FUNCTIONS

INFINITE also look at: /sys/kernel/tracing/touched_functions to see which functions have been touched.

The most common one is: kallsyms_lookup_name (0)

<p align="center">
<img src="https://i.postimg.cc/0y9S2ybS/TOUCHED-FUNCTIONS.png">
</p align="center">


#### FTRACE DISABLE

INFINITE has a function to disable FTRACE, which is somewhat peculiar, but advanced rootkits could evade the typical FTRACE deactivation methods.

Therefore, I have integrated 3 ways to deactivate FTRACE.
1 - Using os.system() to execute the command directly (not very effective against more sophisticated rootkits)

2 - Opening the file and changing its value to 0 (also ineffective against modern rootkits)

3 - Using the pwrite() syscall (effective against more modern rootkits)

<p align="center">
<img src="https://i.postimg.cc/tgMn5dDZ/ftrace-bypass.png">
</p align="center">

The same INFINITE code is responsible for creating, compiling, and running the file, but even so, I will leave the bypass.



## All Credits

**INFINITE** was created by me (**cphx_**) with the goal of detect every or powerfull linux rootkits.


## PLOT TWIST

Unfortunately, with all these detection methods, codes, etc., there are rootkits capable of evading this tool and others.  

In any case, it will be updated little by little. :)



## BUGS

Any bug found, if you want, open a issue or contact me via discord: `cphx_`

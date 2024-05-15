# Z4

## Uros



## Tamara



## Alex

### Set up
<ol>

<li>
Starting Docker `Ubuntu-24` image.
Privileged because we need to edit network settings.
Volume is for saving logs right as we go (path - Windows stuf).

```bat
docker run -it --privileged -v "//d/source/repos/docs/SecureSoftwareDevelopment/Z5/alex/tmp_from_docker:/tmp" -p 5000:5000 -p 22:22 ubuntu:24.04
```
</li>
<li>
I've tried to use `screen`, but it's <span style="color: red;">awful!!!</span>
There were options to use `tmux-logging`, but in fact Docker saves logs, so... no need to suffer.

```bat
docker logs -f suspicious_knuth *> Z5/alex/docker.log
```
</li>

<li>
Installing `open-ssh`

```shell
apt install openssh-server
```

Oopps, no such package.

```shell
apt update
```

</li>

<li>
Installing `nano`.
</li>

<li>
Installing `Python3`. (it is already here)

But we still need to install `pip`.

```shell
apt install python3-pip -y
```
</li>

<li>

```shell
apt install python3-flask
```

Creating some example app (see tmp for details) and running it:

```shell
python3 -m flask --app example run --host=0.0.0.0 &
```

(For those who like me can not start it right from a first try:)

```shell
kill $(lsof -t -i:5000)
```

Installing `lsof` first.
</li>

<li>

```shell
passwd
```

`starcraftrules`

</li>

</ol>

### OS review

<ol>

<li>

``` 
root@9509f6362468:/tmp#  lsb_release -a

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 24.04 LTS
Release:        24.04
Codename:       noble
```

</li>
<li>

``` 
root@9509f6362468:/tmp# uname -a

Linux 9509f6362468 5.15.49-linuxkit-pr #1 SMP Thu May 25 07:17:40 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```

</li>
<li>

```
root@9509f6362468:/tmp# uptime

 23:24:54 up  7:08,  0 user,  load average: 0.00, 0.00, 0.00
```

</li>

</ol>

### Time review

<ol>

<li>

```
root@9509f6362468:/tmp# cat /etc/timezone 
Europe/Belgrade
```

</li>

</ol>

### Package review

1. ```apt list --manual-installed```

Lots of output but nothing interesting (image is new)

### Logging

Discussed in the beginning - Docker cares about it)

### Network review

<ol>
<li>
Installed `ufw`. Configure it to allow `5000` and `22`.

```
root@9509f6362468:/tmp# ufw status
Status: active

To                         Action      From
--                         ------      ----
5000                       ALLOW       Anywhere
22/tcp                     ALLOW       Anywhere
5000 (v6)                  ALLOW       Anywhere (v6)
22/tcp (v6)                ALLOW       Anywhere (v6)
```
</li>

<li>
`ufw` works on reboot:

```
root@9509f6362468:/tmp# ufw enable
Firewall is active and enabled on system startup
```
</li>
</ol>

### Files review

<ol>
<li>
I know that there is only `/tmp` mounted, so I will not check other million of Docker-mounted services for this work.
In real world they all should be checked.

```
root@9509f6362468:/tmp# mount | grep /tmp

grpcfuse on /tmp type fuse.grpcfuse (rw,nosuid,nodev,relatime,user_id=0,group_id=0,allow_other,max_read=1048576)
```
I want to make it `noexec`
```
root@9509f6362468:/tmp# mount -o remount,noexec /tmp
```

```
root@9509f6362468:/tmp# mount | grep /tmp
grpcfuse on /tmp type fuse.grpcfuse (rw,nosuid,nodev,noexec,relatime,user_id=0,group_id=0,allow_other,max_read=1048576)
```

</li>
<li>

```
root@9509f6362468:/tmp# ls -al /etc/shadow

-rw-r----- 1 root shadow 712 May 15 22:13 /etc/shadow
```

Enough secure.

</li>
</ol>


![Meme](alex/images/cat.jpg)

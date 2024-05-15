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


![Meme](alex/images/cat.jpg)

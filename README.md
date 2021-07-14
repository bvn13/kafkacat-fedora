# kafkacat

This is a Fedora package repository of [kafkacat](https://github.com/edenhill/kafkacat) utility

# dependencies

1. librdkafka

```
# dnf install librdkafka
```

2. fedora build system

```
# dnf install fedora-packager fedora-review
# usermod -a -G mock <your-user-name>
```

... and perform a relogin to update user groups

# how to run

1. clone this repo

```
git clone https://github.com/bvn13/kafkacat.git
```

2. update submodule

```
git submodule foreach git pull origin master
```

3. build fedora package

```
fedpkg --release f34 local
```

4. install built rpm

```
# rpm -i x86_64/kafkacat-1.7.0-1.x86_64.rpm
```

#/bin/bash

git submodule foreach git pull origin master

ln -sf kafkacat kafkacat-1.7.0

tar -cf kafkacat-1.7.0.tar kafkacat-1.7.0

fedpkg --release f34 local

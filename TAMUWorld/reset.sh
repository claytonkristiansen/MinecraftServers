#!/bin/sh
rm -r world
java -Xmx8096M -Xms8096M -jar server.jar nogui

#!/bin/bash
adduser -D client
addgroup managerGroup
adduser -D manager -G managerGroup

#!/bin/bash
# This script will install all CVE which are still unresolved in alpine.
# This will get us a huge amount of CVEs in our benchmark
# atm 711 CVE's (this will change when a new alpine patch comes out)
# WARNING: this script uninstalls and installs certain binairies
# it will possibly affect other services running on the benchmark 
# and will take a very long time
apk add curl
apk add --repository https://dl-cdn.alpinelinux.org/alpine/v3.15/community pup


# Iterating from version 3.17 to 3.10
version=18
while (( --version >= 10)); do
    echo "Running as version 3.$version"

    curl "https://security.alpinelinux.org/branch/3.$version-main" \
    -H 'authority: security.alpinelinux.org' \
    -H 'accept: text/html;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
    --compressed \
    > tmp.txt

    # List CVEs
    cat tmp.txt | pup 'a' | grep CVE | grep -v ">" >> CVEs.txt
    sort CVEs.txt | uniq > tmp.cve
    cat tmp.cve > CVEs.txt
    rm tmp.cve

    # List names of binaries whom have cve's
    cat tmp.txt | pup 'a attr{href}' | grep -v "CVE" | grep -v "git" | cut -d "/" -f3 >> names.txt
    sort names.txt | uniq > unique$version.txt 
    sed -e "s#^#apk add  --repository http://dl-cdn.alpinelinux.org/alpine/v3.$version/main/ #" unique$version.txt >> binVersion.txt

    rm names.txt
    xargs apk del < unique$version.txt 
    rm unique$version.txt
    # xargs apk add  --repository http://dl-cdn.alpinelinux.org/alpine/v3.10/main/ < unique$version.txt 
done

# Download bins
tac binVersion.txt | sh
rm tmp.txt
#!/bin/bash
export NODE_ENV=production

mkdir -p releases
TIMESTAMP=$(date '+%Y-%m-%d_%H-%M-%S')
mkdir -p releases/${TIMESTAMP}

platforms=("Facebook" "Instagram" "Twitter" "Tiktok" "Youtube")
for PLATFORM in "${platforms[@]}"; do
    export REACT_APP_PLATFORM=$PLATFORM
    npm run build
    cd packages/data-collector/build
    zip -r ../../../releases/${TIMESTAMP}/${PLATFORM}_${TIMESTAMP}.zip .
    cd ../../..
done

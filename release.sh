#!/bin/bash
export NODE_ENV=production

mkdir -p releases
TIMESTAMP=$(date '+%Y-%m-%d_%H-%M-%S')
mkdir -p releases/${TIMESTAMP}

platforms=("Facebook" "Instagram" "Twitter" "Tiktok" "Youtube")
for PLATFORM in "${platforms[@]}"; do
    export VITE_PLATFORM=$PLATFORM
    npm run build
    cd build
    zip -r ../releases/${TIMESTAMP}/${PLATFORM}_${TIMESTAMP}.zip .
    cd ..
done

#!/bin/bash
# NAME=$1
# mkdir -p releases
# NR=$(find ./releases -type f | wc -l | xargs)
# NR=$(($NR + 1))
# TIMESTAMP=$(date '+%Y-%m-%d')
# cd build
# zip -r ../releases/${NAME}_${TIMESTAMP}_${NR}.zip .

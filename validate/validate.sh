#!/bin/bash

source ./pantheon/env.sh > /dev/null 2>&1

echo "----------------------------------------------------------------------"
echo "PTN: validating" 

OUTPUT=$PANTHEON_RUN_DIR/cinema_databases/$PANTHEON_CDB
GOLD=validate/data/pantheon.cdb

echo "     $OUTPUT"

imgs="RenderView1_000000.png RenderView1_000005.png RenderView1_000011.png"

PASS=true
if [ -d $OUTPUT ]; then
    for img in $imgs; do
        if cmp "$OUTPUT/$img" "$GOLD/$img"; then
            echo "     Comparing images $GOLD/$img"
        else
            echo "FILES differ:"
            echo "    $OUTPUT"
            echo "    $GOLD"
            PASS=false
        fi
    done
else
    echo "Cinema Database: $OUTPUT does not exist"
    PASS=false
fi

if $PASS; then
    echo "PTN: PASS"
    echo "----------------------------------------------------------------------"
else
    echo "PTN: FAIL"
    echo "----------------------------------------------------------------------"
    exit 1
fi


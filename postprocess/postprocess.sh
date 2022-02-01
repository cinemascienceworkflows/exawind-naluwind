#!/bin/bash

source ./pantheon/env.sh > /dev/null 2>&1

echo "----------------------------------------------------------------------"
echo "PTN: Post-processing" 
echo "----------------------------------------------------------------------"

# --------------------------------------------------------------------
# copy python (paraview) and submit scripts to the result directory
cp postprocess/volume_rendering_cdb_extract.py $PANTHEON_RUN_DIR
cp postprocess/post_submit.sh $PANTHEON_RUN_DIR

# go to run dir and update the submit script
pushd $PANTHEON_RUN_DIR
mkdir cinema_databases

sed -i "s/<pantheon_workflow_jid>/${PANTHEON_WORKFLOW_JID}/" post_submit.sh
sed -i "s/<pantheon_post_jid>/${PANTHEON_POST_JID}/" post_submit.sh
sed -i "s#<pantheon_workflow_dir>#${PANTHEON_WORKFLOW_DIR}#" post_submit.sh
sed -i "s#<pantheon_run_dir>#${PANTHEON_RUN_DIR}#" post_submit.sh
sed -i "s#<compute_allocation>#${COMPUTE_ALLOCATION}#" post_submit.sh

# submit the job
echo "----------------------------------------------------------------------"
echo "PTN: submitting run ..."
echo "----------------------------------------------------------------------"
bsub post_submit.sh
popd
./sbang.sh postprocess/wait_for_completion.sh

# install cinema viewers
cp -rf inputs/cinema/* $PANTHEON_RUN_DIR/cinema_databases
# redirect the python notebook viewer to the database
sed -i "s#CINEMA_DB_PATH#$PANTHEON_CDB#" $PANTHEON_RUN_DIR/cinema_databases/cinema.ipynb 

pushd $PANTHEON_RUN_DIR > /dev/null 2>&1

TARNAME=cinema_databases
echo "----------------------------------------------------------------------"
echo "     packaging up cinema database to:"
echo "     $PANTHEON_DATA_DIR/${TARNAME}.tar.gz" 
echo "----------------------------------------------------------------------"

tar -czvf ${TARNAME}.tar.gz $TARNAME > /dev/null 2>&1
mv ${TARNAME}.tar.gz $PANTHEON_DATA_DIR

popd > /dev/null 2>&1

#!/bin/bash

#BSUB -J <pantheon_workflow_jid> 
#BSUB -P <compute_allocation> 
#BSUB -W 0:03
#BSUB -nnodes 1

module purge
#module load spectrum-mpi/10.4.0.3-20210112
source <pantheon_workflow_dir>/spack/share/spack/setup-env.sh
source <pantheon_workflow_dir>/loads
module list

jsrun --np 4 --nrs 1 --cpu_per_rs 4 --latency_priority cpu-cpu naluX -i <pantheon_run_dir>/<nalu_reg_test>.yaml -o <pantheon_run_dir>/<nalu_reg_test>.log

#!/bin/sh
echo "Starting script for west code"
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
BASEDIR=$(dirname "$SCRIPT")
INPUT=$1
URLS=$2
SCRIPT=$3
NO_OF_CORES=$4
MAX_SIZE=26214400

for i in $(echo $URLS | sed "s/,/ /g")
do
        SIZE=$(wget $i | --spider --server-response -O - 2>&1 | sed -ne '/Conten                                                                                                             t-Length/{s/.*: //;p}')
        if [ ! -z "$SIZE" ]
        then
                if [ "$SIZE" -le "$MAX_SIZE" ]
                then
                        wget -N $BASEDIR/$i
                fi
        fi
done
if [ "$SCRIPT" = "pw" ];
then
  mpirun --allow-run-as-root -np $NO_OF_CORES $BASEDIR/$SCRIPT.x -i $BASEDIR/$INPUT  > $BASEDIR/$SCRIPT.out
elif [ "$SCRIPT" = "wstat" -o "$SCRIPT" = "wfreq" ];
then
PW_INPUT=$5
  mpirun --allow-run-as-root -np $NO_OF_CORES $BASEDIR/pw.x -i $BASEDIR/$PW_INPUT  > $BASEDIR/pw.out
  mpirun --allow-run-as-root -np $NO_OF_CORES $BASEDIR/$SCRIPT.x -i $BASEDIR/$INPUT  > $BASEDIR/$SCRIPT.out
else
 echo "missing arguments. e.g. west pw.in http://www.quantum-simulation.org/potentials/sg15_oncv/upf/H_ONCV_PBE-1.0.upf,http://www.quantum-simulation.org/potentials/sg15_oncv/upf/Si_ONCV_PBE-1.1.upf pw 2"
fi
sleep 1d


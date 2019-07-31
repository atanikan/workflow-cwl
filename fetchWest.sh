#!/bin/sh
echo "Starting script for west code"
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
BASEDIR=$(dirname "$SCRIPT")
INPUTFILE=$1
INPUT=$(readlink -f "$1")
URLS=$2
SCRIPT=$3
NO_OF_CORES=$4
if [ ! -f $INPUT ];
then
echo "$INPUT missing"
exit 1
fi
if [ "$SCRIPT" = "pw" ];
then
sudo docker build -t west . 
sudo docker run --name westcontainer -v $INPUT:/app/docker_west/QEDIR/bin/$INPUTFILE -dit west $INPUTFILE $URLS $SCRIPT $NO_OF_CORES
while [ ! -f $SCRIPT.out ];
do
  sleep 2;
  sudo docker cp westcontainer:/app/docker_west/QEDIR/bin/$SCRIPT.out .
done
sudo docker stop westcontainer
sudo docker rm westcontainer
elif [ "$SCRIPT" = "wstat" -o "$SCRIPT" = "wfreq" ];
then
PW_INPUT=$(readlink -f "pw.in")
PW_INPUTFILE="pw.in"
sudo docker build -t west .
sudo docker run --name westcontainer -v $INPUT:/app/docker_west/QEDIR/bin/$INPUTFILE -v $PW_INPUT:/app/docker_west/QEDIR/bin/$PW_INPUTFILE -dit west $INPUT $URLS $SCRIPT $NO_OF_CORES $PW_INPUTFILE
while [ ! -f $SCRIPT.out ];
do
  sleep 2;
  sudo docker cp westcontainer:/app/docker_west/QEDIR/bin/$SCRIPT.out .
done
sudo docker stop westcontainer
sudo docker rm westcontainer
else
echo "Incorrect parameters. For e.g.  ./fetchWest.sh pw.in http://www.quantum-simulation.org/potentials/sg15_oncv/upf/H_ONCV_PBE-1.0.upf,http://www.quantum-simulation.org/potentials/sg15_oncv/upf/Si_ONCV_PBE-1.1.upf pw 2"
fi

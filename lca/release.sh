#!/usr/bin/env bash

die() 
{
	echo $@
	exit 1
}

if [ -z $1 ]
then
	echo requires name
	exit 1
fi
echo Releasing $1
mkdir $1 ||  die 'File exists'
cp -v *.* $1

echo 'Done'

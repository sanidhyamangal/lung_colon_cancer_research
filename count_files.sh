#!/bin/bash
#author = Fabio Alexandre Spanhol
#email = faspanhol@gmail.com
#revision = 07-24-2014


# pass in the directory to search on the command line, use $PWD if not arg received
rdir=${1:-$(pwd)}

# if $rdir is a file, get it's directory
if [ -f $rdir ]; then
    rdir=$(dirname $rdir)
fi

# first, find our tree of directories
for dir in $( find $rdir -type d -print ); do
    # get a count of directories within $dir.
    sdirs=$( find $dir -maxdepth 1 -type d | wc -l );
    # only proceed if sdirs is less than 2 ( 1 = self ).
    if (( $sdirs < 2 )); then 
        # get a count of all the files in $dir, but not in subdirs of $dir)
        files=$( find $dir -maxdepth 1 -type f | wc -l ); 
        echo "$dir : $files"; 
    fi
done

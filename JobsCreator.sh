#!/bin/bash
MyPath=$(pwd)
NAME=${MyPath%/GeneratorInterface*} #delete shortest match of pattern from the end

echo " "  >> Lunch.job
echo "#To lunch with the comand "  >> Lunch.job 
echo "#bsub -J NameOfTheJob -o output_file.out -e error_file.log -q 1nw < Lunch.job" >> Lunch.job
echo " "  >> Lunch.job  
echo "#!/bin/bash"  >> Lunch.job
echo " "  >> Lunch.job
echo "cd $NAME" >> Lunch.job 
echo 'eval `scram runtime -sh`' >> Lunch.job
echo "cd $MyPath" >> Lunch.job
echo "cmsRun $MyPath/$1" >> Lunch.job
echo "cp *.root $MyPath/Out.root" >> Lunch.job
echo "cp *.yoda $MyPath/Out.yoda" >> Lunch.job

#!/bin/bash
year=`date +%Y`
if [ $[$year % 400] -eq 0 ]; then
  echo "Это високосный год. В феврале 29 дней."
elif [ $[$year % 4] -eq 0 ]; then
        if [ $[$year % 100] -ne 0 ]; then
            echo "Это високосный год. В феврале 29 дней."
        else
          echo "Это не високосный год. В феврале 28 дней."
        fi
else
 echo "Это не високосный год. В феврале 28 дней."
fi



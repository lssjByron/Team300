#!/bin/bash

#echo STARTINGD RUN.SH FOR STARTING DJANGO SERVER PORT IS $PORT
#
#echo ENVIRONMENT VAIRABLES IN RUN.SH
#printenv 


#Change this values for django superuser
USER="test"
MAIL="broby2@uwo.ca"
PASS="test"

if [ -z "$VCAP_APP_PORT" ];
  then SERVER_PORT=5000;
  else SERVER_PORT="$VCAP_APP_PORT";
fi

#echo [$0] port is------------------- $SERVER_PORT
python manage.py makemigrations
python manage.py migrate --no-input
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('${USER}', '${MAIL}', '${PASS}')" | python manage.py shell

echo [$0] Starting Django Server...
python manage.py runserver 0.0.0.0:$SERVER_PORT --noreload
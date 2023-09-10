#!/bin/bash
source /home/dominhnhut01/work/miami_university/hackathon/penn-apps/env/bin/activate
python /home/dominhnhut01/work/miami_university/hackathon/penn-apps/manage.py runscript /home/dominhnhut01/work/miami_university/hackathon/penn-apps/scripts/ProcessData.py
sleep 30
source /home/dominhnhut01/work/miami_university/hackathon/penn-apps/env/bin/activate
python /home/dominhnhut01/work/miami_university/hackathon/penn-apps/manage.py runscript /home/dominhnhut01/work/miami_university/hackathon/penn-apps/scripts/ProcessData.py
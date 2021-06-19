# Analyst Job Telegram Bot

### Add to supervisor.conf

```
[program:analyst_bot]
command=/usr/bin/python3 /root/analyst-job-telegram-bot/main.py
stdout_logfile=/root/analyst-job-telegram-bot/main.log
stderr_logfile=/root/analyst-job-telegram-bot/main_err.log
autostart=true
autorestart=true
numprocs=1
```

```
[program:analyst_monitor]
command=/usr/bin/python3 /root/analyst-job-telegram-bot/monitoring.py
stdout_logfile=/root/analyst-job-telegram-bot/monitoring.log
stderr_logfile=/root/analyst-job-telegram-bot/monitoring.log
autostart=true
autorestart=true
numprocs=1
```

### Run screen task

`screen -dmS analyst_bot python3 main.py &`

`screen -dmS analyst_monitor python3 monitoring.py &`

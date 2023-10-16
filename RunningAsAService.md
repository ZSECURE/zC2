# Running as a Service

## Create the file in /etc/systemd/system.
```
sudo nano /etc/systemd/system/teamserver.service
```

## Paste the below into the file

```
[Unit]
Description=Cobalt Strike Team Server
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/home/<User>/<Folder-of-CobaltStrike>
ExecStart=/home/<User>/<Folder-of-CobaltStrike>/teamserver <IP-of-TeamServer> <Password> c2-profiles/normal/<Name-of-Profile>

[Install]
WantedBy=multi-user.target
```

## Reload the systemd manager

```
sudo systemctl daemon-reload
```

## Start the service

```
sudo systemctl start teamserver.service
```

## Check the status 

```
sudo systemctl status teamserver.service
```

## Enable on boot

```
sudo systemctl enable teamserver.service
```

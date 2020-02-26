# Fixing max req data transfer
# max_clients = worker_processes * worker_connections
exec { 'add_maxclients':
  command => "/bin/sed -i 's/worker_processes 4;/worker_processes 30;/g' /etc/nginx/nginx.conf | service nginx restart"
}


# This puppet file create and update the server and install nginx
# setup a new header in nginx condiguration and set the value for
# the $HOSTNAME
# ##############################################################
# #                         Puppet File                        #
# ##############################################################
#
# Update the sistem
exec { 'update-system':
  command => '/usr/bin/apt-get update',
}
# Install the deamon Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['update-system'],
}
# Running the service
service { 'nginx':
  ensure => running,
}
# Create a file and insert basic html
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Holberton School',
  require => Service['nginx'],
}
# add header, using sed
exec { 'add-header':
  command => '/bin/sed -i \'s/_;/_;\n\tadd_header \'X-Served-By\' \"\$HOSTANME\"; /g\' /etc/nginx/sites-available/default',
  require => Service['nginx'],
}

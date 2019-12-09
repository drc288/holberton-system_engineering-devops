# This Puppet file remove the procces killmenow
# provide with the shell
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}

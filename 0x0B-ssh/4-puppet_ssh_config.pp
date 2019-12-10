# Update the password authentication for not
file_line { 'set on the passwd':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
}
# Add the key
file_line { 'Using the key':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/holberton',
}

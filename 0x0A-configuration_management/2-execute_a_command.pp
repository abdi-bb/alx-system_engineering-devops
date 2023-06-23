# Puppet manifest to kill a process named 'killmenow'

exec { 'killmenow':
  command     => 'pkill -9 killmenow',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
}

# Puppet manifest to kill a process named 'killmenow'

exec { 'pkill':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
  subscribe   => File['/killmenow'],
}

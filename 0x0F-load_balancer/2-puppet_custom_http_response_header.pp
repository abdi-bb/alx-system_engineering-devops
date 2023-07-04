# 2-puppet_custom_http_response_header.pp

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to add custom HTTP response header
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "server_tokens off;\nmore_set_headers 'X-Served-By: ${::hostname}';",
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

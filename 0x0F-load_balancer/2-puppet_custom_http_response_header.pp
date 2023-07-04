# Install Nginx package
package { 'nginx':
  ensure => 'present',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
}

# Define the custom HTTP header
$custom_header_name = 'X-Served-By'
$custom_header_value = $::hostname

# Create a template file for the custom header configuration
file { '/etc/nginx/custom_http_header.conf':
  content => "add_header ${custom_header_name} \"${custom_header_value}\";",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Include the custom header configuration file in Nginx configuration
file_line { 'include_custom_http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "include /etc/nginx/custom_http_header.conf;",
  match => '^http {',
}

# Restart Nginx if the configuration changes
exec { 'nginx_reload':
  command => '/usr/sbin/service nginx reload',
  refreshonly => true,
}

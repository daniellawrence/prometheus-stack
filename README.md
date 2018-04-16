prometheus-stack
-------------------

A really really basic application that is setup with prometheus metrics.
What you get.

* 4 python web-servers
** basic application instrumentation
** node-exporter
* 1 haproxy
** balance traffic between the 4 web-servers
* 1 haproxy-exporter
** exports haproxy metrics
* 1 prometheus server
** configured to capture all the exporters


1000 words about how it works.
---------
!( prometheus-stack/images/prometheus-stack.png )[ prometheus-stack/images/prometheus-stack.png ]

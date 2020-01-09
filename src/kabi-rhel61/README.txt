Red Hat Kernel ABI
------------------

This text file tracks some of the changes made to Red Hat kernel ABI. For
each update release beginning with RHEL6.1, additions to the kABI are shown.

RHEL6.1
-------

The following symbols were added to the official kernel ABI in RHEL6.1:

* arp_send
* blk_queue_flush
* bus_register_notifier
* bus_unregister_notifier
* filemap_write_and_wait_range
* path_lookup
* register_inet6addr_notifier
* skb_gso_segment
* sysfs_schedule_callback
* unregister_inet6addr_notifier
* usb_free_urb
* usb_get_urb
* usb_register_driver

For further information, please contact Jon Masters <jcm@redhat.com>.

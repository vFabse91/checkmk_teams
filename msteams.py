#!/usr/bin/env python

register_notification_parameters("msteams",
    Dictionary(
        optional_keys = None,
        elements = [
            ("webhook",
             TextAscii(
                title = _("Webhook URL"),
                help = _("URL of the Webhook configured in MS Teams"),
             ),
            ),
            ("proxy",
             ListOfStrings(
                title = _("Proxies"),
                help = _("configure proxies")
             ),
            ),
        ]
    )
)

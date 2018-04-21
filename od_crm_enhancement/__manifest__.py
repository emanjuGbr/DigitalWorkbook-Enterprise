# Copyright (C) 2018 - TODAY, Emanju.de
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "CRM Enhancement",
    "summary": "Enhances functionality of CRM",
    "version": "11.0.1.0.0",
    "license": "AGPL-3",
    "author": "Bhavesh Odedra, Emanju",
    "category": "CRM",
    "website": "emanju.de",
    "depends": ["mail", "crm"],
    "data": [
        "data/mail_template_data.xml",
        "views/crm_view.xml",
        "wizard/mail_compose_message_view.xml",
    ],
    "installable": True,
}

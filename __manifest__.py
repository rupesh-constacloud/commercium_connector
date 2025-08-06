{
    'name': 'Commercium Connector',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Connect Odoo with Commercium',
    'depends': ['base','web'],
    'data': [
        'views/menu.xml',
        'views/settings_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'commercium_connector/static/src/css/custom_styles.css',
            'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css',
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
            # 'https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js',
            # 'https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js',
            # 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js',
            # 'commercium_connector/static/src/js/copy_button.js',
            # 'http://desktop-84a4aen:8069/commercium_connector/static/src/js/custom_js.js',
            'commercium_connector/static/src/js/custom_js.js',
            'commercium_connector/static/src/js/disconnect_confirm.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}

from odoo import models, fields, api
from urllib.parse import urlparse
import requests

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    platform_connected = fields.Boolean(
        string="Platform Connected",
        config_parameter='platform_connected'  # this connects it with ir.config_parameter
    )
    platform_id = fields.Char(
        string="Platform ID",
        config_parameter='platform_id'
    )

    def get_values(self):
        res = super().get_values()
        param = self.env['ir.config_parameter'].sudo()
        platform_connected = param.get_param('platform_connected') or 'False'
        res.update({
            'platform_connected': platform_connected.lower() in ['1', 'true', 'yes']
        })
        return res

    def set_values(self):
        super().set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('platform_connected', str(self.platform_connected))

    test_username = fields.Char(
        string="Username : ",
        config_parameter='test_connector.username'
    )
    test_password = fields.Char(
        string="Password : ",
        config_parameter='test_connector.password'
    )
    test_db = fields.Char(
        string="DB Name : ",
        config_parameter='test_connector.db'
    )
    test_domain = fields.Char(
        string="Domain : ",
        config_parameter='test_connector.domain'
    )

    @api.model
    def disconnect_platform(self):
        print('Hello - disconnect_platform')
        try:
            # Dummy URL – replace with actual test endpoint
            url = f"https://test-dev.constacloud.com/handle-oauth-callback?available_platform_name=ODOO&platform_id={self.platform_id}"
            print("url : ", url)
            response = requests.post(f"{url}", json={
                "platform_id": self.env.company.id,  # or any identifier
            })
            print("response.status_code : ", response.status_code)
            print("response.json() : ", response.json())

            if response.status_code == 200:
                result = response.json()
                if result.get("status") == "success":
                    # Set flag off
                    self.env['ir.config_parameter'].sudo().set_param("platform_connected", '0')
                    return {"success": True}
                else:
                    return {"success": False, "error": result.get("message", "Unknown error")}
            else:
                return {"success": False, "error": "HTTP Error {}".format(response.status_code)}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def action_connect_platform(self):
        print("`action_connect_platform` method called")
        self.ensure_one()
        self.platform_connected = True

    def action_disconnect_platform(self):

        error_message = "Platform disconnection failed. Please try again later."
        
        # Dummy URL – replace with actual test endpoint
        url = f"https://test-dev.constacloud.com/market_connect/handle-oauth-callback?available_platform_name=ODOO&platform_id={self.platform_id}"
        response = requests.get(f"{url}")
        if response.status_code == 200:
            response_data = response.json()
            response_status_code = response_data.get("status_code")
            if response_status_code not in [200, 201]:
                error_message = response_data.get("message", "Unknown error")

            if response_status_code in [200, 201]:

                self.env['ir.config_parameter'].sudo().set_param('platform_connected', False)
                self.ensure_one()
                self.platform_connected = False

                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Platform Disconnected',
                        'message': 'You have successfully disconnected the platform.',
                        'type': 'success',
                        'sticky': False,
                        'next': {
                            'type': 'ir.actions.client',
                            'tag': 'reload',
                        }
                    }
                }



        else:
            error_message = f"HTTP Error {response.status_code}: {response.text}"
            
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': ('Platform Disconnection Failed'),
                'message': error_message,
                'type': 'danger',
                'sticky': False,
            }
        }

    def copy_test_domain(self):
        # dummy method, button click se kuch nahi hoga
        return True

    def copy_test_username(self):
        # dummy method, button click se kuch nahi hoga
        return True

    def copy_test_password(self):
        # dummy method, button click se kuch nahi hoga
        return True

    def copy_test_db(self):
        # dummy method, button click se kuch nahi hoga
        return True

    @api.model
    def default_get(self, fields_list):
        res = super(ResConfigSettings, self).default_get(fields_list)

        url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        parsed_url = urlparse(url)
        clean_domain = parsed_url.netloc
        
        # Populate autofill values dynamically from session/db
        res.update({
            'test_username': self.env.user.login,
            'test_db': self._cr.dbname,
            'test_domain': clean_domain,
        })

        return res

    def action_connect_test(self):
        # Optional if you still want to use the connect button
        self.ensure_one()
        # _logger.info(f"Trying to connect with: {self.test_username} / {self.test_db}")
        print(f"Trying to connect with: {self.test_username} / {self.test_db}")
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': ('Connection'),
                'message': ('Auto-filled credentials are displayed successfully.'),
                'type': 'success',
                'sticky': False,
            }
        }

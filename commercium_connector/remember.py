CREATE USER odoo_user WITH PASSWORD 'password@123';


CREATE USER odoo_user WITH PASSWORD '12345'

ALTER USER odoo_user WITH PASSWORD 'new_secure_password';

ALTER ROLE odoo_user WITH PASSWORD 'password@123';



-- restar server 
python odoo-bin -c odoo.conf

python odoo-bin shell -d odoo_db

python odoo-bin -d odoo_db -u web --stop-after-init

python odoo-bin -c odoo.conf --dev=all

python odoo-bin -u commercium_connector -d odoo_test_1

python odoo-bin -u commercium_connector -d your_db_name





http://desktop-84a4aen:8069/web/login
odoo_test_1
rupesh.constacloud@gmail.com
123456789000
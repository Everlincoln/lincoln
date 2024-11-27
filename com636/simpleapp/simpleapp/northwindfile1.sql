select o.customer_id,c.first_name,c.last_name,od.order_id, 
	od.product_id, p.product_code, p.product_name,
    od.quantity,od.unit_price,od.quantity * od.unit_price as total_price
from order_details od
	inner join products p on od.product_id = p.id
	inner join orders o on od.order_id = o.id
	inner join customers c on o.customer_id = c.id
order by o.customer_id,od.order_id
;
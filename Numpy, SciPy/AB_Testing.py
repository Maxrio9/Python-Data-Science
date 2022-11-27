import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers
payment_history = noshmishmosh.money_spent

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

baseline_percent = paying_visitor_count / total_visitor_count * 100
print(baseline_percent)
# Prints 18.6

average_payment = np.mean(payment_history)
print(average_payment)
# Prints 26.54

new_customers_needed = np.ceil(1240 / average_payment)
print(new_customers_needed)
# Prints 47

percentage_point_increase = new_customers_needed / total_visitor_count * 100
print(percentage_point_increase)
# Prints 9.4

mde = percentage_point_increase / baseline_percent * 100
print(mde)
# Prints 50.54

# Sample size for an A/B Test with a significance threshold of 10% would therefore be:
ab_sample_size = 490
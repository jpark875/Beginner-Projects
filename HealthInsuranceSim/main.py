import health

healthins1 = health.HealthInsurance("UVA")

print(healthins1.get_data())

healthins1.add_policy("Gold", 5000, 20, 10000)
print(healthins1.get_data())

healthins1.add_policy("Silver", 2500, 20, 5000)
print(healthins1.get_data())

healthins1.add_policy("Bronze", 1000, 40, 2500)
print(healthins1.get_data())

print(healthins1.get_deduc())

print(healthins1.get_coin())

print(healthins1.get_stlo())

print(healthins1.pocket_cost("Gold"))

print(healthins1.policy_info("Silver"))

print(str(healthins1))
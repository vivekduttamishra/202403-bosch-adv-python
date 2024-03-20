import org

bosch=org.get_organization('bosch',50)

for emp in bosch:
    print(emp._name, emp._isPermanent)
import random

def ip4():
    return str(random.randint(0,255))
print(f"Random IPv4: {ip4()}.{ip4()}.{ip4()}.{ip4()}")

def ip6():
    rhex = str(hex(random.randint(0,255))).upper()
    return rhex[2:]
print(f"Random IPv6: {ip6()}{ip6()}.{ip6()}{ip6()}.{ip6()}{ip6()}.{ip6()}{ip6()}")
print(f"Random Mac: {ip6()}.{ip6()}.{ip6()}.{ip6()}.{ip6()}.{ip6()}")
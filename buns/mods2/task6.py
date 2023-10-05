domain = input()

last_dot_index = len(domain) - 1
while domain[last_dot_index] != '.':
    last_dot_index -= 1

domain1 = domain[last_dot_index+1:]
last_domain = domain[:last_dot_index]
print(domain1)

while '.' in last_domain:
    last_dot_index = last_domain.rfind('.')
    domain2 = last_domain[last_dot_index+1:]
    print(domain2)
    last_domain = last_domain[:last_dot_index]

print(last_domain)

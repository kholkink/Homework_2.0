with open('nginx_logs.txt') as logs:
	mass = []
	spammer_dict = {}
	for line in logs:
		split_line = line.split()
		mass.append((split_line[0], split_line[5].strip('"'), split_line[6]))
		spammer_dict.setdefault(split_line[0], 0)
		spammer_dict[split_line[0]] += 1
spammer_dict = sorted(spammer_dict.items(), key=lambda x: x[1])
print(spammer_dict)
def reliabilty(v, i, T, age, w):
	sd_v # = std deviation of voltage
	sd_i # = std deviation of current
	sd_t # = std deviation of temp
	sd_w # = std deviation of w
	sd_age # = std deviation of eff
	a_v # = std deviation of voltage
	a_i # = std deviation of current
	a_t # = std deviation of temp
	a_w # = std deviation of w
	a_age # = std deviation of eff
	reliabilty = 5
	if v > a_v + 1.5*sd_v:
		reliabilty -=1
	if i > a_i + 1.5*sd_i:
		reliabilty -=1
	if T > a_t + 1.5*sd_t:
		reliabilty -=1
	if w > a_w + 1.5*sd_w:
		reliabilty -=1
	if age > a_age + 1*sd_age:
		reliabilty -=1

	if reliabilty = 5:
		return 'Highly reliable'
	if reliabilty =3 or reliabilty = 4:
		return 'Moderately reliable'
	if reliabilty = 1 or reliabilty = 2:
		return 'Less reliable'
	if reliabilty = 0:
		return 'Not reliable'


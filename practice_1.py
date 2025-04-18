def narde_sof(params):
	if params["result"] == "white":
		verdict = 1
	elif params["result"] == "black":
		verdict = -1
	else:
		verdict = 0

	pips_diff = params["black_pips"] - params["white_pips"]
	white_primes = sum([2**p_len for p_len in params["white_primes"]])
	black_primes = sum([2**p_len for p_len in params["black_primes"]])

	return 10000 * verdict \
			+ 3 * pips_diff \
			+ 5 * white_primes \
			- 5 * black_primes \
			- 100 * params["white_trapped"] \
			+ 100 * params["black_trapped"] \
			+ 50 * params["white_in_home"] \
			- 50 * params["black_in_home"]


sit_1 = {
	"result": "no",
	"white_pips": 303,
	"black_pips": 336,
	"white_primes": [1, 2, 1, 1, 1],
	"black_primes": [1, 1, 4],
	"white_trapped": 0,
	"black_trapped": 0,
	"white_in_home": 0,
	"black_in_home": 0
}

sit_2 = {
	"result": "no",
	"white_pips": 325,
	"black_pips": 324,
	"white_primes": [5, 2, 1],
	"black_primes": [1, 4, 1, 1],
	"white_trapped": 0,
	"black_trapped": 0,
	"white_in_home": 0,
	"black_in_home": 0
}

sit_3 = {
	"result": "no",
	"white_pips": 170,
	"black_pips": 112,
	"white_primes": [1, 1, 1, 1, 1, 4],
	"black_primes": [1, 1, 1, 1, 1, 4],
	"white_trapped": 0,
	"black_trapped": 0,
	"white_in_home": 4,
	"black_in_home": 5
}

sit_4 = {
	"result": "no",
	"white_pips": 169,
	"black_pips": 76,
	"white_primes": [1, 1, 1, 8],
	"black_primes": [1, 4, 1],
	"white_trapped": 0,
	"black_trapped": 1,
	"white_in_home": 3,
	"black_in_home": 5
}

print(narde_sof(sit_1))
print(narde_sof(sit_2))
print(narde_sof(sit_3))
print(narde_sof(sit_4))

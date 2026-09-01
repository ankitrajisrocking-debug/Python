import numpy as np

marks = [ 78, 85, 92, 67, 88, 73, 95, 81, 76, 89 ]
temperatures = [ 28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5 ]
sales = [ 12500, 13800, 14200, 11900, 15100, 14750, 16000 ]


def stats_without_numpy( data ):
	n = len(data)
	s = sorted( data )
	mean = sum ( data ) / n
	median = ( s[n//2] if n % 2 else ( s[n//2 - 1] + s[n//2 ]) / 2)
	variance = sum(( x - mean ) ** 2 for x in data) / n
	std = variance ** 0.5
	return { 
		"mean": mean, "median": median, "std": std,
		"min": min( data ), "max": max( data )
		}
	
def stats_with_numpy(data):
	arr = np.array(data)
	return {
		"mean" : np.mean(arr), "median" : np.median( arr ),
		"std" : np.std( arr ), "min" : np.min(arr), "max": np.max(arr)
	}
	
for name, data in [ ("Marks" , marks), ( "Temperatures", temperatures), ("Sales", sales)]:
	print(f"\n--- {name} ---")
	print("without numpy:", stats_without_numpy(data))
	print("with numpy  : " , stats_with_numpy(data)) 
	

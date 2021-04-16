from multiprocessing import Pool
from multiprocessing import freeze_support
from multiprocessing import Manager
from numpy import uint64



def mains(values):
	#Pattern: BadDal251 / GetMet2567 / LolKek3566
	print("Stream started")
	lets_big 		= "BCDFGHJKLMNPRSTVWXZ"
	lets_small 		= "bcdfghjklmnprstvwxz"
	lets_small_vo 	= "aeiouy"
	res = uint64(0)
	for i in range(len(lets_big)):
		for j in range(len(lets_small_vo)):
			for k in range(len(lets_small)):
				for l in range(len(lets_big)):
					for m in range(len(lets_small_vo)):
						for n in range(len(lets_small)):
							for x in range(values[0],values[1]):
								res +=1
	print("Stream completed")
	return round(res/1000000) 


if __name__ == "__main__": 
	manager = Manager()
	dicto = manager.dict()
	freeze_support()
	xx = []
	
#=========================
	print("Number of password options by pattern\n")
	print("**********************\n\n")

	values = [(1000,1999), (2000,2999), (3000,3999), (4000,4999), (5000,5999), (6000,6999),(7000,7999),(8000,8999),(9000,9999)]

	with Pool(9) as p:
		result = sum(p.map(mains, values))
		print("About", result, "millions")
		file = open("RESULT.txt", 'w')
		file.write("About "+str(result)+" millions")
		file.close()

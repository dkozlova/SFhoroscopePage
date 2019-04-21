from random import randrange 

encoding = 'utf-8'

def generate_prophecies():
	times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
	advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
	promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]

	generated_prophecies = []
	i = 0

	while i < 6:
		prediction = []
		k = 0
		
		while k < 2:
			time = times[(randrange(0, len(times)))]
			advice = advices[(randrange(0, len(advices)))]
			promise = promises[(randrange(0, len(promises)))]
			prediction.append(time.capitalize() + ' ' + advice + ' ' + promise + '.')
			k += 1
			
		generated_prophecies.append(prediction[0] + ' ' + prediction[1]) 
		i += 1

	return (generated_prophecies)
	
if __name__ == '__main__':
	print (generate_prophecies())

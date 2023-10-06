leftMission = 3		
leftCannibals = 3		 
rightMissions=0		 
rightCannibals=0		 
userMission = 0	 
userCannibals = 0	 
k = 0
print("\nM M M C C C |	 --- | \n")
try:
	while(True)
		while(True):
			print("Left side -> right side river travel")
			userMission = int(input("Enter number of Missionaries travel => "))	
			userCannibals = int(input("Enter number of Cannibals travel => "))

			if((userMission==0)and(userCannibals==0)):
				print("Empty travel not possible")
				print("Re-enter : ")
			elif(((userMission+userCannibals) <= 2)and((leftMission-userMission)>=0)and((leftCannibals-userCannibals)>=0)):
				break
			else:
				print("Wrong input re-enter : ")
		leftMission = (leftMission-userMission)
		leftCannibals = (leftCannibals-userCannibals)
		rightMissions += userMission
		rightCannibals += userCannibals

		print("\n")
		for i in range(0,leftMission):
			print("M ",end="")
		for i in range(0,leftCannibals):
			print("C ",end="")
		print("| --> | ",end="")
		for i in range(0,rightMissions):
			print("M ",end="")
		for i in range(0,rightCannibals):
			print("C ",end="")
		print("\n")

		k +=1

		if(((leftCannibals==3)and (leftMission == 1))or((leftCannibals==3)and(leftMission==2))or((leftCannibals==2)and(leftMission==1))or((rightCannibals==3)and (rightMissions == 1))or((rightCannibals==3)and(rightMissions==2))or((rightCannibals==2)and(rightMissions==1))):
			print("Cannibals eat missionaries:\nYou lost the game")

			break

		if((rightMissions+rightCannibals) == 6):
			print("You won the game : \n\tCongrats")
			print("Total attempt")
			print(k)
			break
		while(True):
			print("Right side -> Left side river travel")
			userightMissions = int(input("Enter nuserMissionber of Missionaries travel => "))
			userightCannibals = int(input("Enter nuserMissionber of Cannibals travel => "))
			
			if((userightMissions==0)and(userightCannibals==0)):
					print("Empty travel not possible")
					print("Re-enter : ")
			elif(((userightMissions+userightCannibals) <= 2)and((rightMissions-userightMissions)>=0)and((rightCannibals-userightCannibals)>=0)):
				break
			else:
				print("Wrong input re-enter : ")
		leftMission += userightMissions
		leftCannibals += userightCannibals
		rightMissions -= userightMissions
		rightCannibals -= userightCannibals

		k +=1
		print("\n")
		for i in range(0,leftMission):
			print("M ",end="")
		for i in range(0,leftCannibals):
			print("C ",end="")
		print("| <-- | ",end="")
		for i in range(0,rightMissions):
			print("M ",end="")
		for i in range(0,rightCannibals):
			print("C ",end="")
		print("\n")

	

		if(((leftCannibals==3)and (leftMission == 1))or((leftCannibals==3)and(leftMission==2))or((leftCannibals==2)and(leftMission==1))or((rightCannibals==3)and (rightMissions == 1))or((rightCannibals==3)and(rightMissions==2))or((rightCannibals==2)and(rightMissions==1))):
			print("Cannibals eat missionaries:\nYou lost the game")
			break
except EOFError as e:
	print("\nInvalid input please retry !!")

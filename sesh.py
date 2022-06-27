#Fun little activity for gym sessions with friends

import random


print("What are you working out today?")

workoutDay = str(input("arms, legs, back, jump training, abs, compound, random?: "))
workoutSets = random.choice([3,4,5,6])
workoutList = ["arms", "legs", "back", "jump training", "abs", 'compound']

if workoutDay.lower() == 'arms' :
	workoutExercisesInput = input("How many exercises? (max 5): ")
	workoutActivities = int(workoutExercisesInput)
	Activities = ['Bicep Curl', 'Row', 'pushups', 'tricep pull-down', 'standing shoulder press', 'dips', ]
	updatedActivities = random.sample(Activities, workoutActivities)
	for activity in updatedActivities :	
		print(activity)

	print(f"{workoutSets} sets!!!!")

elif workoutDay.lower() == 'legs' :
	workoutExercisesInput = input("How many exercises? (max 5): ")
	workoutActivities = int(workoutExercisesInput)
	Activities = ['Squat', 'Deadlifts', 'Walking Lunges', 'knee-bends', 'hamstring curls', 'step-ups', ]
	updatedActivities = random.sample(Activities, workoutActivities)
	for activity in updatedActivities :	
		print(activity)

	print(f"{workoutSets} sets!!!!")	
	
elif workoutDay.lower() == 'back' :
	workoutExercisesInput = input("How many exercises? (max 5): ")
	workoutActivities = int(workoutExercisesInput)
	Activities = ['lat pull downs', 'Deadlifts', 'pull-ups', 'Row', 'chest supported row', 'band twists', ]
	updatedActivities = random.sample(Activities, workoutActivities)
	for activity in updatedActivities :	
		print(activity)

	print(f"{workoutSets} sets!!!!")	

elif workoutDay.lower() == 'jump training' :
	workoutExercisesInput = input("How many exercises? (max 5): ")
	workoutActivities = int(workoutExercisesInput)
	Activities = ['step-ups', 'standing jump', 'fall to jump', 'deadlift lookalike thingy', 'the cleaner', 'calf raises', ]
	updatedActivities = random.sample(Activities, workoutActivities)
	for activity in updatedActivities :	
		print(activity)

	print(f"{workoutSets} sets!!!!")	

elif workoutDay.lower() == 'abs' :
	workoutExercisesInput = input("How many exercises? (max 5): ")
	workoutActivities = int(workoutExercisesInput)
	Activities = ['sit-ups', 'Russian twists', 'weighted sit-ups', 'full body twists (with bands)', 'plank', 'leg raises', ]
	updatedActivities = random.sample(Activities, workoutActivities)
	for activity in updatedActivities :	
		print(activity)

	print(f"{workoutSets} sets!!!!")

elif workoutDay.lower() == 'compound' :
	workoutExercisesInput = input("How many exercises? (max 5): ")
	workoutActivities = int(workoutExercisesInput)
	Activities = ['bench', 'squats', 'deadlift', 'circuit training', 'plank']
	updatedActivities = random.sample(Activities, workoutActivities)
	for activity in updatedActivities :	
		print(activity)

	print(f"{workoutSets} sets!!!!")

elif workoutDay.lower() == 'random' :
	print("WIP - Stay tuned")
else :
	print("invalid input.")






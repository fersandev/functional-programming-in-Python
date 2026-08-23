names = ["ana", "BOB", "caRLOS", "diana"]
lowered_generator = (n.lower() for n in names)
capitalized_generator = (n.capitalize() for n in lowered_generator)
long_names_generator = (n for n in capitalized_generator if len(n) > 4)
long_names = list(long_names_generator)
print(long_names) # ['Carlos', 'Diana']

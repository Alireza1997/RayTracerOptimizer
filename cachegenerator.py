import os

from pathlib import Path

# Get tx positions (should import from a file)
tx_positions = [(5.0,5.0,5.0)]

# For exevery tranceiever
for tx in tx_positions:
	txX,txY,txZ = tx
	
	# Create cache dir
	cache_dir = Path("Cache/x"+str(txX)+"y"+str(txY)+"z"+str(txZ))
	cache_dir.mkdir(parents=True, exist_ok=True)

	# Generate config
	with open("Config_og.xml") as original_xml:
		
		with open("Config.xml",'w') as new_xml:
			for line in original_xml:
				if "source_position" in line:
					line = "<source_position> <x>" + str(txX) + "</x> <y> " + str(txY) +"</y> <z>" + str(txZ) + "</z> </source_position>\n"
					# print (line)
				new_xml.write(line)

	# Run Sim
	os.system("./RayTubeTracing")

	# Save cache
	os.rename("./Receivers.vtk", cache_dir/"Receivers.vtk")
	os.rename("./ReceivedPowers.csv", cache_dir/"ReceivedPowers.csv")
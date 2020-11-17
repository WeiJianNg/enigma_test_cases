import os
import subprocess

def compare(test_path, output_path):
    test = open(test_path)
    out = open(output_path)
    
    str1 = test.readline()
    str2 = out.readline()
    test.close()
    out.close()
    return str1 == str2

user = input("Input Imperial Username (i.e. wjn13): ")
# Create folder for rotors, reflectors and plugboard settings
# and create folder for output
subprocess.call(["mkdir", "output"])

# Copy settings from lab folder
subprocess.call(["cp", "-R", "../mcslab_2_" + user + "/rotors", "./rotors"])
subprocess.call(["cp", "-R", "../mcslab_2_" + user + "/plugboards", "./plugboards"])
subprocess.call(["cp", "-R", "../mcslab_2_" + user + "/reflectors", "./reflectors"])
subprocess.call(["cp", "../mcslab_2_" + user + "/enigma", "./"])

# create two rotors position files
with open("rotors/2_rotor.pos", "w") as f:
    f.write("3 4")

with open("rotors/1_rotor.pos", "w") as f:
    f.write("3")

with open("rotors/no_rotor.pos", "w") as f:
    f.write("")

# add notches to rotors VI;
with open("rotors/VI.rot", "a") as f:
    f.write(" 16 14 18")

# Generate Output
os.system(" ".join(["./enigma", "plugboards/null.pb", "reflectors/I.rf", "rotors/no_rotor.pos", "< input.txt", "> ./output/test1.txt"]))
os.system(" ".join(["./enigma", "plugboards/null.pb", "reflectors/I.rf", "rotors/V.rot", "rotors/1_rotor.pos", "< input.txt", "> ./output/test2.txt"]))
os.system(" ".join(["./enigma", "plugboards/null.pb", "reflectors/I.rf", "rotors/I.rot", "rotors/VI.rot", "rotors/2_rotor.pos", "< input.txt", "> ./output/test3.txt"]))
os.system(" ".join(["./enigma", "plugboards/I.pb", "reflectors/I.rf", "rotors/I.rot", "rotors/II.rot", "rotors/III.rot", "rotors/I.pos", "< input.txt", "> ./output/test4.txt"]))
os.system(" ".join(["./enigma", "plugboards/II.pb", "reflectors/I.rf", "rotors/III.rot", "rotors/II.rot", "rotors/I.rot", "rotors/II.pos", "< input.txt", "> ./output/test5.txt"]))
os.system(" ".join(["./enigma", "plugboards/III.pb", "reflectors/I.rf", "rotors/VI.rot", "rotors/V.rot", "rotors/VII.rot", "rotors/III.pos", "< input.txt", "> ./output/test6.txt"]))
os.system(" ".join(["./enigma", "plugboards/IV.pb", "reflectors/I.rf", "rotors/I.rot", "rotors/II.rot", "rotors/VI.rot", "rotors/II.pos", "< input.txt", "> ./output/test7.txt"]))
os.system(" ".join(["./enigma", "plugboards/null.pb", "reflectors/I.rf", "rotors/I.rot", "rotors/II.rot", "rotors/VI.rot", "rotors/II.pos", "< input.txt", "> ./output/test8.txt"]))

for i in range(1, 9):
    isPass = compare("test_case/test" + str(i) + ".txt", "output/test" + str(i) + ".txt")
    if isPass:
        print("test case" + str(i) + " - Passed")
    else:
        print("test case" + str(i) + " - Failed")

# Remove setting files from test folder
subprocess.call(["rm", "-r", "-f", "enigma"])
subprocess.call(["rm", "-r", "-f", "rotors/"])
subprocess.call(["rm", "-r", "-f", "plugboards/"])
subprocess.call(["rm", "-r", "-f", "reflectors/"])
subprocess.call(["rm", "-r", "-f", "output/"])


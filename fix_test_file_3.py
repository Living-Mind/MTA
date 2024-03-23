def xml_automation():
    with open("test-suite.xml", "r") as file:

        lines = file.readlines()
        #print(lines)
        with open("test-automated.xml", "a") as new_file:
            for index, line in enumerate(lines):

               if "<description>" in line and "Recovery" in lines[index+1]:
                   edited_line = line.replace("Tests", "(Automated) Tests")
                   new_file.write(edited_line)
                   #print(edited_line)
               else:
                    new_file.write(line)

    file.close()
    new_file.close()
         
xml_automation() 
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("GEO_studies"):
    f.extend(filenames)
    break

var = ["!dataset_title =", "!dataset_sample_count =", "!dataset_update_date =", "!dataset_platform_organism =", "!dataset_pubmed_id =", "!dataset_platform =", "!dataset_platform_technology_type =", "!dataset_reference_series =", "!dataset_description ="]
var_val = []

f_Out = open("output.txt", 'w')

for item in f:
    _file = open("GEO_studies/" + item, "r")
    f_Out.write("++++++++####### NEW FILE #######++++++++\n")
    for lines in _file:
        for items in var:
            if items in lines:
                print(lines.strip())
                f_Out.write(lines)

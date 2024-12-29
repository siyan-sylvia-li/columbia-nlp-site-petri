import json

if __name__ == "__main__":
    data_file = json.load(open("cu_nlp_people.json"))
    phds = data_file["Ph.D. Graduates"]
    curr_yml = open("phd_grads.yml", "w+")
    for p in phds:
        curr_yml.write("\n- name: " + p[0] + "\n  url: "  + p[1] + "\n")
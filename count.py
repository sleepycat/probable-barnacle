import yaml

file = open("all_2015_20160907.yml", "r")
dataset = yaml.load(file)

projects = 0
collaborative_projects = 0
dfo_projects = 0
dfo_collaborative_projects = 0

for project in dataset:
    projects = projects + 1
    all_collaborators = project["project_lead"] + project["project_team"] + project["collaborators"]
    organizations = set()
    for collaborator in all_collaborators:
        organizations.add(collaborator["org"])
    if "Fisheries and Oceans Canada" in organizations:
        dfo_projects = dfo_projects + 1
    if len(organizations) > 1:
        collaborative_projects = collaborative_projects + 1
        if "Fisheries and Oceans Canada" in organizations:
            dfo_collaborative_projects = dfo_collaborative_projects + 1

template = "Total projects: {0}, collaborative: {1}, DFO projects: {2}, DFO collaborative projects: {3}"
summary = template.format(projects, collaborative_projects, dfo_projects, dfo_collaborative_projects)
print(summary)

file.close()

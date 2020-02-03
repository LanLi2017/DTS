'''
 Lan Li
 software: OpenRefine
 folder: Openrefien client - py3
 project id : 1942440243171
'''
import json

from google_refine.refine import refine


# load json file through OpenRefine python client library
def load_recipe(project_id, rep_path):
    rep= refine.RefineProject(refine.RefineServer(),project_id).get_operations()
    with open(f'../OpenRefine_recipe/{rep_path}.json','w')as fout:
        json.dump(rep,fout, indent=4)


def main():
    load_recipe(1942440243171,'demo1')


if __name__=='__main__':
    main()
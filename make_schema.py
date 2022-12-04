from cv.schema import CurriculumVitae

with open('cv.json', 'w') as f:
    f.write(CurriculumVitae.schema_json(indent=2))

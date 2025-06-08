def category_check(type_of_cat: str) -> str:
    if type_of_cat in ['Fire','Water','Electric','Grass','Ice','Psychic','Dragon','Dark']:
        return 'Special'
    else:
        return 'Physical'
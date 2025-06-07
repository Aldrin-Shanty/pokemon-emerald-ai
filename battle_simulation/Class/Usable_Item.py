class UsableItem:

    def __init__(self, item_name : str, heal : int = 0,status_cure : str = None, pp : int = 0,
                 quantity : int = 1,pp_all : int = 0,percent_heal : int = 0) -> None:

        self.item_name = item_name
        self.pp = pp
        self.pp_all = pp_all
        self.heal = heal
        self.percent_heal = percent_heal
        self.status_cure = status_cure
        self.quantity = quantity

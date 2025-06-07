class UsableItem:

    def __init__(self, item_name, heal=0,status_cure=None,pp=0,quantity=1,pp_all=0,percent_heal=0):

        self.item_name=item_name
        self.pp=pp
        self.pp_all=pp_all
        self.heal=heal
        self.percent_heal=percent_heal
        self.status_cure=status_cure
        self.quantity=quantity

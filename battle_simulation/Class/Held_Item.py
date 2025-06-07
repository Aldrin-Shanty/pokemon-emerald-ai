class HeldItem:

    def __init__(self,item_name : str,consumable : bool = True ) -> None:

        self.item_name = item_name
        self.consumable = consumable
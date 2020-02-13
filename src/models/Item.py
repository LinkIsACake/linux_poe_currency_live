class Currency:

    CATEGORIES = ['Orb',
                  'Shard',
                  'Oil',
                  'Essence',
                  'Fossil',
                  'Resonator',
                  'Incubator',
                  'Catalyst']

    name:str
    id:str
    categorie:str

    @staticmethod
    def get_type(name:str):
        categoeries = []
        for categorie in Currency.CATEGORIES:
            if name.find(categorie) != -1:
                categoeries.append(categorie)
        if len(categoeries) == 0:
            categoeries.append("Others")
        return categoeries

    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.type = Currency.get_type(name)


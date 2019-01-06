import uuid

""" Attributes : name,climate,terrain,apparitions,population,_id """


class Planet(object):

    def __init__(self, name: str, climate: list, terrain: list, apparitions:None, population: None, _id: None):

        if _id is None:
            self._id = uuid.uuid4
        else:
            self._id = _id
            self.name = name
            self.climate = climate
            self.terrain = terrain

        if apparitions is None:
            self.apparitions = None
        else:
            self.apparitions = apparitions
    
        if population is None:
            self.population = None
        else:
            self.population = population

    """
        The from_dict method comes in handy when we have to create a model 
        from data coming from another layer (such as the database layer or the query string of the REST layer).
    """

    @classmethod
    def from_dict(cls,planet_dict):
        planet = Planet(
            _id = planet_dict["_id"],
            name=planet_dict["name"],
            climate=planet_dict["climate"],
            terrain=planet_dict["terrain"],
            apparitions=planet_dict["apparitions"] if "apparitions" in planet_dict else None,
            population=planet_dict["population"] if "population" in planet_dict else None,
        )
        return planet

    def to_dict(self):
        return {
            '_id': self._id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'apparitions': self.apparitions,
            'population': self.population,
            
        }
    
    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

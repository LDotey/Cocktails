from models.__init__ import CURSOR, CONN

class State: 
    all = {}

    def __init__(self, name, population, region, id=None):
        self.name = name
        self.population = population
        self.region = region
        self.id = id


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Length must be between 1 and 15 characters")
        self._name = name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        if not isinstance(population,int): 
            raise ValueError("Population must be an Integer")
        self._population = population

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if not isinstance(region, str):
            raise ValueError("Region must be a string")
        self._region = region


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS states (
            id INTEGER PRIMARY KEY,
            name TEXT,
            population INT, 
            region TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS states"
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        sql = """
            INSERT INTO states (name, population, region)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.population, self.region))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    
    def update(self):
        sql= "UPDATE states SET name = ?, population =?, region = ? WHERE id = ?"

        CURSOR.execute(sql, (self.name, self.population, self.region, self.id))
        CONN.commit()

    def delete(self): 
        sql = "DELETE FROM states WHERE id = ?" 

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None 

    
    @classmethod
    def create(cls, name, population, region):
        state = cls(name, population, region)
        state.save()
        return state

    @classmethod
    def instance_from_db(cls, row):
        state = cls.all.get(row[0])
        if state:
            state.name = row[1]
            state.population = row[2]
            state.region = row[3]
        else:
            state = cls(row[1], row[2], row[3])
            state.id = row[0]
            cls.all[state.id] = state
        return state

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM states
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM states
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM states
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None



    









    
        


    
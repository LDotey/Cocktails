from models.__init__ import CURSOR, CONN
from models.state import State

class City: 
    all = {}

    def __init__(self, name, city_population, state_id, id=None):
        self.name = name
        self.city_population = city_population
        self.id = id
        self.state_id = state_id


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city_population(self):
        return self._city_population

    @city_population.setter
    def city_population(self, city_population):
        if isinstance(city_population, int):
            self._city_population = city_population
        else:
            raise ValueError("Population must be an integer")

    @property
    def state_id(self):
        return self._state_id
 
    @state_id.setter
    def state_id(self, state_id):
        if isinstance(state_id, int) and State.find_by_id(state_id):
            self._state_id = state_id
        else:
            raise ValueError("state_id must reference a reference in the database")


           
            
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            name TEXT,
            city_population INTEGER,
            state_id INTEGER,
            FOREIGN KEY (state_id) REFERENCES states(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS cities;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO cities (name, city_population, state_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.city_population, self.state_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE cities
            SET name = ?, city_population = ?, state_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.city_population, self.state_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM cities
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, city_population, state_id):
        city = cls(name, city_population, state_id)
        city.save()
        return city

    @classmethod
    def instance_from_db(cls, row):
        city = cls.all.get(row[0])
        if city:
            city.name = row[1]
            city.city_population = row[2]
            city.state_id = row[3]
        else:
            city = cls(row[1], row[2], row[3])
            city.id = row[0]
            cls.all[city.id] = city
        return city

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM cities
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM cities
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM cities
            WHERE name = 
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod

    def find_by_state(cls, state_id):
        sql = """
            SELECT *
            FROM cities
            WHERE state_id = ?
        """
        rows = CURSOR.execute(sql, (state_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def state(self):
        return State.find_by_id(self.state_id)
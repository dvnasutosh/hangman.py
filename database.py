
import contextlib
import sqlite3 as sq

class SqlLite:
    """
    A class to interact with a SQLite database.

    Methods:
        start(): Connects to the database.
        add(name, livesleft, difficulty): Adds a new winner to the database.
        getLeaderBoard(limit=10): Returns the leaderboard, limited to the specified number of rows.
    """

    def __init__(self) -> None:
        """
        Initializes the database connection.
        """
        self.start()
        # Creating winners Table if it doesnt exists
        self.conn.execute('''
                        CREATE TABLE IF NOT EXISTS difficulties(
                            id INTEGER PRIMARY KEY,
                            name VARCHAR(200) NOT NULL
                        )
                        ''')
        self.conn.commit()
        
        with contextlib.suppress(Exception):
            self.conn.execute('''
                            INSERT INTO difficulties(id,name)
                            VALUES(1, 'Easy'),
                                (2,'MODERATE'),
                                (3,'HARD');
                            ''')
            self.conn.commit()
        self.conn.execute('''
                        CREATE TABLE IF NOT EXISTS winners(
                            id INTEGER PRIMARY KEY,
                            name VARCHAR(200) NOT NULL,
                            lives_left TINYINT NOT NULL,
                            DIFFICULTY TINYINT NOT NULL,
                                
                            CONSTRAINT fk_department
                                FOREIGN KEY (DIFFICULTY)
                                REFERENCES difficulties(id)
                        )
                        
                        ''')
        self.conn.commit()

    def start(self):
        """
        Connects to the database.
        """
        self.conn = sq.connect('leaderboard.db')

    def add(self, name:str, livesleft:int, difficulty: int):
        """
        Adds a new winner to the database.

        Args:
            name (str): The winner's name.
            livesleft (int): The number of lives the winner had left.
            difficulty (int): The difficulty of the game.
        """
        self.start()
        
        cur = self.conn.cursor()
        
        cur.execute("""
                    INSERT INTO winners(name,lives_left, DIFFICULTY)
                    VALUES(?,?,?)
                """, (name, livesleft, difficulty))
        cur.close()
        self.conn.commit()
        self.conn.close()
        
    def getLeaderBoard(self, limit: int = 10):
        """
        Returns the leaderboard, limited to the specified number of rows.

        Args:
            limit (int, optional): The number of rows to return. Defaults to 10.

        Returns:
            list: The leaderboard, as a list of tuples.
        """
        self.start()
        query = f"""
                    SELECT winners.DIFFICULTY, difficulties.name, winners.name, winners.lives_left 
                    FROM winners
                    JOIN difficulties ON winners.DIFFICULTY = difficulties.id
                    ORDER BY winners.DIFFICULTY DESC, lives_left DESC
                    LIMIT {limit};
                """
        
        curr = self.conn.cursor()
        
        out=curr.execute(query).fetchall()
        self.conn.commit()
        curr.close()
    
        self.conn.close()
        return out

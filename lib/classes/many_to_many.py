class Game:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Game(title={self.title})"


    @property # GETTER
    def title(self):
    # Returns the game's title
        return self._title
    
    @title.setter #SETTER
    def title(self, title):
        if hasattr(self, "title"):
            raise Exception("Cannot change Game title after it's set")
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception("Game title must be a string longer than 0 characters, cannot change title after instantiation")


    def results(self):
        return [ result for result in Result.all_results if result.game == self ]

    def players(self):
        return set([ result.player for result in Result.all_results if result.game == self ])

    def average_score(self, player_instance):
        # step one: get all the results / scores between this game and the player arg
        scores_list = [ result.score for result in Result.all_results if result.game == self and result.player == player_instance ]
        # (self is a game)
        # step two: sum all the scores and divide by the number of scores
        sum_list = sum(scores_list)
        average_score = sum_list / len(scores_list)

        return average_score

class Player:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"Player(username={self.username})"

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Player username must be a string between 2 and 16 characters inclusive")

    def results(self):
        # loop through all the results
        # only return the results in a list that belong to this player
        return [ result for result in Result.all_results if result.player == self ]
            
    def games_played(self):
        return list( set( [ result.game for result in Result.all_results if result.player == self ] ) )

    def played_game(self, game):
        # Receives a game object as argument
        # Returns True if the player has played the game object provided
        # Returns False otherwise
        # for g in self.games_played():
        #     if g == game:
        #         return True

        # return False
        return game in self.games_played()

    def num_times_played(self, game):
        # we'll need a counter --> sum
        counter = 0
        for result in self.results():
            if result.game == game:
                counter += 1

        return counter
        # how many times they've gotten a result in that game --> integer


class Result:

    all_results = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all_results.append(self)

    def __repr__(self):
        return f"Result(score={self.score}, player={self.player.username}, game={self.game.title})"

    @property # GETTER
    def score(self):
        return self._score
    
    @score.setter # SETTER
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, 'score'):
            self._score = score
        else:
            raise Exception("Score must be an integer between 1 and 5000")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        if type(value) == Player:
        # if isinstance(value, Player):
            self._player = value
        else:
            raise Exception("Player must be of type Player")

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, value):
        if type(value) == Game:
            self._game = value
        else:
            raise Exception("Game must be of type Game")
        
# Result(player=player_one)
'''Player class to record stats for individual players
'''


class Player:
    '''Dosctring TODO
    THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay
    '''
    def __init__(self, name=None, yards=0, touchdowns=0, safety=0,
                 interceptions=0, field_goals=0):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.touchdowns
        safety_points = 2 * self.safety
        field_goal = 3 * self.field_goals
        total_points = td_points + safety_points+field_goal
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

class Defensive(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to Defensive Player'''
    
    def __init__(self,tackles, sacks, name=None, yards=0, touchdowns=0, safety=0,
                 interceptions=0, field_goals=0):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.tackles = tackles
        self.sacks = sacks

    def defensive_score(self):
        score = (self.tackles * 1) + (self.sacks * 3) + (self.interceptions * 5)
        return score
# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.

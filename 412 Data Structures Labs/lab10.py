'''
Andrew Kozempel
CMPSC 412
Lab 10
Fall 2023
'''

class GymMatcher:
    def __init__(self):  
        
        # Dictionary of dictionaries - store user information
        self.user_data = {}

        # dictionary of lists - matches for specific lifts
        self.bench_matches = {}
        self.deadlift_matches = {}
        self.squat_matches = {}

        # graphs (dictionaries of sets) - match 'networks' for each lift
        self.bench_graph = {}
        self.deadlift_graph = {}
        self.squat_graph = {}

    # adds user info to the user_data
    def add_user(self, name, bench_stat, deadlift_stat, squat_stat):

        # dictionary with user info for the user_data dictionary.
        self.user_data[name] = {
            "bench": bench_stat,
            "deadlift": deadlift_stat,
            "squat": squat_stat
        }

        # add name to matches dictionaries
        self.add_to_matches(name, bench_stat, "bench")
        self.add_to_matches(name, deadlift_stat, "deadlift")
        self.add_to_matches(name, squat_stat, "squat")

        # initialize node in graphs
        self.bench_graph[name] = set()
        self.deadlift_graph[name] = set()
        self.squat_graph[name] = set()

        # add edges for each graph
        for lift_type in ['bench', 'deadlift', 'squat']:
            self.add_edges(lift_type)
    
    # removes user info to the user_data
    def remove_user(self, name):

        # check if valid user
        if name in self.user_data:

            # delete from user data
            del self.user_data[name]

            # delete user from matching dictionaries
            for match_dict in [self.bench_matches, self.deadlift_matches, self.squat_matches]:
                for weight, users in list(match_dict.items()):
                    if name in users:
                        users.remove(name)

            # delete user from matching graphs
            for graph in [self.bench_graph, self.deadlift_graph, self.squat_graph]:
                if name in graph:
                    del graph[name]
                    for users in graph.values():
                        users.discard(name)
        else:
            print(f"User {name} not found.")

    # updates user info in user_data
    def update_user(self, name, bench_stat, deadlift_stat, squat_stat):

        # check if valid user
        if name not in self.user_data:
            print(f"User {name} not found.")
            return

        # remove user with old stats and add again with new stats
        self.remove_user(name)
        self.add_user(name, bench_stat, deadlift_stat, squat_stat)

    # print user info
    def get_user_info(self, name):
        
        # print user info, if valid user
        if name in self.user_data:
            print(f"{name}: {self.user_data[name]}.")
        
        # invalid user
        else:
            print(f"User {name} not found.")

    # add user to matches dictionary
    def add_to_matches(self, name, weight, lift_type):

        # round the weight to closest 5lbs
        rounded_weight = 5 * round(weight / 5)

        # determine which 'matches' dictionary to look in
        if lift_type == "bench":
            lift_matches = self.bench_matches

        elif lift_type == "deadlift":
            lift_matches = self.deadlift_matches

        elif lift_type == "squat":
            lift_matches = self.squat_matches

        # depending on the exercise, 
        # if the rounded weight does not exist yet, 
        # then you can create it as a key. 
        # add the new name as a value.
        if rounded_weight not in lift_matches:
            lift_matches[rounded_weight] = []

        lift_matches[rounded_weight].append(name)

    # determine matches of specified user within +/- 5lbs
    def get_matches(self, name, lift_type):

        # make sure user exists
        if name not in self.user_data:
            print("\n\tUser not found.")
            return 

        # get user's weight for specified exercise
        target_stat = self.user_data[name][lift_type]

        # round weight to nearest 5lbs
        rounded_weight = 5 * round(target_stat / 5)

        # print statement for
        print(f'\nMatches for {name} ({rounded_weight}lbs {lift_type.capitalize()}):')

        # determine which 'matches' dictionary to look in
        if lift_type == "bench":
            potential_matches = self.bench_matches

        elif lift_type == "deadlift":
            potential_matches = self.deadlift_matches

        elif lift_type == "squat":
            potential_matches = self.squat_matches

        # check exact weight, as well as +/- 5lbs for matches
        for weight in [rounded_weight, rounded_weight-5, rounded_weight+5]:

            # if weight exists in dictionary
            if weight in potential_matches:

                # create a string from matches
                matches = ', '.join([match for match in potential_matches[weight] if match != name])
                
                # if there are matches, print them
                # print 'None' otherwise
                if matches != '':
                    print(f'\n\tMatches @ {weight}lbs: {matches}')
                else:
                    print(f'\n\tMatches @ {weight}lbs: None')

            # if weight isn't in the dictionary, print 'None' 
            else:
                print(f'\n\tMatches @ {weight}lbs: None')

    # add matches/connections to user nodes
    def add_edges(self, lift_type):

        # set specified dictionary based on exercise
        if lift_type == "bench":
            match_dict = self.bench_matches
            graph = self.bench_graph
        elif lift_type == "deadlift":
            match_dict = self.deadlift_matches
            graph = self.deadlift_graph
        elif lift_type == "squat":
            match_dict = self.squat_matches
            graph = self.squat_graph


        for weight, users in match_dict.items():
            for user in users:
                # add an edge between this user and all other users in the same weight category
                graph[user].update(set(users) - {user})

    # print specified graph
    def print_graph(self, graph):

        # for each user and its edges/matches
        for user, connections in graph.items():

            # convert matches to string and print
            connections_str = ', '.join(connections)
            print(f"\t{user}: {connections_str}")

    # print all 3 graphs
    def print_all_graphs(self):
        print("\nBench Graph:\n")
        self.print_graph(self.bench_graph)

        print("\nDeadlift Graph:\n")
        self.print_graph(self.deadlift_graph)

        print("\nSquat Graph:\n")
        self.print_graph(self.squat_graph)


# initialize
gym_matcher = GymMatcher()

print('\n===========================================')
print('=====  RAW DATA AFTER INITIALIZATION  =====')
print('===========================================')

# show 'raw' data structure attributes
print(f'\nuser_data: {gym_matcher.user_data}')
print(f'\nbench_matches: {gym_matcher.bench_matches}')
print(f'\ndeadlift_matches: {gym_matcher.deadlift_matches}')
print(f'\nsquat_matches: {gym_matcher.squat_matches}')
print(f'\nbench_graph: {gym_matcher.bench_graph}')
print(f'\ndeadlift_graph: {gym_matcher.deadlift_graph}')
print(f'\nsquat_graph: {gym_matcher.squat_graph}')

# add users to user info
gym_matcher.add_user("User1", 195, 300, 250)
gym_matcher.add_user("User2", 195, 310, 245)
gym_matcher.add_user("User3", 200, 300, 265)
gym_matcher.add_user("User4", 180, 290, 245)
gym_matcher.add_user("User5", 205, 350, 270)
gym_matcher.add_user("User6", 190, 295, 245)
gym_matcher.add_user("User7", 210, 350, 280)
gym_matcher.add_user("User8", 180, 290, 250)
gym_matcher.add_user("User9", 210, 315, 265)
gym_matcher.add_user("User10", 195, 315, 230)
gym_matcher.add_user("User11", 210, 350, 245)

print('\n\n=======================================')
print('=====  RAW DATA AFTER INSERTIONS  =====')
print('=======================================')
# show 'raw' data structure attributes
print(f'\nuser_data: {gym_matcher.user_data}')
print(f'\nbench_matches: {gym_matcher.bench_matches}')
print(f'\ndeadlift_matches: {gym_matcher.deadlift_matches}')
print(f'\nsquat_matches: {gym_matcher.squat_matches}')
print(f'\nbench_graph: {gym_matcher.bench_graph}')
print(f'\ndeadlift_graph: {gym_matcher.deadlift_graph}')
print(f'\nsquat_graph: {gym_matcher.squat_graph}')

# show matching graph
print('\n\n=======================================')
print('=====  PRINTING ALL MATCH GRAPHS  =====')
print('=======================================')
gym_matcher.print_all_graphs()

# get matches for specified user
print('\n\n=====================================')
print('=====  PRINTING USER11 MATCHES  =====')
print('=====================================')
gym_matcher.get_matches("User11", "bench")

# update and get matches again
print('\n\n===================================')
print('=====  MATCHES AFTER UPDATING =====')
print('===================================')
gym_matcher.update_user("User11", 195, 350, 245)
gym_matcher.get_matches("User11", "bench")

# remove and get matches again
print('\n\n===================================')
print('=====  MATCHES AFTER REMOVING =====')
print('===================================')
gym_matcher.remove_user("User11")
gym_matcher.get_matches("User11", "bench")

# print user info of user 10
print('\n\n===================================')
print('=======  User10 INFORMATION =======')
print('===================================\n')
gym_matcher.get_user_info("User10")
print('\n===================================\n')
# Dict data of DataSciencester network that contains user's id and name 
users = [
    {"id": 0, "name": "Hero" },
    {"id": 1, "name": "Dunn" },
    {"id": 2, "name": "Sue" },
    {"id": 3, "name": "Chi" },
    {"id": 4, "name": "Thor" },
    {"id": 5, "name": "Clive" },
    {"id": 6, "name": "Hicks" },
    {"id": 7, "name": "Devin" },
    {"id": 8, "name": "Kate" },
    {"id": 9, "name": "Klein" }
] 
print(users)

# Friendship data based on their id number:
friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
                    (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j) # Add j as a friend of user i
    friendships[j].append(i) # Add i as a friend of user j

print(friendships)

def number_of_friends(user):
    """how many frends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users) # 24
print(total_connections)

num_users = len(users)                                  # length of the users list
avg_connections = total_connections / num_users        # 24 / 10 == 2.4 


# Create a list (user_id, number_of_friends). 
num_friends_by_id = [(user["id"], number_of_friends(user))
                        for user in users]
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True)

# Each pair is (user_id, num_friends):
# [(1,3), (2,3), (3,3), (5,3), (8,3),
#  (0,2), (4,2), (6,2), (7,2), (9,1)]
   
# continued

def foaf_ids_bad(user):
    """foaf is shot for "friend of a friend" """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_ids_bad
        for foaf_id in friendships[user_id]
        for foaf_id in friendships[friend_in]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )
print(friends_of_friends(users[3]))
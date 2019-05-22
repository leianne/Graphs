import random
from queue import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, numUsers):
            self.addUser(f'User {i}')
        # Create friendships
        possibleFriendships = []

        for userID in self.users:
            # for friendID in range(1, 2):
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        random.shuffle(possibleFriendships)
        for i in range(numUsers * avgFriendships //2):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # {1: {2, 3, 4}, 2: {1, 5}, 3: {1, 4}, 4: {1, 3}, 5: {2}}
        # 1 - 2 - 5
        # 1 - 3 - 4
        
        q = Queue() # []
        q.enqueue([userID]) #[1]
        visited = {}  # Note that this is a dictionary, not a set
        # What we are trying to return 
        # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        # VISITED 
        # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
        # [] Grap 1st User from queue
        # If user not in visited add to visited
        # !!!! IMPLEMENT ME
        while q.size() > 0:
            path = q.dequeue() 
            current = path[-1]
            if current not in visited:
                visited[current] = path
                for i in self.friendships[current]:
                    path_copy = path.copy()
                    path_copy.append(i)
                    q.enqueue(path_copy)
            # print(f'Visited : {visited}')
            # print(f'Queue: {q.queue}')
            # print(f'self.friendships: {self.friendships[userID]}')     
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populateGraph(10, 3)
    sg.friendships = {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(f' connections {connections}')

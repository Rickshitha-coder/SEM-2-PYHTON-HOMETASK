'''You are a developer at a school, and you have been given a dictionary containing students' names 
and their marks in a test. [Use lambda function and methods for each task]
Your task is to:
1. Sort students by marks in ascending order.
2. Sort students by marks in descending order.
3. Find the top 3 students with the highest marks.
4. Sort students by name alphabeticall'''
class Detail:
    def __init__(self):
        self.students = {
            "Rickshi": 85,
            "Mirthula": 92,
            "Monash": 78,
            "Dev": 88,
            "Shreeman": 95,
            "Vicky": 80,
            "Dharshan": 90,
        }

    def sorted_students_asc(self):
        return dict(sorted(self.students.items(), key=lambda item: item[1]))

    def sorted_students_desc(self):
        return dict(sorted(self.students.items(), key=lambda item: item[1], reverse=True))

    def top_students(self):
        return dict(sorted(self.students.items(), key=lambda item: item[1], reverse=True)[:3])

    def sorted_students_alpha(self):
        return dict(sorted(self.students.items()))

    def Display(self):
        print("Students sorted by marks in ascending order:")
        for student, marks in self.sorted_students_asc().items():
            print(f"{student}: {marks}")
        print("\nStudents sorted by marks in descending order:")
        for student, marks in self.sorted_students_desc().items():
            print(f"{student}: {marks}")
        print("\nTop 3 students with the highest marks:")
        for student, marks in self.top_students().items():
            print(f"{student}: {marks}")
        print("\nStudents sorted by name alphabetically:")
        for student, marks in self.sorted_students_alpha().items():
            print(f"{student}: {marks}")

c = Detail()
c.Display()

'''Sorting a List of Tuples Using Lambda
Scenario
You are working as a data analyst for a sports organization. You have a list of tuples where each tuple 
represents a player's name and their total number of goals scored in a football season.
Your task is to:
1. Sort the players by goals scored in ascending order.
2. Sort the players by goals scored in descending order.
3. Find the top 3 goal scorers.
4. Sort players by their names alphabetically.
5. Find employees earning more than $5000'''
class Sports:
    def __init__(self):
        self.players = [
            ("Pele", 67),
            ("Lionel Messi", 45),
            ("Crisitna Ronaldo", 80),
            ("Kylian", 65),
            ("Neymar", 89),
            ("Erling Haaland", 56),
            ("Hazard", 26),
            ("Suarez", 10),
            ("Griezmann", 21)
        ]

    def sorted_players_asc(self):
        return sorted(self.players, key=lambda x: x[1])

    def sorted_players_desc(self):
        return sorted(self.players, key=lambda x: x[1], reverse=True)

    def top_scorers(self):
        return sorted(self.players, key=lambda x: x[1], reverse=True)[:3]

    def sorted_players_alpha(self):
        return sorted(self.players, key=lambda x: x[0])

    def display(self):
        print("Players sorted by goals scored in ascending order:")
        for player in self.sorted_players_asc():
            print(player)
        print("\nPlayers sorted by goals scored in descending order:")
        for player in self.sorted_players_desc():
            print(player)
        print("\nTop 3 goal scorers:")
        for player in self.top_scorers():
            print(player)
        print("\nPlayers sorted by their names alphabetically:")
        for player in self.sorted_players_alpha():
            print(player)

s = Sports()
s.display()

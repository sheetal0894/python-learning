skills = {"Python","AWS","Docker"}
class Skill:
 def __init__(self,skills):
        self.skills = skills

 def details(self):
        for i in self.skills:
            print(f"{i} is a skill")

skill_details = Skill(skills)
skill_details.details()
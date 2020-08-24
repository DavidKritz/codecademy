class Pokemon:

    def __init__(self, name, level, poke_type, max_health = 100, curr_health = 100, knocked_out = "false"):
        self._name = name
        self._level = level
        self._poke_type = poke_type
        self._max_health = max_health
        self._curr_health = curr_health
        self._knocked_out = knocked_out
        self._exp_points = 0
        self._attck = 0

    def get_name(self): 
        print("getter method called")
        return self._name
       
    def set_name(self, n): 
        print("setter method called") 
        self._name = n 

    def get_curr_health(self):
        return self._curr_health

    def set_curr_health(self, ch):
        self._curr_health = ch
        if self._curr_health > self._max_health:
            self._curr_health = self._max_health
        print("Your current health is {}.".format(self._curr_health))

    def get_level(self): 
        print("getter method called") 
        return self._level
       
    def set_level(self, l): 
        print("{} has reached level {}.".format(self._name, self._level) )
        self._level = l 

    def get_poke_type(self): 
        print("getter method called") 
        return self._poke_type
       
    def set_poke_type(self, t): 
        print("setter method called") 
        self._poke_type = t

    def get_exp_points(self): 
        print("getter method called") 
        return self._exp_points
       
    def set_exp_points(self, xp): 
        print("setter method called") 
        self._exp_points = xp

    def lose_health(self, lh):
        self._curr_health = self._curr_health - lh
        if self._curr_health <= 0:
            knockout_poke()
            self._curr_health = 0
            print("You have been knocked out!!!")

    def regain_health(self, rh):
        self._curr_health = self._curr_health + rh
        print("{} has {} health available.".format(self._name, self._curr_health)) 

    def knockout_poke(self):
        self._knocked_out = 'true'

    def revive_poke(self):
        self._knocked_out = false
        self._curr_health = 100
        print("You have been revived to full health.")

    def attack(self, opponent):
        fire_attack = 20
        grass_attack = 5
        water_attach = 10
        if self._knocked_out == "true":
            print("You {} are unconcious, you cannot attack anyone else!".format(self._name))
            return
        if self._poke_type == "Grass" and opponent._poke_type == "Fire":
            self._attck = grass_attack * 0.5
        elif self._poke_type == "Grass" and opponent._poke_type == "Water":
            self._attck = grass_attack * 2
        elif self._poke_type == "Water" and opponent._poke_type == "Fire":
            self._attck = water_attack + 2
        elif self._poke_type == "Water" and opponent._poke_type == "Grass":
            self._attck = water_attack * 0.5
        elif self._poke_type == "Fire" and opponent._poke_type == "Grass":
            self._attck = fire_attack * 2
        elif self._poke_type == "Fire" and opponent._poke_type == "Water":
            self._attck = fire_attack * 0.5
        opponent.set_curr_health(opponent._curr_health - self._attck)
        self.gain_exp(self._attck)
        print("{} has attacked {}, and done {} damage.".format(self._name, opponent._name, self._attck))

    def gain_exp(self, xp):
        exp = self._exp_points + self._attck
        if 0 < exp and exp < 1001:
            self.set_level(1)
            print("You are at level {}.".format(self._level))
        elif 1000 < exp and exp < 2001:
            self.set_level(2)
        elif 2000 < exp and exp < 3001:
            self.set_level(3)
        elif 3000 < exp and exp < 4001:
            self.set_level(4)
        elif 4000 < exp and exp < 5001:
            self.set_level(5)
        elif 5000 < exp and exp < 6001:
            self.set_level(6)
        elif 6000 < exp and exp < 7001:
            self.set_level(7)
        elif 7000 < exp and exp < 8001:
            self.set_level(8)



class Trainer:
    

    def __init__(self, name, sm_potions, md_potions, lg_potions,  trainees, ap):
        self._name = name
        self._sm_potions = sm_potions
        self._md_potions = md_potions
        self._lg_potions = lg_potions
        self._trainees = trainees
        self._ap = ap
        self._currently_active_p = ap - 1
        self._attck = 0

    def get_name(self): 
        print("getter method called") 
        return self._name
       
    def set_name(self, n): 
        print("setter method called") 
        self._name = n 

    def get_sm_potions(self): 
        print("getter method called") 
        return self._sm_potions
       
    def set_sm_potions(self, sp): 
        print("setter method called") 
        self._sm_potions = sp 

    def get_md_potions(self): 
        print("getter method called") 
        return self._md_potions
       
    def set_md_potions(self, mp): 
        print("setter method called") 
        self._md_potions = mp 

    def get_lg_potions(self): 
        print("getter method called") 
        return self._lg_potions
       
    def set_lg_potions(self, lp): 
        print("setter method called") 
        self._lg_potions = lp 


    def get_currently_active_p(self): 
        print("getter method called") 
        return self._currently_active_p
       
    def set_currently_active_p(self, p): 
        print("setter method called") 
        if self._trainees[self._ap - 1]._knocked_out == "true":
            print("{} is knocked out. You cannot switch.".format(self._trainees[self._ap - 1]._name))
            return
        self._currently_active_p = p-1 

    def get_trainees(self): 
        print("getter method called") 
        return self._trainees
       
    def set_trainees(self, p): 
        print("setter method called") 
        self._trainees = trainees

    def attack(self, opponent):
        fire_attack = 20
        grass_attack = 5
        water_attack = 10
        if self._trainees[self._ap - 1]._poke_type == "Grass" and opponent._poke_type == "Fire":
            self._attck = grass_attack * 0.5
        elif self._trainees[self._ap - 1]._poke_type == "Grass" and opponent._poke_type == "Water":
            self._attck = grass_attack * 2
        elif self._trainees[self._ap - 1]._poke_type == "Water" and opponent._poke_type == "Fire":
            self._attck = water_attack + 2
        elif self._trainees[self._ap - 1]._poke_type == "Water" and opponent._poke_type == "Grass":
            self._attck = water_attack * 0.5
        elif self._trainees[self._ap - 1]._poke_type == "Fire" and opponent._poke_type == "Grass":
            self._attck = fire_attack * 2
        elif self._trainees[self._ap - 1]._poke_type == "Fire" and opponent._poke_type == "Water":
            self._attck = fire_attack * 0.5
        opponent.set_curr_health(opponent._curr_health - self._attck)
        self._trainees[self._ap - 1].gain_exp(self._attck)
        print("{} has attacked {}, and done {} damage.".format(self._trainees[self._ap - 1]._name, opponent._name, self._attck))

    def heal_trainee(self, t):
        small_potion = 10
        medium_potion = 20
        large_potion = 50
        if t == "small":
            if self._sm_potions == 0:
                print("No more small potions to prescribe.")
                return 
            total_health = self._trainees[self._ap - 1].get_curr_health() + small_potion
            self.set_sm_potions(self._sm_potions - 1)
        elif t == "medium":
            if self._sm_potions == 0:
                print("No more medium potions to prescribe.")
                return 
            total_health = self._trainees[self._ap - 1].get_curr_health() + medium_potion
            self.set_md_potions(self._md_potions - 1)
        elif t == "large":
            if self._sm_potions == 0:
                print("No more large potions to prescribe.")
                return 
            total_health = self._trainees[self._ap - 1].get_curr_health() + large_potion
            self.set_lg_potions(self._lg_potions - 1)
        self._trainees[self._ap - 1].set_curr_health(total_health)
        print("You have healed {}.".format(self._trainees[self._ap - 1]._name))

sam_fire = Pokemon("SamFire", 2, "Fire", 100, 100, "false")
dave_fire = Pokemon("DavidFire", 2, "Fire", 100, 100, "false")
john_water = Pokemon("JohnWater", 2, "Water", 100, 100, "false")
sue_water = Pokemon("SueWater", 2, "Water", 100, 100, "false")
pete_grass = Pokemon("PeterGrass", 2, "Grass", 100, 100, "false")
jul_grass = Pokemon("JulieGrass", 2, "Grass", 100, 100, "false")
#sam_fire.knockout_poke()
sam_fire.attack(pete_grass)
tr_list = [sam_fire, dave_fire, john_water, sue_water, pete_grass, jul_grass]
sam_trainer = Trainer("SamTrainer", 10, 10, 10, tr_list, 1)
sam_trainer.get_currently_active_p()
sam_trainer.set_currently_active_p(3)
sam_trainer.heal_trainee("small")
sam_trainer.attack(pete_grass)

import hashlib
import fileinput
import operator

from Shared.gameSettings import GameSettings


class UserScore:

    def __init__(self):
        self.__userscore = self.load()

    def get_users(self):
        return self.__userscore

    def load(self):
        users_score = []
        for line in fileinput.input(GameSettings.USER_DATA):
            name, score, md5 = line.split('[::]')
            md5 = md5.replace('\n', '')

            if str(hashlib.md5(str.encode(str(name+score+GameSettings.SALT))).hexdigest()) == str(md5):
                users_score.append([str(name), int(score), str(md5)])

        users_score.sort(key=operator.itemgetter(1), reverse=True)
        users_score = users_score[1:12]

        return users_score

    def add_score(self, name, score):
        hash = hashlib.md5((str(name+str(score)+GameSettings.SALT)).encode('utf'))
        self.__userscore.append([name, str(score), hash.hexdigest()])

        with open(GameSettings.USER_DATA, "w") as user_file:
            for name, score, md5 in self.__userscore:
                user_file.write(str(name)+"[::]"+str(score)+"[::]"+str(md5)+"\n")
